import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    success, img = cap.read()
    if success:
        cv2.imshow("Test", img)
    else:
        print("Hardware still not sending data...")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()