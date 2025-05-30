import os
from dotenv import load_dotenv
from memory import memory_store
from google import genai

load_dotenv()

def process_pdf(data,filename,intent):

    client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

    sender = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Extract just the sender's name from the text and if there is no sender just say unknown\n {data}",
    )
    urgency = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Classify the urgency of this text into by just saying High or Medium or Low\n {data}",
    )
    print(f"source: {filename}\nformat: PDF\nIntent: {intent}\nAgent: pdfAgent\nSender: {sender.text.strip()}\nUrgency: {urgency.text.strip()}\n\n")
    memory_store.log({
        "source": filename,
        "format": "PDF",
        "intent": intent,
        "agent": "pdfAgent",
        "sender": sender.text.strip(),
        "urgency": urgency.text.strip()
    })
