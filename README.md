# 🍦Team CREAM

## ✅ 프로젝트 소개

- 프로젝트 개요: 콩팀콩팀의 여행지 정보 및 후기 공유 커뮤니티 서비스

- 프로젝트 기간:  2022.11.01 ~ 2022.11.08

<br>

## 🎯 기획 목표

- 여행지 정보를 공유하기 위한 리뷰사이트

- 국내, 해외, 테마 인기 여행지 분류

- 각 카테고리별 관광지 리스트 구현

- 관광지 추가 혹은 추가되어 있는 관광지에 리뷰남기기

- 관광지 위치정보 제공

<br>

## 🎯 프로젝트 목표

### Frontend

- Django-Template 사용을 통한 템플릿 관리
- **내장 라이브러리 사용 경험** 쌓기
- **AWS**, **heroku** 사용을 통한 **동적 사이트** 배포

<br>

### Backend

- Django 사용을 통한 DB 관리
- AWS, heroku 사용을 통한 사이트 배포

<br>

### 공통

- 백엔드-프론트엔드 커뮤니케이션 및 통신으로 **협업 경험 쌓기**

<br>

## 👥 팀원 구성

- **Frontend**

  - 최정아
  - 김희동

  **Backend**

  - 김현중(팀장)
  - 손세철
  
    <br>

## 🎥 시연 영상

업로드 예정입니다.

<br>

## 👨‍💻 적용 기술

- Frontend: JavaScript, CSS, Bootstrap, Kakao Map api

- Backend: Python, Django,

- 협업 tool: Git & Github, Notion, Discord, Kanbanboard

<br>

## 🖊 주 구현 기능

- 회원관리
  - 팔로우 및 정보수정

- 메인 페이지
- 관광지 목록 페이지
  - 관광지 추가 페이지

- 관광지 정보 페이지
  - 리뷰 페이지

  - 평점 및 좋아요 구현


<br>

## 💻 팀원별 상세 구현 기능

**김현중**

- 메인 페이지 ( index.html )

  - Background-image, Search bar, Main Text 삽입

  - Grid 반응형 카테고리 분류 탭 구현

  - DB의 Location Entity의 Country Attribute가 True == 국내, False == 해외 구분

  - 테마의 경우 7가지 외에는 etc로 분류

- 관광지 리스트 ( hotlist.html )
  - 지역 이미지 Carousel 삽입
  - Search bar
  - 관광지 Card list ( 후기평균 점수, 최근 후기작성 시간, 좋아요 등 표현 )
  - 페이지네이션 적용
- 관광지 추가 ( hotcreate.html )
  - 명소이름, 주소, 국가, 테마, 명소설명을 필수로 입력받음
  - 주소 input에 주소를 직접 입력 후 주소확인 버튼 클릭
  - 지도 클릭시 해당 위치에 마커생성 및 상세주소 자동입력
  - 테마 선택지 중에 원하는 테마가 없을 경우 직접입력 가능
  - 다중 이미지 upload 기능 구현

- 관광지 페이지 ( detail.html )
  - 이미지 클릭시 입력된 다중이미지 전체를 Modal로 팝업
  - 관광지 Content가 8행 초과시 ellipsis, JS로 toggle 기능 구현
  - 좋아요 비동기 기능 구현
  - 관광지 위치정보 마커 구현
  - 후기탭 작성된 리뷰들 3행 초과시 ellipsis, JS로 toggle 기능 구현
  - 페이지네이션 적용

- 리뷰 추가 ( reviewcreate.html )
  - 별점 range-input 구현
  - 


<br>

**최정아**

- Base
  - Navigation componets design, Footer design

- Accounts app
  - signup, Index, Detail, 회원정보 및 방명록 렌더, 팔로우


<br>

**김희동**

- Detail review list
- Review create, delete, update, read
- Review ppt

<br>

**손세철**

- Base
  - Navbar, body, static 이미지 구현
  - accounts/ index 구현
  - 로그인, 로그아웃 기능 구현
  - 회원 정보 수정 기능 구현
  - Account ppt