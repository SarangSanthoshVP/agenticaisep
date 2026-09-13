def call_gemini(model, prompt):
    print("Model:", model)
    print("Prompt:", prompt)
    return {
        "status": "success",
        "code": "print('hello')",
        "tokens": 343,
        "language": "python",
        "isDone": True 
    }

response = call_gemini("3.8-flash", "Print hello code in python")
print(response)
print("Code:", response["code"], "Language:", response["language"])
print("Cost:", response["tokens"]+1000)