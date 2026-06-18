# GitHub Actions 정리

## 목차

1. [GitHub Actions 란?]
2. [워크플로우 파일 구조]
3. [기본 예시 - Push 시 자동 테스트]
4. [주요 트리거(이벤트) 종류]
5. [자주 사용하는 Actions]

---

## 1. [GitHub Actions 란?]

### GitHub Actions 란?
* GitHub 에서 제공하는 CI/CD(지속적 통합/배포) 자동화 플랫폼
* 코드 push, PR 생성, 일정 등 다양한 이벤트를 트리거로 자동화 워크플로우를 실행한다.
* `.github/workflows/` 디렉토리에 YAML 파일로 워크플로우를 정의한다.
* Public 레포는 무료, Private 레포는 월 2,000분 무료 제공 (초과 시 과금)

### 주요 개념
| 용어 | 설명 |
|------|------|
| Workflow | 자동화 작업의 전체 흐름 (.yml 파일 하나) |
| Event(trigger) | 워크플로우를 실행시키는 조건 (push, PR 등) |
| Job | 워크플로우 내의 작업 단위 (병렬 실행 가능) |
| Step | Job 내의 개별 실행 단계 |
| Action | 재사용 가능한 Step 모음 (GitHub Marketplace 제공) |
| Runner | 워크플로우가 실행되는 서버 환경 (ubuntu, macos, windows) |

---

## 2. [워크플로우 파일 구조]

### 디렉토리 구조
```
레포지토리/
└── .github/
    └── workflows/
        ├── ci.yml       (CI 워크플로우)
        └── deploy.yml   (배포 워크플로우)
```

### 기본 YAML 구조
```yaml
name: 워크플로우 이름

on:               # 트리거(이벤트) 정의
  push:
    branches: [ main ]

jobs:             # 실행할 Job 정의
  job-name:
    runs-on: ubuntu-latest   # Runner 환경

    steps:        # Job 내의 단계
      - name: 단계 이름
        uses: actions/checkout@v4   # 외부 Action 사용

      - name: 명령어 실행
        run: echo "Hello, GitHub Actions!"
```

---

## 3. [기본 예시 - Push 시 자동 테스트]

### Python 프로젝트 CI 예시
* `.github/workflows/ci.yml` 파일 생성
  ```yaml
  name: CI

  on:
    push:
      branches: [ main, develop ]
    pull_request:
      branches: [ main ]

  jobs:
    test:
      runs-on: ubuntu-latest

      steps:
        - name: 코드 체크아웃
          uses: actions/checkout@v4

        - name: Python 설치
          uses: actions/setup-python@v5
          with:
            python-version: '3.11'

        - name: 의존성 설치
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt

        - name: 테스트 실행
          run: python -m pytest tests/
  ```

### 실행 결과 확인
* GitHub 웹에서 레포 → Actions 탭 → 워크플로우 목록에서 실행 이력 및 로그 확인
* PR 화면에서 checks 항목으로 통과 여부 확인

---

## 4. [주요 트리거(이벤트) 종류]

### push
```yaml
on:
  push:
    branches: [ main ]         # main 브랜치에 push 될 때
    paths:
      - 'src/**'               # src 디렉토리 변경 시에만 실행
```

### pull_request
```yaml
on:
  pull_request:
    branches: [ main ]         # main 으로 향하는 PR 생성/업데이트 시
    types: [ opened, synchronize, reopened ]
```

### schedule (정기 실행)
```yaml
on:
  schedule:
    - cron: '0 9 * * 1-5'     # 평일 오전 9시 (UTC 기준)
```

### workflow_dispatch (수동 실행)
```yaml
on:
  workflow_dispatch:           # GitHub 웹에서 수동으로 실행 버튼 클릭 시
    inputs:
      environment:
        description: '배포 환경'
        required: true
        default: 'staging'
```

---

## 5. [자주 사용하는 Actions]

### 코드 체크아웃
```yaml
- uses: actions/checkout@v4
```

### 언어 런타임 설치
```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.11'

- uses: actions/setup-node@v4
  with:
    node-version: '20'

- uses: actions/setup-java@v4
  with:
    java-version: '17'
    distribution: 'temurin'
```

### 캐시 활용 (의존성 설치 속도 향상)
```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

### Slack 알림
```yaml
- name: Slack 알림
  uses: slackapi/slack-github-action@v1
  with:
    payload: |
      {
        "text": "배포 완료: ${{ github.repository }}"
      }
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
```

### 환경 변수 및 시크릿 사용
* GitHub 웹에서 레포 → Settings → Secrets and variables → Actions → New repository secret 으로 등록
* 워크플로우에서 `${{ secrets.SECRET_NAME }}` 형식으로 참조
  ```yaml
  - name: 배포
    run: ./deploy.sh
    env:
      API_KEY: ${{ secrets.API_KEY }}
      DB_URL: ${{ secrets.DATABASE_URL }}
  ```

* 레퍼런스
  * https://docs.github.com/en/actions
  * https://github.com/marketplace?type=actions
  * https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows
