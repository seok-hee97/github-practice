# Github-practice

## 문서 목차

| 문서 | 설명 |
|------|------|
| [git_workflow/README.md](git_workflow/README.md) | Git Flow, 브랜치 전략, 주요 명령어 (branch, checkout, merge, rebase, cherry-pick 등), Conventional Commits |
| [git_workflow/pull_request.md](git_workflow/pull_request.md) | Pull Request 워크플로우 (Fork 기반 / 브랜치 기반, 코드 리뷰, 머지 방법) |
| [troubleshooting/README.md](troubleshooting/README.md) | 트러블슈팅 (커밋 되돌리기, Merge Conflict 해결, reflog 복구, reset vs revert, LF/CRLF) |
| [github_features/actions.md](github_features/actions.md) | GitHub Actions CI/CD 입문 (워크플로우 구조, 트리거, 자주 쓰는 Actions) |

---

## 참고 자료

- 깃, 깃허브 한번에 이해시켜드리고 포트폴리오 올리는 법 1탄

[https://www.youtube.com/watch?v=lelVripbt2M](https://www.youtube.com/watch?v=lelVripbt2M)

- Git 명령어 총정리집(by 코딩알려주는 누나) 2탄

[https://hackmd.io/@oW_dDxdsRoSpl0M64Tfg2g/ByfwpNJ-K](https://hackmd.io/@oW_dDxdsRoSpl0M64Tfg2g/ByfwpNJ-K)

- Git and GitHub for Beginners - Crash Course

[https://www.youtube.com/watch?v=RGOj5yH7evk](https://www.youtube.com/watch?v=RGOj5yH7evk)

- Git 명령어 모음 (Cheat Sheet)

[https://gist.github.com/gwenf/19e5748a5391929e8e938a22c8a4b3f2](https://gist.github.com/gwenf/19e5748a5391929e8e938a22c8a4b3f2)

- Powerful VSCode Tips And Tricks For Python Development And Design

[https://www.youtube.com/watch?v=fj2tuTIcUys&t=130s](https://www.youtube.com/watch?v=fj2tuTIcUys&t=130s)

---

## 기본 개념

- repo -> repository (저장소)
- clone -> bring a repo down from the internet (깃 레포지터리 폴더 가져오기)
- add -> track your files and changes with Git (변경 파일 추적 등록)
- commit -> save your changes into Git (변경 사항 저장)
- push -> push your changes to your remote repo on Github (로컬 변경 사항을 원격 레포에 업로드)
- pull -> pull changes down from the remote repo to your local machine (원격 레포의 변경 사항을 로컬에 반영)
- status -> check to see which files are being tracked or need to be commited (추적 중인 파일 및 변경 사항 확인)
- init -> use this command inside of your project to turn it into a Git repository (프로젝트를 Git 레포로 초기화)

---

## git clone 사용 없이 깃헙 레포에 올리는 방법

```
git init

git remote add origin <GitHub 레포지토리 주소>

git add .

git commit -m "init commit message"

git push -u origin main
```

---

## Github Token 발급

- github login → settings → Developer Settings → Personal access tokens → Tokens(classic)
- repo 권한 체크 후 토큰 발급

- github-repo-codeline.py : 깃헙 레포에 있는 코드라인 수 세는 코드
- github-repos-codeline.py : 깃헙에 있는 코드라인 수 세는 코드
