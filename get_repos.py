from requests import get
from parameters import build_parameters

GITHUB_API_URL = "https://api.github.com/search/repositories"


def get_repos_with_most_stars(languages, sort="stars", order="desc", stars=50000):
    """Fetches the data from the GitHub API

    Arguments:
        languages {list} -- the list of languages 

    Keyword Arguments:
        sort {str} -- the sort condition (default: {"stars"})
        order {str} -- the order pattern (default: {"desc"})
        stars {int} -- the minimum number of stars (default: {50000})

    Raises:
        RuntimeError: Error that might occur while fetching data from the API

    Returns:
        {tuple} -- the repos and number of repos
    """

    parameters = build_parameters(languages, sort, order, stars)

    response = get(GITHUB_API_URL, params=parameters)

    if response.status_code != 200:
        raise RuntimeError(
            f"An error occured while fetching the data. The status code was {response.status_code}")

    repos = response.json()["items"]
    repo_count = response.json()["total_count"]

    return repos, repo_count
