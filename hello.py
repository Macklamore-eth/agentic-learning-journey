import requests
import certifi


req = requests.get("https://catfact.ninja/fact", verify = False)


                   
if req.status_code == 200:
    print("Is successful")
else:
    print("Failed")


print("Cat Fact", req.json())



