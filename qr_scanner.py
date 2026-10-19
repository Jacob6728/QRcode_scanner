import cv2

qr_detector = cv2.QRCodeDetector()

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

print("QR Code Scanner Started!")
print("Hold a QR code in front of the camera to scan it")
print("Press 'q' to quit.")

last_scanned_data = ""

while True:

    success, frame = camera.read()


    if not success:
        print("Error: Could not read frame from camera.")
        break

    data, points, _ = qr_detector.detectAndDecode(frame)

    if points is not None and data:

        points = points.astype(int)

        for i in range(len(points[0])):

            pt1 = tuple(points[0][i])

            pt2 = tuple(points[0][(i+1) % 4])

            cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

        if data != last_scanned_data:
            print("\nQR Code Detected!")
            print("Content:", data)

            last_scanned_data = data

        cv2.putText(frame, "QR Code Detected!", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        camera.release()
        cv2.destroyAllWindows()

        print("\nQR Code Scanner Stopped.")