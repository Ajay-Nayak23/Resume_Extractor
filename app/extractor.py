import re
import fitz
import spacy

nlp = spacy.load("en_core_web_sm")

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
PHONE_REGEX = r'\+?\d[\d\-\(\) ]{7,}\d'

STATIC_SKILL_SET = {
    'Python', 'Java', 'C++', 'SQL', 'HTML', 'CSS', 'JavaScript',
    'React', 'ReactJS', 'Django', 'Django REST Framework', 'Bootstrap',
    'Redux Toolkit', 'Flask', 'Git', 'PyTorch', 'TensorFlow',
    'Machine Learning', 'Deep Learning', 'OpenCV', 'PyBullet',
    'SMTP', 'API Integration', 'API', 'Linux', 'MongoDB', 'MySQL'
}

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_full_name(text):
    lines = text.strip().split('\n')[:5]  # First 5 lines of the resume
    for line in lines:
        line = line.strip()
        if (
            1 <= len(line.split()) <= 4
            and '@' not in line
            and not re.search(PHONE_REGEX, line)
            and not any(keyword in line.lower() for keyword in ['academic', 'profile', 'degree', 'email', 'phone'])
        ):
            return line
    return "Not found"

def extract_details(text):
    doc = nlp(text)

    # Extract name using the improved method
    name = extract_full_name(text)

    # Email
    email_matches = re.findall(EMAIL_REGEX, text)
    email = email_matches[0] if email_matches else "Not found"

    # Phone
    phone_matches = re.findall(PHONE_REGEX, text)
    phone = phone_matches[0] if phone_matches else "Not found"

    # Skills: match from static set only
    text_lower = text.lower()
    found_static_skills = {
        skill for skill in STATIC_SKILL_SET if skill.lower() in text_lower
    }
    skills = sorted(found_static_skills)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills
    }
