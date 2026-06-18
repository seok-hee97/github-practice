# Pull Request (PR) 워크플로우 정리

## 목차

1. [Pull Request 란?]
2. [Fork 기반 PR 워크플로우]
3. [브랜치 기반 PR 워크플로우]
4. [코드 리뷰 및 머지]

---

## 1. [Pull Request 란?]

### Pull Request 란?
* 내가 작업한 브랜치의 변경 사항을 다른 브랜치(주로 main/develop)에 병합 요청하는 기능
* 코드 리뷰, 논의, CI/CD 연동 등을 거친 후 최종 merge 를 진행한다.
* 오픈소스 기여 또는 팀 협업에서 가장 핵심적인 협업 방식이다.

### PR 의 두 가지 방식
| 방식 | 사용 시점 |
|------|-----------|
| Fork 기반 PR | 외부 레포(오픈소스 등)에 기여할 때 |
| 브랜치 기반 PR | 같은 레포 내에서 팀원과 협업할 때 |

---

## 2. [Fork 기반 PR 워크플로우]

### 전체 흐름
```
원본 레포 fork → 내 계정으로 clone → 브랜치 생성 → 작업 → push → PR 생성
```

### 단계별 설명

* fork
  * GitHub 웹에서 원본 레포의 Fork 버튼 클릭 → 내 계정에 복사본 생성

* 내 fork 레포를 로컬에 clone
  ```
  git clone https://github.com/<<내 계정>>/<<레포명>>.git
  cd <<레포명>>
  ```

* 원본 레포를 upstream 으로 등록 (최신 변경 사항 동기화를 위해)
  ```
  git remote add upstream https://github.com/<<원본 계정>>/<<레포명>>.git
  git remote -v
  ```
  * 예시
    ```
    <user>@MacBook-Pro:project <user>$ git remote -v
    origin    https://github.com/<user>/project.git (fetch)
    origin    https://github.com/<user>/project.git (push)
    upstream  https://github.com/original-owner/project.git (fetch)
    upstream  https://github.com/original-owner/project.git (push)
    ```

* 작업 브랜치 생성 후 작업
  ```
  git checkout -b feature/my-feature
  (코드 작업)
  git add .
  git commit -m "feat: 기능 추가"
  git push origin feature/my-feature
  ```

* PR 생성
  * GitHub 웹에서 내 fork 레포 접속
  * Compare & pull request 버튼 클릭
  * base: 원본 레포의 main (또는 develop), compare: 내 feature 브랜치 선택
  * 제목, 설명 작성 후 Create pull request 클릭

* upstream 최신 변경 사항 동기화 (PR 머지 전 충돌 방지)
  ```
  git fetch upstream
  git checkout main
  git merge upstream/main
  git push origin main
  ```

---

## 3. [브랜치 기반 PR 워크플로우]

### 전체 흐름
```
브랜치 생성 → 작업 → push → PR 생성 → 코드 리뷰 → merge → 브랜치 삭제
```

### 단계별 설명

* 최신 main 브랜치에서 작업 브랜치 생성
  ```
  git checkout main
  git pull origin main
  git checkout -b feature/login
  ```
  * 예시
    ```
    <user>@MacBook-Pro:git_workflow <user>$ git checkout main
    Switched to branch 'main'
    <user>@MacBook-Pro:git_workflow <user>$ git pull origin main
    Already up to date.
    <user>@MacBook-Pro:git_workflow <user>$ git checkout -b feature/login
    Switched to a new branch 'feature/login'
    ```

* 작업 후 커밋 및 push
  ```
  git add .
  git commit -m "feat(auth): 로그인 기능 추가"
  git push origin feature/login
  ```
  * 예시
    ```
    <user>@MacBook-Pro:git_workflow <user>$ git push origin feature/login
    Enumerating objects: 5, done.
    Counting objects: 100% (5/5), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 312 bytes | 312.00 KiB/s, done.
    Total 3 (delta 1), reused 0 (delta 0)
    To https://github.com/<user>/git_workflow.git
     * [new branch]      feature/login -> feature/login
    ```

* GitHub 웹에서 PR 생성
  * 레포 접속 → Pull requests 탭 → New pull request 클릭
  * base: main, compare: feature/login 선택
  * 제목, 설명 작성 (어떤 변경인지, 테스트 방법 등)
  * Reviewers, Labels, Assignees 지정 후 Create pull request 클릭

---

## 4. [코드 리뷰 및 머지]

### 코드 리뷰
* PR 화면에서 Files changed 탭으로 변경된 코드 확인
* 라인 단위로 코멘트 작성 가능
* 리뷰어는 아래 세 가지 중 하나로 리뷰 완료
  * Comment : 단순 의견 전달
  * Approve : 승인 (merge 가능)
  * Request changes : 수정 요청

### 리뷰 반영 후 재push
```
(리뷰 내용 반영 후)
git add .
git commit -m "fix: 리뷰 반영 - 입력값 유효성 검사 추가"
git push origin feature/login
```

### 머지 방법
| 방법 | 설명 | 특징 |
|------|------|------|
| Merge commit | 브랜치 이력을 그대로 유지하며 merge | 히스토리 보존 |
| Squash and merge | 브랜치의 커밋을 하나로 합쳐 merge | 깔끔한 main 히스토리 |
| Rebase and merge | 커밋을 main 위에 재배치 후 merge | 선형 히스토리 유지 |

### 머지 후 브랜치 삭제
* GitHub 웹 PR 화면에서 Delete branch 클릭
* 또는 로컬에서 삭제
  ```
  git checkout main
  git pull origin main
  git branch -d feature/login
  ```
  * 예시
    ```
    <user>@MacBook-Pro:git_workflow <user>$ git branch -d feature/login
    Deleted branch feature/login (was a1b2c3d).
    ```

* 레퍼런스
  * https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
  * https://docs.github.com/en/get-started/quickstart/contributing-to-projects
