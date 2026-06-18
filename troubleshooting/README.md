# Git 트러블슈팅 정리

## 목차

1. [잘못된 커밋 되돌리기]
2. [Merge Conflict 해결]
3. [실수로 삭제한 커밋 복구 (reflog)]
4. [reset vs revert 비교]
5. [줄바꿈(LF/CRLF) 이슈 해결]

---

## 1. [잘못된 커밋 되돌리기]

### 마지막 커밋 메시지만 수정 (아직 push 전)
```
git commit --amend -m "수정된 커밋 메시지"
```
* 예시
  ```
  <user>@MacBook-Pro:git_workflow <user>$ git log --oneline
  a1b2c3d (HEAD -> main) 오타가 있는 컷밋 메시지
  5c32ea3 이전 커밋

  <user>@MacBook-Pro:git_workflow <user>$ git commit --amend -m "feat: 오타 수정된 커밋 메시지"
  [main a2b3c4d] feat: 오타 수정된 커밋 메시지

  <user>@MacBook-Pro:git_workflow <user>$ git log --oneline
  a2b3c4d (HEAD -> main) feat: 오타 수정된 커밋 메시지
  5c32ea3 이전 커밋
  ```

### 스테이징한 파일 취소 (add 취소)
```
git restore --staged <<파일명>>
```
* 예시
  ```
  <user>@MacBook-Pro:git_workflow <user>$ git status
  Changes to be committed:
    (use "git restore --staged <file>..." to unstage)
          modified:   README.md
          modified:   config.py

  <user>@MacBook-Pro:git_workflow <user>$ git restore --staged config.py

  <user>@MacBook-Pro:git_workflow <user>$ git status
  Changes to be committed:
          modified:   README.md
  Changes not staged for commit:
          modified:   config.py
  ```

### 워킹 디렉토리 변경 사항 취소 (수정 내용 원복)
```
git restore <<파일명>>
```
* 주의: 취소 후 되돌릴 수 없다.

### 최근 N개 커밋 취소 (로컬에서만, push 전)
```
git reset HEAD~<<N>>         (변경 사항 유지, 스테이징 해제)
git reset --soft HEAD~<<N>>  (변경 사항 유지, 스테이징 상태 유지)
git reset --hard HEAD~<<N>>  (변경 사항 완전 삭제 - 주의!)
```
* 예시
  ```
  <user>@MacBook-Pro:git_workflow <user>$ git log --oneline
  c3d4e5f (HEAD -> main) feat: 잘못 추가한 기능
  b2c3d4e feat: 이전 정상 기능
  a1b2c3d 초기 커밋

  <user>@MacBook-Pro:git_workflow <user>$ git reset HEAD~1
  Unstaged changes after reset:
  M	feature.py

  <user>@MacBook-Pro:git_workflow <user>$ git log --oneline
  b2c3d4e (HEAD -> main) feat: 이전 정상 기능
  a1b2c3d 초기 커밋
  ```

---

## 2. [Merge Conflict 해결]

### Conflict 발생 상황
* 같은 파일의 같은 라인을 서로 다르게 수정한 후 merge 할 때 발생

### Conflict 발생 예시
```
<user>@MacBook-Pro:git_workflow <user>$ git merge feature/login
Auto-merging login.py
CONFLICT (content): Merge conflict in login.py
Automatic merge failed; fix conflicts and then commit the result.
```

### Conflict 파일 내용
```
<<<<<<< HEAD
def login(username, password):
    return auth_service.login(username, password)
=======
def login(user, pw):
    return db.authenticate(user, pw)
>>>>>>> feature/login
```
* `<<<<<<< HEAD` ~ `=======` : 현재 브랜치(HEAD)의 내용
* `=======` ~ `>>>>>>> feature/login` : 병합할 브랜치의 내용

### 해결 방법
* 1. 파일을 직접 편집하여 원하는 내용으로 수정
  ```
  def login(username, password):
      return auth_service.login(username, password)
  ```
* 2. 수정 완료 후 add → commit
  ```
  <user>@MacBook-Pro:git_workflow <user>$ git add login.py
  <user>@MacBook-Pro:git_workflow <user>$ git commit -m "merge: feature/login conflict 해결"
  [main f1e2d3c] merge: feature/login conflict 해결
  ```

