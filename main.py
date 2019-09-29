"""Pulls in the main files and executes them here
Prints the output of the executions
"""

from pprint import pprint as pp
from get_repos import get_repos_with_most_stars
from clean_repo import get_useful_fields


if __name__ == "__main__":
    languages = ["javascript", "python", "go"]

    repos, repo_count = get_repos_with_most_stars(languages)
    cleaned_repos = get_useful_fields(repos, repo_count)

    pp(cleaned_repos)
