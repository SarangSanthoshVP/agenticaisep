import json


def call_gemini(geminiInput,prompt):
    print("Model:", geminiInput["model"])
    print("api_token", geminiInput["api_token"])
    print("tokens:", geminiInput["tokens"])
    print("Prompt:", prompt)

    return {
          "status":"success",
          "cost":234,
          "response":"Hello"
    }

with open("gemini-config.json","r") as file:
        geminiInput=json.loads(file.read())
        

 #same location   so just "gemini-config.json" 

response=call_gemini(geminiInput,"what is oops")

with open("gemini-response.json","w") as file:
      json.dump(response, file, indent=4)



