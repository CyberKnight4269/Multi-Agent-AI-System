import os
from dotenv import load_dotenv
import json
from google import genai

load_dotenv()

def classify_input(data, filename):
    format_type = detect_format(data, filename)
    intent = detect_intent(data)

    if format_type == "Email":
        from email_agent import process_email
        process_email(data,filename,intent)
    elif format_type == "JSON":
        from json_agent import process_json
        process_json(json.loads(data),filename,intent)
    # elif format_type == "PDF":
    #     from pdf_agent import process_pdf
    #     return process_pdf(data)
    else:
        return {"error": "Unsupported format"}

def detect_format(data, filename):
    if filename.endswith(".json"):
        return "JSON"
    if filename.endswith(".pdf") or b"%PDF" in data:
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