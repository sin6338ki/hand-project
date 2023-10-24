from flask import Flask, render_template, Response, jsonify
import cv2
from flask_cors import CORS
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume #Python Core Audio Windows Library
import os #운영체제 종속 기능에 대한 간단한 명령을 모아놓은 기본 모듈

app = Flask(__name__)
#Cor에러 방지
CORS(app)

#mediapipe hands 솔루션 적용
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

#윈도우 오디오 장치 가져오기
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#손가락 사이 간격 계산 메서드
def dist(x1,y1,x2,y2):
    return math.sqrt(math.pow(x1 - x2, 2)) + math.sqrt(math.pow(y1 - y2, 2))

#화면 캡쳐 메서드
def gen_frames_screen():
    global folded_fingers
    global unfolded_fingers

    folded_fingers = 0
    unfolded_fingers = 0
    # 웹캠 카메라 불러오기
    camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # 카메라 번호
    i = 1 #파일명번호
    j = 1 #파일명번호(브이)
    # 손모양 상태 관리
    previous_state = False #다 접었을 때
    current_state = False # 다 폈을 때
    v_on_Off = False #v_capture 실행
    v_restart = True #v_capture 멈춤

    try:
        while True:
            success, frame = camera.read()
            if not success:
                break

            # 영상 처리를 위한 전처리
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 색상 변환
            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                landmarks = results.multi_hand_landmarks[0]
                finger_tips = [8, 12, 16, 20]
                mcp_joints = [5, 9, 13, 17]

                #for tip, mcp in zip(finger_tips, mcp_joint)
                #   if landmarks.landmark[tip].y < landmarks.landmark[mcp].y => 손가락 끝이 손 손가락 시작점 보다 높이 있을 때
                #       and landmarks.landmark[tip].y > landmarks.landmar[0].y => 손가락 끝이 손목보다 높이 있을 때
                #if문에 해당하는 1을 더한다는 뜻
                unfolded_fingers = sum([1 for tip, mcp in zip(finger_tips, mcp_joints) if
                                      landmarks.landmark[tip].y < landmarks.landmark[mcp].y])

                folded_fingers = 4 - unfolded_fingers

                if unfolded_fingers == 4: #4손가락 폈을 때
                    previous_state = True
                elif (dist(landmarks.landmark[0].x, landmarks.landmark[0].y, landmarks.landmark[8].x, landmarks.landmark[8].y)
                    > dist(landmarks.landmark[0].x, landmarks.landmark[0].y, landmarks.landmark[5].x, landmarks.landmark[5].y) + 0.15):
                    if(dist(landmarks.landmark[0].x, landmarks.landmark[0].y, landmarks.landmark[12].x, landmarks.landmark[12].y)
                    > dist(landmarks.landmark[0].x, landmarks.landmark[0].y, landmarks.landmark[9].x, landmarks.landmark[9].y) + 0.2): #손가락이 V 모양일 때
                        v_on_Off = True

                if previous_state == True and folded_fingers == 4: #4손가락을 모두 폈다가 4손가락 모두 접었을 때
                    current_state = True

            # 주먹을 쥐었다 펼쳤을 때
            if (not results.multi_hand_landmarks) and current_state == True: #4손가락 모두 폈다가 접은 후 손이 화면에 안보일 때

                #delay
                delay = 10000000
                while (delay != 0):
                    delay = delay - 1

                previous_state = False
                current_state = False
                file_name = 'capture' + str(i) + '.jpg'
                i += 1
                cv2.imwrite(file_name, frame) #이미지 저장
                path = os.path.realpath('../mediapipe_server') 
                os.startfile(path) #저장 파일 위치 열기

            if v_restart == True and v_on_Off == True: #v했을 때
                previous_state = False
                current_state = False
                v_on_Off = False
                v_restart = False
                file_name = 'v_capture' + str(j) + '.jpg'
                j += 1
                cv2.imwrite(file_name, frame)
                path = os.path.realpath('../mediapipe_server')
                os.startfile(path)

            if unfolded_fingers == 1: #v후 한 손가락만 폈을 때 다시 v 캡쳐가 가능하도록 변경
                v_restart = True
                v_on_Off = False

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    finally:
        camera.release()

#볼륨 조절 메서드
def gen_frames_volume():
    # 웹캠 카메라 불러오기
    camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # 카메라 번호
    try:
        while True:
            success, frame = camera.read()
            if not success:
                break

            # 영상 처리를 위한 전처리
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 색상 변환
            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks: 
                    #4번째 손가락을 접었을 때 볼륨 조절 가능하도록 설정
                    open = (dist(handLms.landmark[0].x, handLms.landmark[0].y, handLms.landmark[14].x, handLms.landmark[14].y)
                            < dist(handLms.landmark[0].x, handLms.landmark[0].y, handLms.landmark[16].x, handLms.landmark[16].y))
                    if open == False:
                        #엄지와 검지 사이의 거리 / 엄지와 검지 시작점 간 거리 * 2 (0~1사이의 값으로 만들어 주기 위한 처리)
                        curdist = (-dist(handLms.landmark[4].x, handLms.landmark[4].y, handLms.landmark[8].x, handLms.landmark[8].y)
                                   / (dist(handLms.landmark[2].x, handLms.landmark[2].y, handLms.landmark[5].x, handLms.landmark[5].y) * 2))
                        curdist = curdist * 100
                        curdist = -62.25 - curdist
                        curdist = min(0, curdist)
                        volume_level = min(max(curdist, -65.25), 0) #윈도우 오디오 최댓값 0, 최솟값 -65.25
                        #볼륨 변환
                        vol = round((curdist + 62.5) * 1.6, 0)
                        str = "Volume : %s" % vol
                        cv2.putText(frame, str, (20,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0)) #영상에 TEXT 표시
                        volume.SetMasterVolumeLevel(volume_level, None)
                    mp_drawing.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    finally:
        camera.release()

@app.route('/video_frame_volume')
def video_feed_volume():
    return Response(gen_frames_volume(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_frame_screen')
def video_feed_screen():
    return Response(gen_frames_screen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api', methods=['POST'])
def get_text_response():

    response_message = f"접힌 손가락 수: {folded_fingers}, 안 접힌 손가락 수: {unfolded_fingers}"

    return jsonify({"response": response_message})

@app.route('/')
def index():
    return render_template('handtracking.html')

if __name__ == '__main__':
    app.run(debug=True)