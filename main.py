import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"




def build_parameters(languages, sort="stars", order="desc", stars=100000):
    return {"q": f"stars:>{stars}", "sort": sort, "order": order}
    

def get_repos_with_most_stars():

    response = requests.get(GITHUB_API_URL, params=parameters)

    repos = response.json()["items"]
    return repos


if __name__ == "__main__":

    print(get_repos_with_most_stars())
