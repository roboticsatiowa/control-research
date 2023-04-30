import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0) #main videp camera

# https://google.github.io/mediapipe/solutions/hands.html
# Database of manually annotated pictures of hands and has inbuilt functions

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # 20:00 in video "Advanced Computer Vision with Python"

    cv2.imshow("Image", img)
    cv2.waitKey(1)
