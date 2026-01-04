import cv2

# Initialize the camera (0 is usually the default webcam)
cap = cv2.VideoCapture(0)

print("System: Camera initialized. Press 'q' to exit.")

while True:
    # Read the camera frame
    success, img = cap.read()

    # Show the video feed in a window
    cv2.imshow("Abhinav's Camera", img)

    #Image Shape
    print(img.shape)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up: Release hardware and close window
cap.release()
cv2.destroyAllWindows()