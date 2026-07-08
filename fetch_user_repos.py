import requests
url="https://api.github.com/users/vibhutichaddha/repos"
responses=requests.get(url)
if responses.status_code==200:
    data=responses.json()
    for repo in data:
        print("Repo Name:",repo["name"])
        print("Description:",repo["description"])
        print("Programming language:",repo["language"])
        print("Stars:",repo["stargazers_count"])
        print("Forks:",repo["forks_count"])
else:
    print("User not found")