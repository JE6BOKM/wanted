# 프레시코드
- 과제 출제 기업 정보
  - 기업명 : 프레시코드
  - [프레시코드](https://freshcode.com/)
  - [wanted 채용공고 링크](https://www.wanted.co.kr/company/4865)

## 💁‍♀️ Members
|이름   |github                   |담당 기능|
|-------|-------------------------|--------------------|
|신재민 |[shinjam](https://github.com/shinjam)     | 테스트 코드   |
|신우주 |[shinwooju](https://github.com/shinwooju)     | 상품 CRUD   |
|최혜림 |[rimi0108](https://github.com/rimi0108)     | 로그인   |
|강성묵 |[miranaky](https://github.com/miranaky)     | 로그인   |
|김민규 |[miranaky](https://github.com/SkyStar-K)     | 상품 CRUD  |


## ⭐ 과제 내용

### [필수 포함 사항]
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현
    - Swagger 대신 Postman 이용시 API 목록을 Export하여 함께 제출해 주세요
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger를 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅

### [개발 요구사항]
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현
    - Swagger 대신 Postman 이용시 API 목록을 Export하여 함께 제출해 주세요
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger를 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅


## 사용 기술 및 tools
> - Back-End :  <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/mysql 8.0-1b9e41?style=for-the-badge&logo=Mysql&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC :  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

## 🏄‍♀️ 모델링
![5 drawio](https://user-images.githubusercontent.com/8315252/139969615-38f01f08-cc1c-427e-87a6-09671525525b.png)

## API
[링크-postman document](https://documenter.getpostman.com/view/16042359/UVBzmpLX)

## 구현 기능

### 로그인 기능
- 사용자 인증을 통해 상품 관리를 할 수 있어야 합니다.
    - 구현
        - JWT 인증 방식을 이용합니다.
        - 서비스 실행시 데이터베이스 또는 In Memory 상에 유저를 미리 등록해주세요.
        - Request시 Header에 Authorization 키를 체크합니다.
        - Authorization 키의 값이 없거나 인증 실패시 적절한 Error Handling을 해주세요.
        - 상품 추가/수정/삭제는 admin 권한을 가진 사용자만 이용할 수 있습니다.
    - 시용자 인증 / 인가

        ```
        사전 등록된 사용자는 총 2명입니다.

        - 사용자 1번
        	EMAIL: user@freshcode.me
        	PASSWORD: user
          ROLE : [user]

        - 사용자 2번
        	EMAIL: admin@freshcode.me
        	PASSWORD: admin
          ROLE : [admin]
        ```


### 상품 관리 기능
- 아래 상품 JSON 구조를 이용하여 데이터베이스 및 API를 개발해주세요.
    - 구현
        - 서비스 실행시 데이터베이스 또는 In Memory 상에 상품 최소한 5개를 미리 생성해주세요.
        - 상품 조회는 하나 또는 전체목록을 조회할 수 있으며, 전체목록은 페이징 기능이 있습니다.
            - 한 페이지 당 아이템 수는 5개 입니다.
        - 사용자는 상품 조회만 가능합니다.
        - 관리자는 상품 추가/수정/삭제를 할 수 있습니다.
        - 상품 관리 API 개발시 적절한 Error Handling을 해주세요.
    - 상품 구조

        ```json
        // JSON DATA Structure
        {
          menus: [
            {
              id: 245,
              category: "SALAD",
              name: "깔라마리 달래 샐러드",
              description: "해산물 샐러드",
              isSold: false,
              badge: "NEW",
              items: [
                {
                  id: 1,
                  menuId: 245,
                  name: "미디움",
                  size: "M",
                  price: 8000,
                  isSold: false,
                },
              ],
              tags: [
                {
                  id: 1,
                  menuId: 245,
                  type: "vegetarianism",
                  name: "페스코베지테리언"
                }
              ],
            }
          ]
        }

        ```

## API TEST 방법
...

## 설치 및 실행 방법
###  Local 개발 및 테스트용
...

###  배포용
...

## 폴더 구조


# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 **에서 출제한 과제를 기반으로 만들었습니다.
