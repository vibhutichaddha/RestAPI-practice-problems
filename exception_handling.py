import requests 
url=f"https://pi.github.com/users/vibhutichaddha"
try:
    response=requests.get(url,timeout=5)
    if response.status_code==404:
        print("Error: Github user not found!")
    elif response.status_code==200:
        try:
            user_data=response.json()
            print("Name:",user_data["name"])
            print("Username:",user_data["login"])
            print("Bio:",user_data["bio"])
        except requests.exceptions.JSONDecodeError:
            print("Error: Invalid JSON response recieved!")
    else:
        print("Error: API request failed!")
except requests.exceptions.ConnectionError:
    print("Error: internet connection failed!")
except requests.exceptions.Timeout:
    print("Error: Request timed out!")
except requests.exceptions.RequestException:
    print("Error: Something went wrong with the API request!")