def make_api_call(model, prompt, **params):
    print("Model:", model)
    print("Prompt:", prompt)

    print(params)

    print("Making API Call")
    if model=="Gemini":
        print(params.get("tokens"), params.get("gemini_api_key"), params.get("precision"))
    elif model=="Claude":
        print(params.get("tokens"), params.get("claude_token"))
    elif model=="chatgpt":
        print(params.get("chatgpt_account_id"), params.get("password"), params.get("precision"))


make_api_call(
    model="Gemini", 
    prompt="What is Python", 
    tokens=10, 
    gemini_api_key="4terfdeq3r4terfsdwe3", 
    precision="1"
)
make_api_call(
    model="Claude", 
    prompt="What is Python", 
    tokens=10, 
    claude_token="123456743214",
)
make_api_call(
    model="chatgpt", 
    prompt="What is Python", 
    chatgpt_account_id=11324560, 
    password="23456",
    precision="2"
)