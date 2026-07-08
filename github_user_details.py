import requests
username=input("Enter Github username:")
url="https://api.github.com/users/vibhutichaddha"
responses=requests.get(url)
if responses.status_code==200:
    data=responses.json()
    print("Name:",data["name"])
    print("Username:",data["login"])
    print("Bio:",data["bio"])
    print("Followers:",data["followers"])
    print("Following:",data["following"])
    print("Public Repositories:",data["public_repos"])
    print("Account Creation Date:",data["created_at"])
else:
    print("API request failed")