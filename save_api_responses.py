import requests
import json
user_url="https://api.github.com/users/vibhutichaddha"
repos_url="https://api.github.com/users/vibhutichaddha/repos"
user_response=requests.get(user_url)
repos_response=requests.get(repos_url)
if user_response.status_code==200 & repos_response.status_code==200:
    user_data=user_response.json
    repo_data=repos_response.json
    with open("user_details.json", "w") as file:
        json.dump(user_response.json(), file, indent=4)
    with open("repositories.json", "w") as file:
        json.dump(repos_response.json(), file, indent=4)
    print("User details are stored in user_details.json")
    print("Repo details are stored in repositories.json")
else:
    print("Error in fetching API data")