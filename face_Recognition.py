import threading
import cv2
from deepface import DeepFace
import pyautogui
import random

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

path = r'E:\Python\PYthon Projects\Face_Recogition\ab.jpg' #use your face photo url
reference_img = cv2.imread(path)


def cursor():
    y = random.randint(0,1800)
    pyautogui.moveTo(y,1800)

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame,reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
            cursor()

    except ValueError:
        face_match = False
        cursor()

while True:
    ret, frame = cap.read()
    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText( frame, "MATCH", (20,450), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)
            
        else:
            cv2.putText( frame, "NO-MATCH", (20,450), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),3)   
            
        cv2.imshow("video", frame) 

    key = cv2.waitKey(1)

    if key == ord("e"):

        break

cv2.destroyAllWindows()


