# 🧠 Resume Skill Extractor

An AI-powered web application that extracts structured information from PDF resumes, including:
- Full Name
- Email Address
- Phone Number
- Technical Skills

Built using **Flask**, **spaCy**, **PyMuPDF**, and **Docker**. Styled with a custom UI using HTML + CSS.

---

## 🚀 Features

✅ Upload `.pdf` resumes via a simple web UI  
✅ Automatically extract name, email, phone, and skills using NLP and regex  
✅ Clean and modern frontend design with a custom color palette  
✅ Dockerized for easy deployment  
✅ Built and optimized using **Windsurf** (Codeium's AI IDE)

---

## 🖥️ Demo

> Replace this with your deployed link or demo video if available.

---

## 🛠️ Tech Stack

| Component       | Tech        |
|----------------|-------------|
| Backend        | Flask       |
| PDF Parsing    | PyMuPDF     |
| NLP            | spaCy       |
| Frontend       | HTML + CSS  |
| Containerization | Docker     |
| IDE Used       | Windsurf (Codeium) |

---

## 📦 Installation

### 1. Clone the repo

    git clone https://github.com/YOUR_USERNAME/resume_extractor.git
    cd resume_extractor

2. Create virtual environment

        python -m venv venv
        venv\Scripts\activate    # On Windows
        # OR
        source venv/bin/activate # On macOS/Linux
 3. Install dependencies
    
        pip install -r requirements.txt
        python -m spacy download en_core_web_sm
    
 4. Run the app 

         python run.py
    
    App will be live at: http://localhost:5000
  
5. Run with Docker

        docker build -t resume-extractor .
        docker run -p 5000:5000 resume-extractor
   
 Project Structure :

     resume_extractor/
      ├── app/
      │   ├── __init__.py
      │   ├── routes.py
      │   ├── extractor.py
      │   ├── templates/
      │   │   └── index.html
      │   └── uploads/
      ├── Dockerfile
      ├── requirements.txt
      ├── run.py
      └── README.md

 Screenshots :
  🔹 Homepage before uploading a resume – clean upload interface
  ![image](https://github.com/user-attachments/assets/d8fdfde2-4dac-4059-a17c-54676c977541)

  🔹 User selecting and uploading a PDF resume
  ![image](https://github.com/user-attachments/assets/7f86fb56-b890-49ce-99ce-abe24d3365f4)

  🔹 Extracted name, email, phone, and skills displayed clearly
  ![image](https://github.com/user-attachments/assets/987e50c4-1975-4818-96d9-8a5ff61a5515)

Built with Windsurf :
This project was built using Windsurf by Codeium, an agentic AI IDE.
Windsurf AI helped rapidly scaffold and optimize routes, parsing logic, Dockerization, and frontend styling.




  
