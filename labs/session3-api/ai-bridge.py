from pydantic import BaseModel, ValidationError
import requests
import json

class UserInsight(BaseModel):
    user_name: str
    sentiment_score: int
    is_flagged_for_review: bool

print("--- MODEL INITIALIZED ---")
print("Pydantic Schema enforces: user_name (str), sentiment_score (int), is_flagged_for_review (bool)\n")

def analyze_user_data_via_api():
    api_url = "https://jsonplaceholder.typicode.com/posts"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-mock-api-key-12345"
    }
    
    payload = {
        "model": "gpt-4-turbo",
        "messages": [
            {"role": "system", "content": "You analyze user sentiment."},
            {"role": "user", "content": "Analyze the sentiment for user 'Alice'."}
        ]
    }
    
    print("--- TRANSMITTING HTTP POST REQUEST ---")
    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=5)
        
        response.raise_for_status() 
        
        print(f"Network Success! Status Code: {response.status_code}\n")
        with open("raw_llm_output.json", "w") as file:
            json.dump(response.json(), file, indent=4)
        
        mock_llm_output = {
            "user_name": "Alice",
            "sentiment_score": "88",       # Notice this is a STRING, but Pydantic expects an INT
            "is_flagged_for_review": "false" # Notice this is a STRING, but Pydantic expects a BOOL
        }
        
        return mock_llm_output


        
    except requests.exceptions.RequestException as e:
        print(f"[NETWORK CRASH] Failed to reach API: {e}")
        return None

if __name__ == "__main__":
    
    # Step A: Get the raw data from the web
    raw_api_data = analyze_user_data_via_api()
    
    if raw_api_data:
        print("--- VALIDATING RAW LLM OUTPUT ---")
        print(f"Raw Data received: {raw_api_data}\n")
        
        try:
            # Step B: Pass the raw dictionary into our strict Pydantic model
            # This is where the magic happens (Auto-casting strings to ints/bools)
            validated_insight = UserInsight(**raw_api_data)
            
            print("--- VALIDATION SUCCESSFUL! ---")
            print(f"Secured Object: {validated_insight}")
            
            # Now your IDE knows exactly what data types these are!
            print(f"Cleaned Score (Now a true Integer): {validated_insight.sentiment_score + 10}")
            
        except ValidationError as e:
            # Step C: Fail Fast if the LLM completely hallucinated the structure
            print(f"[VALIDATION CRASH] The LLM failed to match our schema:\n{e.json()}")