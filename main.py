from requests import get

GITHUB_API_URL = "https://api.github.com/search/repositories"


def create_query(languages, stars):
    query = f"stars:>{stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def build_parameters(languages, sort, order, stars):
    query = create_query(languages, stars)

    return {"q": query, "sort": sort, "order": order}


def get_repos_with_most_stars(languages, sort="stars", order="desc", stars=50000):
    parameters = build_parameters(languages, sort, order, stars)

    response = get(GITHUB_API_URL, params=parameters)

    repos = response.json()["items"]
    repo_count = response.json()["total_count"]

    return repos, repo_count


def get_useful_fields(repos, repo_count):
    filtered_repos = []

    for repo in repos:
        filtered_repos.append({
            "name": repo["name"],
            "language": repo["language"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "issues": repo["open_issues_count"]
        })

    return {
        "Number of repositories": repo_count,
        "Repositories": filtered_repos
    }


if __name__ == "__main__":
    languages = ["javascript", "python", "go"]

    repos, repo_count = get_repos_with_most_stars(languages)
    cleaned_repos = get_useful_fields(repos, repo_count)

    print(cleaned_repos)
