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
        # Process the first hand detected to avoid erratic switching between hands
        hand_landmarks = results.multi_hand_landmarks[0]
        
        # Get landmark for index finger tip (id=8)
        y = hand_landmarks.landmark[8].y * h

        if prev_y is None:
            prev_y = y
        else:
            diff = y - prev_y

            # Update prev_y only when we actually scroll, to accumulate slower movements
            if diff > 30:
                pyautogui.scroll(-300)  # Scroll down
                prev_y = y
            elif diff < -30:
                pyautogui.scroll(300)   # Scroll up
                prev_y = y

        # Draw landmarks for all detected hands
        for hlms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hlms, mp_hands.HAND_CONNECTIONS)

    else:
        prev_y = None  # Reset if hand is not detected

    cv2.imshow("Gesture Scroll", image)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
