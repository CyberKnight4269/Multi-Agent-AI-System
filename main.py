import sys
from classifier_agent import classify_input
# from memory import memory_store

if len(sys.argv) != 2:
    print("Usage: python main.py <file_path>")
try:
    path = sys.argv[1]
    with open(path, "rb") as f:
        content = f.read()
    # result = classify_input(content, path)
    classify_input(content, path)
    # print("\n🧾 Result:\n", result)
    # print("\n📚 Memory Log:")
    # memory_store.show()
except Exception as e:
    print("Error:", e)