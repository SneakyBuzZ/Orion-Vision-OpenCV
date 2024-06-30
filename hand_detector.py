
def get_gesture(hands, gesture_shown, gesture_limit, detector):

    # GESTURE DETECTION
    if hands and gesture_shown is False:
        hand = hands[0]
        center_x, center_y = hand['center']

        hand_type = hand['type']

        # PERFORMING OPERATIONS ONLY WITHIN THE GESTURE LIMIT
        if center_y < gesture_limit:
            fingers_up = detector.fingersUp(hand)
            if hand_type == 'Left':
                if fingers_up == [0, 0, 0, 0, 0]:
                    gesture_shown = True
                    return [gesture_shown, "Right"]
                elif fingers_up == [1, 0, 0, 0, 1]:
                    gesture_shown = True
                    return [gesture_shown, "Left"]
            elif hand_type == 'Right':
                if fingers_up == [0, 0, 0, 0, 0]:
                    gesture_shown = True
                    return [gesture_shown, "Left"]
                elif fingers_up == [1, 0, 0, 0, 1]:
                    gesture_shown = True
                    return [gesture_shown, "Right"]

