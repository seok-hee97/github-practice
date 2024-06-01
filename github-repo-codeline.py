import requests

def get_repo_line_count(username, repository, token):
    headers = {'Authorization': 'token ' + token}
    url = f'https://api.github.com/repos/{username}/{repository}'
    repo_info = requests.get(url, headers=headers).json()

    commits_url = repo_info['commits_url'].split("{")[0]  # commits_url에서 {/sha} 부분 제거
    commits = requests.get(commits_url, headers=headers).json()

    total_lines = 0
    for commit in commits:
        commit_url = commit['url']
        commit_details = requests.get(commit_url, headers=headers).json()
        files = commit_details['files']

        for file in files:
            total_lines += file['additions'] + file['deletions']

    return total_lines

# 사용자의 GitHub 아이디, 레포지토리 이름, 개발자 토큰 설정
username = '사용자_아이디'
repository = '레포지토리_이름'
token = '개발자_토큰'

total_lines = get_repo_line_count(username, repository, token)
print(f'Total lines of code in {username}/{repository}: {total_lines}')
