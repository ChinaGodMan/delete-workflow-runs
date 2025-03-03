import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAMES = os.getenv("REPO_NAME", "").split(",")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


# 获取所有 Actions 运行记录
def get_all_workflow_runs(repo_owner, repo_name):
    base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs"
    runs = []
    page = 1
    while True:
        response = requests.get(f"{base_url}?page={page}", headers=headers)
        if response.status_code != 200:
            print(f"Error fetching runs for {repo_name}: {response.status_code}")
            break
        data = response.json()
        runs.extend(data.get("workflow_runs", []))
        if "next" not in response.links:
            break
        page += 1
    return runs


# 删除指定的运行记录
def delete_workflow_run(repo_owner, repo_name, run_id):
    delete_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs/{run_id}"
    response = requests.delete(delete_url, headers=headers)
    if response.status_code == 204:
        print(f"Successfully deleted run {run_id} from {repo_name}")
    else:
        print(f"Failed to delete run {run_id} from {repo_name}: {response.status_code}, {response.text}")


# 主函数，获取并删除所有运行记录
def main():
    if not REPO_NAMES:
        print("No repositories specified.")
        return

    for repo_name in REPO_NAMES:
        repo_name = repo_name.strip()
        print(f"Processing repository: {repo_name}")
        runs = get_all_workflow_runs(REPO_OWNER, repo_name)
        if not runs:
            print(f"No workflow runs found for {repo_name}.")
            continue
        print(f"Found {len(runs)} workflow runs in {repo_name}. Deleting them now...")
        for run in runs:
            delete_workflow_run(REPO_OWNER, repo_name, run["id"])


if __name__ == "__main__":
    main()
