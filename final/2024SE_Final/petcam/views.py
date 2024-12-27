from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import subprocess
import datetime
import json
import time
import os
import cv2


###Link Google Drive###
def AccessGoogleDrive():
        SCOPES = ['https://www.googleapis.com/auth/drive']
        creds = None

        if os.path.exists('token.json'): #token.json은 자동으로 만들어짐짐
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                        creds.refresh(Request())
                else:
                        flow = InstalledAppFlow.from_client_secrets_file('api_token.json', SCOPES)
                        creds = flow.run_local_server(port=0)

                with open('token.json', 'w') as token:
                        token.write(creds.to_json())

        return creds

def Upload(creds, fpath, fileName, folderID = "구글드라이브폴더ID"):
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
                'name': fileName,
                'parents': [folderID]
        }
        media = MediaFileUpload(fpath, mimetype='video/mp4')

        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

def CurrentDT():
        now = datetime.datetime.now()
        DateTime = now.strftime("%Y%m%d_%H%M%S")
        return DateTime

@csrf_exempt
def start_recording(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        duration = data.get('duration', 10)  # 녹화 시간 기본값: 10초
        output_dir = os.path.join(settings.MEDIA_ROOT, 'recordings')
        os.makedirs(output_dir, exist_ok=True)

        creds = AccessGoogleDrive()

        # 저장 파일 경로
        timestamp = CurrentDT()
        output_file = os.path.join(output_dir, f"recording_{timestamp}.mp4")

        # 카메라 스트림 URL
        stream_url = "http://주소:5000/stream.mjpg"
        cap = cv2.VideoCapture(stream_url)

        if not cap.isOpened():
            return JsonResponse({"error": "카메라 스트림을 열 수 없습니다."}, status=400)

        # 비디오 저장 설정
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # mp4 코덱
        fps = 20.0
        frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        out = cv2.VideoWriter(output_file, fourcc, fps, frame_size)

        # 녹화 루프
        start_time = time.time()
        while time.time() - start_time < duration:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

        # 리소스 정리
        cap.release()
        out.release()

        fpath = f"영상파일경로"

        Upload(creds, fpath, f"recording_{timestamp}.mp4")

        os.remove(fpath)

        return JsonResponse({"file_path": fpath})
    return JsonResponse({"error": "Invalid request method"}, status=405)

    return JsonResponse({"error": "Invalid request method"}, status=405)

# Global variable to store the process
process = None

def toggle_motion():
    global process
    if process:  # If motion is running, stop it
        process.terminate()
        process = None
    else:  # If motion is not running, start it
        process = subprocess.Popen(['python', 'motion.py경로'])

def get_motion_status():
    """Check if motion.py is running"""
    global process
    return "running" if process else "stopped"
    
def toggle_motion_view(request):
    result = toggle_motion()
    return JsonResponse({"status": result})

def get_motion_status_view(request):
    status = get_motion_status()
    return JsonResponse({"status": status})
    
@csrf_exempt
def reset_system(request):
    if request.method in ["POST", "GET"]:  # POST와 GET 모두 허용
        try:
            os.system("sudo reboot")  # 리부트 명령 실행
            return JsonResponse({"status": "success", "message": "Reboot initiated."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

def index(request):
    return render(request, 'petcam/index.html')