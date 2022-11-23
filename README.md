#### 팀원 정보 및 업무 분담 내역

- **최보영** (팀장)
  
  - Django
    
    - 오류 발생시 코드 수정
  
  - Vue
    
    - App.vue
      
      : bootstrap 의 nav bar 이용하여 nav bar 구현
    
    - HomeView.vue
      
      : 인기 영화 정보를 담은 카드들의 목록 구현
      
      - <mark>아래 내용 넣을 지 말 지 고민해보자,,,</mark>
      
      > MovieCard.vue 를 하위 컴포넌트로 사용하여 목록 만들었음
    
    - MovieCard.vue
      
      : 영화 포스터 이미지와 영화 제목으로 구성된 카드 구현
      
      > 카드 클릭시 클릭한 영화의 상세정보를 볼 수 있는 페이지(MovieView.vue)로 이동
    
    - MovieView.vue
      
      : 영화 상세정보를 볼 수 있는 페이지 구현
      
      > ㅇ
    
    - LatestMovie.vue?
      
      : 추천 알고리즘을 통해 가져온 최신 영화의 포스터 이미지와 영화 제목으로 구성된 카드 구현
    
    - CommunityView.vue
      
      : 최신 영화의 트레일러(????)를 시청할 수 있고, 기대평을 남길 수 있는 커뮤니티 페이지 구현
    
    - CommentCreate.vue
      
      : 기대평(댓글)을 작성하는 폼 구현
    
    - CommentList.vue
      
      : 작성된 기대평(댓글)의 목록 구현
    
    - CommentListItem.vue
      
      : 작성된 각각의 기대평(댓글)의 수정, 삭제 기능 구현
    
    - PopUp.vue
      
      : 댓글 수정시 필요한 폼 구현
    
    - SignUp.vue?
      
      : 회원가입 페이지 구현
    
    - LogIn.vue?
      
      : 로그인 페이지 구현
  
  - CSS
    
    - HomeView.vue 에서 영화 카드위에 마우스를 올리면 테두리 스타일 변경
    
    - HomeView.vue 에서 영화 카드의 사이즈 고정 

- **박현영**
  
  - Django
    
    - movies 앱
      
      1. models.py
         
         Top_Movie, Now_Movie, Comments model 작성
      
      2. urls.py
         
         Top_Movie 영화목록, Now_Movie 영화목록, 댓글 목록, 댓글 상세정보, 댓글 생성 작성
      
      3. serializers.py
         
         Top_Movie 와 Now_Movie 모델의 각각의 영화목록직렬화, Comments 모델의 댓글직렬화 작성
      
      4. views.py
         
         작성한 serializer 를 이용하여 views 함수 작성
    
    - accounts 앱
      
      1. settings.py, models.py
      
      2. urls.py
      
      3. serializers.py
      
      4. views.py
  
  - Vue
  
  - CSS
    
    - nav  bar CSS 지정
    
    - 글자 스타일 설정
    
    - 배경 이미지 설정
    
    - 최신영화 리스트 스크롤 구현
    
    - 댓글 목록 스타일 구현
    
    - ㅇㅇㅇ

#### 목표 서비스 구현 및 실제 구현 정도

- ㅇ

- ㅇ

#### 데이터베이스 모델링 (ERD)

- ㅇ

- ㅇ

#### 영화 추천 알고리즘에 대한 기술적 설명

- <mark>코드를 넣어서 자세하게 설명하기!!</mark>

- Top_Movie 리스트 인 MovieCard 를 하나 클릭하면 이 영화가 가지고 있는 장르 중에서 하나를  랜덤으로 고른다.

- Now_Movie 리스트 중에서 랜덤으로 추출한 장르를 가지고 있는 영화들을 찾는다.

- 찾은 영화들을 랜덤으로 최대 10개(??????)까지 뽑아 추천한다.

#### 서비스 대표 기능에 대한 설명

- <mark>사진도 같이 첨부하여 설명하기!!</mark>

- Top_Movie 영화 검색 가능

- 클릭한 영화와 관련된 추천 영화 제시 (위에 있는 데 넣어야 되남)

- 최신 영화에 기대평 작성 가능

#### 기타 (느낀 점, 후기 등)

- ㅇ
