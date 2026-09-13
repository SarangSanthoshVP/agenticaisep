import json
import requests

api_endpoint = "https://pokeapi.co/api/v2/pokemon/ditto"
headers = {
    'accept': 'application/json, text/plain, */*'
}
#  
# GET
try:
    response = requests.get(api_endpoint, headers=headers)

    # response.raise_for_status() # not successfull #raise_for_status() is a method in the requests library that raises an HTTPError if the HTTP request returned an unsuccessful status code (4xx or 5xx). It helps in error handling by allowing you to catch exceptions for failed requests. In this case, it is commented out, so the code will not raise an exception for unsuccessful responses.  
    data = response.json()
 
    with open("pokemon.json", "w") as file:
        json.dump(data, file)                #not using json.dump(asdict(data), file) because data is already a dictionary, so we can directly dump it to the file without converting it to a dictionary again. Using asdict() would be unnecessary and could lead to errors if data is not a dataclass instance.
except Exception as e:
    print("Error:", e)