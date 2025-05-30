from memory import memory_store

def process_json(payload,filename,intent):
    required = ["id", "type", "price"]
    missing = [key for key in required if key not in payload]
    result = {
        "valid": not missing,
        "missing_fields": missing,
    }
    print(f"source: {filename}\nformat: JSON\nIntent: {intent}\nAgent: JsonAgent\n\n")
    memory_store.log({
        "source": filename,
        "format": "JSON",
        "intent": intent,
        "agent": "JsonAgent",
        "sender": 'None',
        "urgency": 'None'
    })
    print(result)
