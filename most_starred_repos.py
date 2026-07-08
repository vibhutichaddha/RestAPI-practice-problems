import requests
url="https://api.github.com/users/octocat/repos"
responses=requests.get(url)
if responses.status_code==200:
    data=responses.json()
    sorted_repos=sorted(data,key=lambda repo: repo["stargazers_count"],reverse=True)
    top_5=sorted_repos[::5]
    print("\nTop 5 starred repositiories\n")
    for repo in top_5:
        print("Repo Name:",repo["name"])
        print("Programming language:",repo["language"])
        print("Stars:",repo["stargazers_count"])
else:
    print("Error:",responses.status_code)