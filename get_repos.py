from requests import get
from parameters import build_parameters

GITHUB_API_URL = "https://api.github.com/search/repositories"


def get_repos_with_most_stars(languages, sort="stars", order="desc", stars=50000):
    parameters = build_parameters(languages, sort, order, stars)

    response = get(GITHUB_API_URL, params=parameters)

    repos = response.json()["items"]
    repo_count = response.json()["total_count"]

    return repos, repo_count
