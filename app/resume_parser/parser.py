from PyPDF2 import PdfReader

def extract_resume_text(pdf_file):

    text = ""

    pdf_reader = PdfReader(pdf_file)

    for page in pdf_reader.pages:
        content = page.extract_text()

        if content:
            text += content

    return text

