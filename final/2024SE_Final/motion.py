import cv2
import requests
import telegram

# 스트림 URL (카메라 MJPEG 스트림 URL)
stream_url = "http://주소:5000/stream.mjpg"
start_recording_url = "http://주소:8000/petcam/start-recording/"

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def detect_motion():
    # OpenCV로 카메라 스트림 분석
    cap = cv2.VideoCapture(stream_url)
    first_frame = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 프레임을 그레이스케일로 변환
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

        # 첫 번째 프레임 저장
        if first_frame is None:
            first_frame = gray_frame
            continue

        # 현재 프레임과 첫 번째 프레임의 차이 계산
        frame_delta = cv2.absdiff(first_frame, gray_frame)
        thresh = cv2.threshold(frame_delta, 100, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        # 윤곽선 검출
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue

            # 움직임 감지 시 Django 서버에 POST 요청
            print("움직임 감지! Django 서버에 녹화 요청을 보냅니다.")
            send_telegram_message("봇 토큰", "챗ID", "카메라에 움직임 감지")
            try:
                headers = {
                    'Content-Type': 'application/json'
                }
                data = {"duration": 10}  # 요청 데이터 (10초 동안 녹화)
                response = requests.post(start_recording_url, headers=headers, json=data)
                print("서버 응답:", response.json())
            except Exception as e:
                print(f"서버 요청 중 오류 발생: {e}")

            # 한 번 움직임 감지 후 첫 프레임 초기화
            first_frame = None
            break

    cap.release()
    print("스트림 종료.")

if __name__ == "__main__":
    detect_motion()