### 현재 브랜치 또는 상대 브랜치 내용 전체 선택
```
git checkout --ours <<파일명>>    (현재 브랜치 내용으로 덮어씀)
git checkout --theirs <<파일명>> (병합할 브랜치 내용으로 덮어씀)
```

---

## 3. [실수로 삭제한 커밋 복구 (reflog)]

### git reflog 란?
* HEAD 가 이동한 모든 이력을 기록하는 명령어
* reset --hard 로 커밋을 삭제했더라도, reflog 를 통해 복구 가능하다.

### reflog 로 커밋 복구
* 예시 - reset --hard 로 커밋을 삭제한 상황
  ```
  <user>@MacBook-Pro:git_workflow <user>$ git log --oneline
  c3d4e5f (HEAD -> main) feat: 중요한 기능 추가
  b2c3d4e feat: 이전 기능
  a1b2c3d 초기 커밋

  <user>@MacBook-Pro:git_workflow <user>$ git reset --hard HEAD~1
  HEAD is now at b2c3d4e feat: 이전 기능

  <user>@MacBook-Pro:git_workflow <user>$ git log --oneline
  b2c3d4e (HEAD -> main) feat: 이전 기능
  a1b2c3d 초기 커밋
  ```
* reflog 로 삭제된 커밋 확인
  ```
  <user>@MacBook-Pro:git_workflow <user>$ git reflog
  b2c3d4e (HEAD -> main) HEAD@{0}: reset: moving to HEAD~1
  c3d4e5f HEAD@{1}: commit: feat: 중요한 기능 추가
  b2c3d4e HEAD@{2}: commit: feat: 이전 기능
  a1b2c3d HEAD@{3}: commit (initial): 초기 커밋
  ```
* 삭제된 커밋으로 복구
  ```
  <user>@MacBook-Pro:git_workflow <user>$ git reset --hard c3d4e5f
  HEAD is now at c3d4e5f feat: 중요한 기능 추가

  <user>@MacBook-Pro:git_workflow <user>$ git log --oneline
  c3d4e5f (HEAD -> main) feat: 중요한 기능 추가
  b2c3d4e feat: 이전 기능
  a1b2c3d 초기 커밋
  ```

---

## 4. [reset vs revert 비교]

| 항목 | git reset | git revert |
|------|-----------|------------|
| 동작 | 커밋 히스토리 자체를 제거 | 되돌리는 새 커밋을 생성 |
| 히스토리 | 변경됨 (해당 커밋 사라짐) | 유지됨 (revert 커밋 추가) |
| push 후 사용 | 위험 (강제 push 필요) | 안전 (일반 push 가능) |
| 사용 시점 | 로컬에서 아직 push 전 | 이미 공유된 커밋 되돌릴 때 |

### 예시 비교
* reset (로컬에서만 사용 권장)
  ```
  git reset --hard HEAD~1   (마지막 커밋 삭제)
  ```
* revert (push 된 커밋 되돌릴 때)
  ```
  git revert a1b2c3d        (해당 커밋을 되돌리는 새 커밋 생성)
  ```

---

## 5. [줄바꿈(LF/CRLF) 이슈 해결]

### 발생 원인
* Windows 는 줄바꿈으로 CRLF(`\r\n`), Mac/Linux 는 LF(`\n`)를 사용
* OS 가 다른 팀원과 협업 시 줄바꿈 문자 차이로 인해 불필요한 diff 가 발생

### 해결 방법 - .gitattributes 파일 설정 (권장)
* 레포 루트에 `.gitattributes` 파일 생성
  ```
  * text=auto
  *.py text eol=lf
  *.sh text eol=lf
  *.md text eol=lf
  *.bat text eol=crlf
  ```
* `text=auto` : Git 이 자동으로 줄바꿈 처리
* `eol=lf` : 체크아웃 시 LF 로 변환
* `eol=crlf` : 체크아웃 시 CRLF 로 변환

### git 전역 설정으로 해결
```
(Mac/Linux)
git config --global core.autocrlf input

(Windows)
git config --global core.autocrlf true
```
* `input` : 커밋 시 CRLF → LF 변환, 체크아웃 시 변환 없음
* `true` : 커밋 시 CRLF → LF 변환, 체크아웃 시 LF → CRLF 변환

* 레퍼런스
  * https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings
  * https://git-scm.com/docs/gitattributes
