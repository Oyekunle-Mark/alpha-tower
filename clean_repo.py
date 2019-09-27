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
