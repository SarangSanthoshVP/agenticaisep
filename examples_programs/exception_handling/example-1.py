def call_gemini(**geminiInput):
    try:
        print("Model:", geminiInput["model"])
        print("Prompt:", geminiInput["prompt"])
        print("Cost:", geminiInput["token"]+100)
    except KeyError as e:               #means if key is not present in dictionary then it will throw error and we can catch that error using KeyError
        print("Please provide all the input:", e)
    except Exception as e:             #means if any other error occurs then it will catch that error and print the error message
        print("Error Occurred:", e)
    finally:                  #alwasys executed wether there is error or not    
        print("Call Done")


call_gemini(
    model="3.8-pro",
    prompt="What is Python?",
    token='100'
)