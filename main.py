import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"


def get_repos_with_most_stars():
    parameters = {"q": "stars:>200000", "sort": "stars", "order": "desc"}

    response = requests.get(GITHUB_API_URL, params=parameters)

    return response.json()


print(get_repos_with_most_stars())
