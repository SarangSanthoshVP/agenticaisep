from pydantic import BaseModel, EmailStr, ValidationError, PositiveInt

class GeminiResponse(BaseModel):
    status: str
    code: str
    tokens: PositiveInt
    language: str
    isDone: bool = True
    userEmail: EmailStr

geminiResponse1 = GeminiResponse(status="success", code="hello", tokens="12321", language="python", userEmail="abhinav@hello.com")
print(geminiResponse1)

try:
    geminiResponse1 = GeminiResponse(status="success", code="hello", tokens="12321", userEmail="abhinav@newtonschool.com")
    print(geminiResponse1)
except ValidationError as e:
    print("ValidationError:", e)

try:
    geminiResponse1 = GeminiResponse(status="success", code="hello", tokens="12321", language="python", userEmail="werawtsdgfsderwt4rgf")
    print(geminiResponse1)
except ValidationError as e:
    print("ValidationError:", e)

try:
    geminiResponse1 = GeminiResponse(status="success", code="hello", tokens=-21345, language="python", userEmail="abhinav@hello.com")
    print(geminiResponse1)
except ValidationError as e:
    print("ValidationError:", e)