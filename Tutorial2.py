import cv2

# 2. Capture, show, save  video
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter("CapturedVideo.avi", fourcc, 20, (640, 480))

while(cap.isOpened()):
    # capture each frame
    ret, frame = cap.read()

    # convert color to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    flipped = cv2.flip(gray, 0)

    # display frame
    cv2.imshow("Video", flipped)
    # Write frame
    out.write(flipped)

    if cv2.waitKey(1) & 0xFF == ord('q'): # wait for 1 milli sec
        break


# Release capture
cap.release()
out.release()
cv2.destroyAllWindows()
