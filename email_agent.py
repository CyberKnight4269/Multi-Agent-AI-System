import os
from dotenv import load_dotenv
from memory import memory_store
from google import genai

load_dotenv()

def process_email(text,filename,intent):
    client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

    sender = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Extract just the sender's name from the email and if there is no sender just say unknown\n {text}",
    )
    urgency = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Classify the urgency of this email into by just saying High or Normal\n {text}",
    )
    print(f"source: {filename}\nformat: Email\nIntent: {intent}\nAgent: EmailAgent\nSender: {sender.text.strip()}\nUrgency: {urgency.text.strip()}\n\n")
    memory_store.log({
        "source": filename,
        "format": "Email",
        "intent": intent,
        "agent": "EmailAgent",
        "sender": sender.text.strip(),
        "urgency": urgency.text.strip()
    })

