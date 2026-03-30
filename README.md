# Gesture Recognition Scroll

This project uses your webcam to track your hand gestures and scroll your screen up or down entirely hands-free.

## Features
- **Hands-Free Scrolling**: Scroll documents and webpages simply by moving your index finger up and down.
- **Real-Time UI Overlay**: An interactive on-screen display shows you instructions and the current scrolling status.

## Technologies Used
- **Python**
- **OpenCV**: Handles webcam feed
- **MediaPipe**: Real-time hand tracking and 3D land marking points
- **PyAutoGUI**: Simulates mouse scroll commands

## How To Use
1. Install the required libraries via `pip install opencv-python mediapipe pyautogui`
2. Run `demo1.py`.
3. Raise your hand so the camera captures it. Move your index finger up and down to trigger the scrolling!
4. Press `ESC` to exit the program.
