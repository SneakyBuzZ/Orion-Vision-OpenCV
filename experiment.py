import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import time
import hand_detector


# CAMERA SETUP
width, height = 640, 360
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# VARIABLES
gesture_limit = 500
gesture_shown = False
gesture_count = 0
frame_delay = 20
action_direction = None

# HAND DETECTOR
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    # READING THE FRAMES
    success, frame = cap.read()
    h, w, _ = frame.shape
    cv2.line(frame, (0, gesture_limit), (w, gesture_limit), (0, 255, 0), 1)
    frame = cv2.flip(frame, 1)

    hands, frame = detector.findHands(frame, flipType=False)

    data = hand_detector.get_gesture(gesture_limit=gesture_limit,
                                     gesture_shown=gesture_shown,
                                     detector=detector,
                                     hands=hands)

    if data is not None:
        # ADDING DELAY IN FRAMES
        if data[0]:
            gesture_count += 1
            if gesture_count > frame_delay:
                if data[1] == 'Left':
                    print(data[1])
                    pyautogui.press('left')
                elif data[1] == 'Right':
                    print(data[1])
                    pyautogui.press('right')
                gesture_shown = False
                gesture_count = 0

    # OPENING THE WEBCAM
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break




