import os
from dotenv import load_dotenv
import fitz
import json
from google import genai

load_dotenv()

def classify_input(path):
    filename=path
    format_type = detect_format(filename)
    if format_type == "PDF":
        doc = fitz.open(path)
        data = "\n".join([page.get_text() for page in doc])
        doc.close()
        intent = detect_intent(data)
        from pdf_agent import process_pdf
        return process_pdf(data,filename,intent)
    else:
        with open(path, "rb") as f:
            data = f.read()
        intent = detect_intent(data)

    if format_type == "Email":
        from email_agent import process_email
        process_email(data,filename,intent)
    elif format_type == "JSON":
        from json_agent import process_json
        process_json(json.loads(data),filename,intent)
    else:
        print("error: Unsupported file format")

def detect_format(filename):
    if filename.endswith(".json"):
        return "JSON"
    if filename.endswith(".pdf"):
        return "PDF"
    if filename.endswith(".txt"):
        return "Email"
    return "Unknown"

def detect_intent(data):
    client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

    intent = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Classify the intent of the text in a single word if possible. Example-Invoice, RFQ, Complaint, Regulation, etc.\n {data}",
    )

    return intent.text.strip()