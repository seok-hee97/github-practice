import requests


def get_repo_line_count(username, token):
    headers = {'Authorization': 'token ' + token}
    url = f'https://api.github.com/users/{username}/repos'
    repos = requests.get(url, headers=headers).json()

    total_lines = 0
    for repo in repos:
        repo_name = repo['name']
        commits_url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
        commits = requests.get(commits_url, headers=headers).json()

        for commit in commits:
            commit_url = commit['url']
            commit_details = requests.get(commit_url, headers=headers).json()
            files = commit_details['files']

            for file in files:
                total_lines += file['additions'] + file['deletions']

    return total_lines

username = 'username'
token = 'token'

total_lines = get_repo_line_count(username, token)
print(f'Total lines of code in all repositories: {total_lines}')
