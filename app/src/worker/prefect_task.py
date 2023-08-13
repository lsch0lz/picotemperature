from typing import Tuple, Any

import httpx

from prefect import task, flow


@task(retries=2)
def get_repo(repo_owner: str, repo_name: str) -> str:
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    api_response = httpx.get(url)
    api_response.raise_for_status()
    repo_info = api_response.json()
    return repo_info


@task
def get_contributors(repo_info: str) -> str:
    contributors_url = repo_info["contributors_url"]
    api_response = httpx.get(contributors_url)
    api_response.raise_for_status()
    contributors = api_response.json()
    return contributors


@flow(name="GitHub Contributors", log_prints=True)
def repo_info(repo_owner: str = "PrefectHQ", repo_name: str = "prefect") -> tuple[Any | None, Any | None]:
    repo_info = get_repo(repo_owner, repo_name)
    print(f"Stars 🌠 : {repo_info['stargazers_count']}")

    contributors = get_contributors(repo_info)
    print(f"Number of contributors 👷: {len(contributors)}")

    return repo_info, contributors
