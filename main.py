import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import time
import hand_detector


def get_direction():
    # CAMERA SETUP
    width, height = 1280, 720
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # VARIABLES
    gesture_limit = 500
    gesture_shown = False
    gesture_count = 0
    frame_delay = 12
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
            # CHECK FOR GESTURE AND UPDATE DIRECTION
            if data[0]:
                gesture_count += 1
                if gesture_count > frame_delay:
                    action_direction = data[1]  # Update direction variable
                    if action_direction == 'Left':
                        print(action_direction)
                        pyautogui.press('left')
                    elif action_direction == 'Right':
                        print(action_direction)
                        pyautogui.press('right')
                    gesture_shown = False
                    gesture_count = 0

        # OPENING THE WEBCAM
        cv2.imshow("frame", frame)
        key1 = cv2.waitKey(1)
        if key1 == ord('q'):
            break

        return action_direction

    # Release resources after loop exits
    cap.release()
    cv2.destroyAllWindows()


# Main program loop
while True:
    direction = get_direction()
    if direction is not None:
        print("DIRECTION: ", direction)

    # Add other processing or exit logic here (e.g., press a key to quit)
    key2 = cv2.waitKey(1)
    if key2 == ord('q'):
        break

