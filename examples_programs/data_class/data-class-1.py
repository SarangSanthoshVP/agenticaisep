from dataclasses import dataclass, asdict

@dataclass        #telling python that this is a data class and it takes care of the init method and other methods
class GeminiInput:
    model: str
    prompt: str
    tokens: int
    temperature=10.0


def call_gemini(geminiInput: GeminiInput): #telling geminiInput is of type of class GeminiInput
    print("Model:", geminiInput.model)     #geminiInput.model means extracting actual model from input object of class GeminiInput
    print("Prompt:", geminiInput.prompt)
    print(geminiInput.tokens, geminiInput.temperature)


input = GeminiInput(
    model="3.7-flash",
    prompt="What is OOPs?",
    tokens=100
)

input.model = "3.8-pro"

print(asdict(input))

print("\n")

call_gemini(input)

print("\n")

input.prompt = "What is Python?"

call_gemini(input)