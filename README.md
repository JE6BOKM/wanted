# 원티드랩

- 과제 출제 기업 정보
  - 기업명 : 원티드랩
  - [원티드](https://www.wanted.co.kr/)
  - [wanted 채용공고 링크](https://www.wanted.co.kr/company/79)

## 💁‍♀️ Members

| 이름   | github                                    | 담당 기능                  |
| ------ | ----------------------------------------- | -------------------------- |
| 신재민 | [shinjam](https://github.com/shinjam)     | Test코드 적용, 배포        |
| 신우주 | [shinwooju](https://github.com/shinwooju) | 회사 이름으로 검색         |
| 최혜림 | [rimi0108](https://github.com/rimi0108)   | 데이터변환 및 업로드       |
| 강성묵 | [miranaky](https://github.com/miranaky)   | 전체 총괄, 회사명 자동완성 |
| 김민규 | [SkyStar-K](https://github.com/SkyStar-K) | 회사 생성                  |

## ⭐ 과제 내용

---

### [필수 포함 사항]

- READ.ME 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

---

### [개발 요구사항]

✔️ **데이터**

---

- 회사 정보
  - 회사 이름 (다국어 지원 가능)
- 회사 정보 예제
  - 회사 이름 (원티드랩 / Wantedlab)
- 데이터 셋은 원티드에서 제공
- 데이터셋 예제

      -   원티드랩 회사는 한국어, 영어 회사명을 가지고 있습니다. (모든 회사가 모든 언어의 회사명을 가지고 있지는 않습니다.)

  ✔️ **REST API 기능**

---

- 회사명 자동완성
  - 회사명의 일부만 들어가도 검색이 되어야 합니다.
- 회사 이름으로 회사 검색
- 새로운 회사 추가

**✔️ 개발 조건**

---

- 제공되는 test case를 통과할 수 있도록 개발해야 합니다.
  [test_app.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d2517b3-b80b-4a1b-82c4-9bc6f2a0d5ae/test_app.py)
- ORM 사용해야 합니다.
- 결과는 JSON 형식이어야 합니다.
- database는 RDB를 사용해야 합니다.
- database table 갯수는 제한없습니다.
- 필요한 조건이 있다면 추가하셔도 좋습니다.
- Docker로 개발하면 가산점이 있습니다.

---

---

## 사용 기술 및 tools

> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=PostgreSQL&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

---

---

## 🏄‍♀️ 모델링

![image](https://user-images.githubusercontent.com/79964569/140952581-2c215f7f-a93d-49f7-8bf6-c438ffa6536a.png)

---

---

## API

[링크-postman document](https://documenter.getpostman.com/view/13670333/UVC5F7t1)

---

---

## 구현 기능

</br>

### 회사명 자동완성

- 회사명의 일부만 들어가도 검색이 되어야 합니다.
- header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다. - 구현 - header의 Key값에 x-wanted-language, Value값에 'ko', 'en','ja','tw' 등을 이용하여 필터링 해야합니다.

  - 구현
    - 회사명의 일부 단어가 들어오면 그 단어를 포함하는 이름을 모두 검색합니다.
    - header에서 요청한 언어값으로만 검색합니다. 다른 언어값은 검색 하지 않습니다.
    - 언어 값과 회사명을 같이 갖도록 해서 두가지가 일치한 값만 보여줍니다.
  - 요청
    ```bash
    curl --location --request GET 'http://127.0.0.1:8000/search?query=라인' --header 'x-wanted-language: ko'
    ```
  - 결과
    `json [ { "company_name": "라인 웍스" }, { "company_name": "라인 프래시" } ] `
    ` `
    </br>

### 회사이름으로 회사검색

- 구현
  ```
  {
      "company_name": "infobank",
      "tags": [
          "tag_1",
          "tag_2"
      ]
  }
  ```
- header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.

  - 구현
    - header의 Key값에 x-wanted-language, Value값에 'ko', 'en','ja','tw' 등을 이용하여 필터링 해야합니다.
    ```
    {
        "company_name": "인포뱅크",
        "tags": [
            "태그_1",
            "태그_2"
        ]
    },
    {
        "company_name": "infobank",
        "tags": [
            "tag_1",
            "tag_2"
        ]
    }
    ```

- 검색된 회사가 없는경우 404를 리턴합니다.
  - 구현
    ```
    {
        "error": "없는회사 is Not Exist."
    }
    ```

### 새로운 회사 추가

- 새로운 언어(tw)도 같이 추가 될 수 있습니다.
- 저장 완료후 header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.

  - 구현
    - 새로운 회사를 만들도록 POST 요청을 받으면 회사 이름과 태그로 분리하여 각각 생성합니다.
    - 언어 필드 값이 기존에 없을 경우 새로 생성 합니다.
    - 최종적으로 header에서 요청한 언어로 생성된 데이터를 보여줍니다.
  - 요청
    ```bash
        curl --location --request POST 'http://127.0.0.1:8000/companies' \
    --header 'x-wanted-language: tw' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "company_name": {
            "ko": "라인 프래시",
            "en": "LINE FRESH"
        },
        "tags": [
            {
                "tag_name": {
                    "ko": "태그_4",
                    "en": "tag_4"
                }
            },
            {
                "tag_name": {
                    "ko": "태그_20",
                    "en": "tag_20"
                }
            },
            {
                "tag_name": {
                    "ko": "태그_16",
                    "en": "tag_16"
                }
            }
        ]
    }'
    ```
  - 결과

  ```json
  {
    "company_name": "LINE FRESH",
    "tags": ["tag_4", "tag_20", "tag_16"]
  }
  ```

## 설치 및 실행 방법

</br>

### Local 개발 및 테스트용

```bash
    # git clone
    git clone https://github.com/JE6BOKM/wanted.git

    cd wanted

    # db migration
    docker-compose -f docker/compose/local.yml run --rm django ./manage.py makemigrations
    docker-compose -f docker/compose/local.yml run --rm django ./manage.py migrate

    # superuser create
    # ! admin 이란 이름으로 생성 할 것
    docker-compose -f docker/compose/local.yml run --rm django ./manage.py createsuperuser

    # 실행
    docker-compose -f docker/compose/local.yml up
```

### 배포용

...

## 폴더 구조

```
.
├── Makefile
├── README.md
├── apps
│   ├── __init__.py
│   ├── company_info
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── local.py
│   │   ├── production.py
│   │   └── test.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── authentications.py
│   │   ├── management
│   │   │   └── commands
│   │   │       └── dummy.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   └── serializers.py
│   ├── urls.py
│   ├── users
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   └── test_viewsets.py
│   │   ├── urls.py
│   │   └── views.py
│   └── wsgi.py
├── conftest.py
├── db_uploader.py
├── docker
│   ├── compose
│   │   ├── local.yml
│   │   └── prod.yml
│   └── images
│       ├── local
│       │   ├── Django.Dockerfile
│       │   └── start
│       └── prod
│           ├── Django.Dockerfile
│           └── start
├── docs
│   ├── api
│   │   ├── authentication.md
│   │   └── users.md
│   └── index.md
├── manage.py
├── mkdocs.yml
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── setup.cfg
├── test
│   ├── __init__.py
│   ├── factories
│   │   ├── __init__.py
│   │   └── users.py
│   └── schema
│       ├── __init__.py
│       └── users.py
└── wait_for_postgres.py
```

---

---

# Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 원티드랩에서 출제한 과제를 기반으로 만들었습니다.
