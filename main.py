import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"


def create_query(languages, stars):
    query = f"stars:>{stars} "

    for language in languages:
        query += f"language:{language} "

    return query

def build_parameters(languages, sort, order, stars):
    query = create_query(languages, stars);

    return {"q": query, "sort": sort, "order": order}
    

def get_repos_with_most_stars(languages, sort="stars", order="desc", stars=100000):
    parameters = build_parameters(languages, sort, order, stars)

    response = requests.get(GITHUB_API_URL, params=parameters)

    repos = response.json()["items"]
    return repos


if __name__ == "__main__":
    languages = ["javascript", "python", "go"]

    print(get_repos_with_most_stars(languages))
