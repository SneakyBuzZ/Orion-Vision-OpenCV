## ORION VISION - Hand Gesture Controlled Keystroke Automation

This project utilizes OpenCV library for real-time hand detection and enables control over specific keystrokes based on hand gestures.

### Project Overview

ORION VISION leverages computer vision to detect hand gestures in front of a webcam. It recognizes two specific gestures:

1.  **Fist:** Triggers a "right key" press (configurable)
2.  **Open Palm:** Triggers a "left key" press (configurable)

These gestures are then translated into keyboard presses ("right" and "left" keys by default) for interacting with your computer.

### Dependencies

- Python 3.x
- OpenCV library (install using pip install opencv-python)

### Hardware

- Webcam

### Functionality

1.  The program initializes the webcam and captures video frames.
2.  It employs OpenCV's hand detection algorithms to identify hands in the frame.
3.  Based on the detected hand posture (fist or open palm):

    - Fist triggers a "right key" press (configurable key).
    - Open palm triggers a "left key" press (configurable key).

4.  The program displays the video feed with detected hand region and keystroke information.

### Usage

1.  Save this markdown file as orion_vision.md alongside the Python script.
2.  Modify the Python script to configure desired keystrokes for each gesture.
3.  Run the Python script.
4.  Open your palm or clench your fist in front of the webcam to trigger key presses.

**Note:** This is a basic outline. The actual Python script will contain functionalities for webcam capture, hand detection, gesture recognition, key simulation, and displaying the video feed.

### Further Enhancements

- Implement additional hand gestures for more complex controls.
- Integrate machine learning for more robust gesture recognition.
- Allow customization of keystroke mapping for different gestures.

### Disclaimer

This project is for educational purposes only. Please be mindful of potential security implications when simulating keystrokes.
