import os
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename  # <-- import this
from .extractor import extract_text_from_pdf, extract_details

views = Blueprint("views", __name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@views.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['resume']
        if uploaded_file.filename.endswith('.pdf'):
            # Sanitize filename
            safe_filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, safe_filename)
            uploaded_file.save(filepath)

            text = extract_text_from_pdf(filepath)
            result = extract_details(text)

            return render_template('index.html', result=result)

    return render_template('index.html', result=None)
