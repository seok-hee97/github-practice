# Github-practice

## 문서 목차

| 문서 | 설명 |
|------|------|
| [git_workflow/README.md](git_workflow/README.md) | Git Flow, 브랜치 전략, 주요 명령어 (branch, checkout, merge, rebase, cherry-pick 등), Conventional Commits |
| [git_workflow/pull_request.md](git_workflow/pull_request.md) | Pull Request 워크플로우 (Fork 기반 / 브랜치 기반, 코드 리뷰, 머지 방법) |
| [troubleshooting/README.md](troubleshooting/README.md) | 트러블슈팅 (커밋 되돌리기, Merge Conflict 해결, reflog 복구, reset vs revert, LF/CRLF) |
| [github_features/actions.md](github_features/actions.md) | GitHub Actions CI/CD 입문 (워크플로우 구조, 트리거, 자주 쓰는 Actions) |

---


- 깃, 깃허브 한번에 이해시켜드리고 포트폴리오 올리는 법 1탄 o

[https://www.youtube.com/watch?v=lelVripbt2M](https://www.youtube.com/watch?v=lelVripbt2M)

- Git 명령어 총정리집(by 코딩알려주는 누나) 2탄 o

[https://hackmd.io/@oW_dDxdsRoSpl0M64Tfg2g/ByfwpNJ-K](https://hackmd.io/@oW_dDxdsRoSpl0M64Tfg2g/ByfwpNJ-K)

**Git and GitHub for Beginners - Crash Course o**

**[https://www.youtube.com/watch?v=RGOj5yH7evk](https://www.youtube.com/watch?v=RGOj5yH7evk)**

**[Git-command.md](http://Git-command.md)**

**[https://gist.github.com/gwenf/19e5748a5391929e8e938a22c8a4b3f2](https://gist.github.com/gwenf/19e5748a5391929e8e938a22c8a4b3f2)**

- repo -> repository
- clone -> bring a repo down from the internet (remote repository like Github) to your local machine

(깃 레포지터리 폴더 가져오기)

- add -> track your files and changes with Git
- commit -> save your changes into Git
- push -> push your changes to your remote repo on Github (or another website)
- pull -> pull changes down from the remote repo to your local machine
- status -> check to see which files are being tracked or need to be commited
- init -> use this command inside of your project to turn it into a Git repository and start using Git with that codebase
- **Powerful VSCode Tips And Tricks For Python Development And Design**

[Powerful VSCode Tips And Tricks For Python Development And Design](https://www.youtube.com/watch?v=fj2tuTIcUys&t=130s)



git clone 사용안하고 깃헙 레포에 올리는 방법
```
git init

git remote add origin <GitHub 레포지토리 주소>

git add .

git commit -m "init commit message"

git push -u origin main
```


Github token 발급 필요
(github login -> settings -> Developer Settings -> Personal access tokens -> Tokens(classic) -> need repo auth check!! -> get token!!)
- github-repo-codeline.py : 깃헙 레포에 있는 코드라인 수 세는 코드
- github-repos-codeline.py : 깃헙에 있는 코드라인 수 세는 코드

#### etc



- **Mac m1에 우분투설치**

**[https://webnautes.tistory.com/1580**](https://webnautes.tistory.com/1580**)

$ sudo apt update

$ sudo apt install ubuntu-desktop

[https://www.qt.io/offline-installers](https://www.qt.io/offline-installers)


[Github 프로필 리드미 작서하는법 및 꾸미기](https://junia3.github.io/blog/githubreadme)





