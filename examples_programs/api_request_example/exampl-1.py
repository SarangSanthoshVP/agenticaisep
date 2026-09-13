import json
import requests

api_endpoint = "https://my.newtonschool.co/api/v1/instructor/course/h/88sqmk67n6nl/overview/"
headers = {
    'accept': 'application/json, text/plain, */*',
    'authorization': 'Bearer <token>'
}
#headers is used for authentication and authorization. It contains the necessary credentials or tokens that allow the client to access protected resources on the server. In this case, the 'authorization' header includes a Bearer token that grants access to the API endpoint.

# GET
try:
    response = requests.get(api_endpoint, headers=headers)

    # response.raise_for_status() # not successfull
    data = response.json()

    with open("api_response.json", "w") as file:
        json.dump(data, file)
except Exception as e:
    print("Error:", e)