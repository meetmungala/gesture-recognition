import cv2

import mediapipe as mp
import pyautogui

# Initialize MediaPipe and Webcam
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_y = None

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    image = cv2.flip(image, 1)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    h, w, _ = image.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get landmark for index finger tip (id=8)
            y = hand_landmarks.landmark[8].y * h

            if prev_y is not None:
                diff = y - prev_y

                if diff > 20:
                    pyautogui.scroll(-50)  # Scroll down
                elif diff < -20:
                    pyautogui.scroll(50)   # Scroll up

            prev_y = y

            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    else:
        prev_y = None  # Reset if hand is not detected

    cv2.imshow("Gesture Scroll", image)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
