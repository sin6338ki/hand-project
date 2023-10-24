# hands-tracking 
## 프로젝트 소개 
- 프로젝트명 : 핸드 제스처를 활용한 볼륨 조절 및 영상 캡처 서비스
- 프로젝트 기간 : 2023년 10월 20일 ~ 2023년 10월 23일
- 활용 기술
  1. Flask를 활용한 웹서버 구현
  2. OpenCV를 활용한 영상 및 이미지 처리
  3. MediaPipe Hands를 활용한 손가락 인식 및 추적
## 사용 언어 및 도구 
![image](https://github.com/sin6338ki/hand-project/assets/130349912/1f49544b-c1be-4ce7-a842-6b56c2ef3d07)
## 개발 내용 
### 볼륨 조절 기능 
- 엄지와 검지 손가락을 활용해 볼륨 조절을 할 수 있습니다.
- 약지를 접은 상태에서만 조절이 가능하고, 두 손가락 사이가 멀어질수록 볼륨이 커지고 가까워질수록 볼륨이 작아집니다.

![image](https://github.com/sin6338ki/hand-project/assets/130349912/2d0c4f92-570c-4145-9fcd-d34f5bd42ba6)
- 개발 방법
![image](https://github.com/sin6338ki/hand-project/assets/130349912/8f8d6770-f534-4dca-a2a4-20e3030ce4b3)
### 영상 화면 캡처 기능
- 두 가지 방법을 통해 캡처가 가능합니다.
  1. 손바닥을 모두 펼쳤다 쥔 후
  2. 브이했을 때
- 캡쳐가 완료되면 파일이 저장된 위치를 불러옵니다.
  ![image](https://github.com/sin6338ki/hand-project/assets/130349912/7b222822-f6aa-48c1-8a9b-d7c12a6532be)
- 개발 방법
  ![image](https://github.com/sin6338ki/hand-project/assets/130349912/1c7dd49c-5682-41dd-9bbd-9e8e31d96989)
### 트러블 슈팅
1. ![image](https://github.com/sin6338ki/hand-project/assets/130349912/ed6042f3-0d50-4bfb-97f9-91bfd7793b71)
2. ![image](https://github.com/sin6338ki/hand-project/assets/130349912/8ea06de4-366f-4b5f-a69d-65bff3fcc101)
## 향후 발전 방향
1. 볼륨 조정 로직 변경
  - 현재 : 엄지와 검지 손가락 간격이 좁은 범위에서 움직이며, 작은 볼륨은 조절이 어려운 상태
  - 향후방안 : 로직 변경을 통해 범위를 넓히고, 작은 볼륨도 조절이 가능하도록 변경 필요
2. 카운트 기능 추가
  - 현재 : MediaPipe에서 손이 인식되지 않을 경우 캡처하도록 구현하였으나 정확도가 떨어짐
  - 향후 방안 : 주먹을 쥔 후 3초간 카운트를 부여하여 원하는 자세로 촬영 가능하도록 보완 필요
