import cv2
import numpy as np

# 3. Draw shapes and insert text into images

# Create black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw line
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 3, cv2.LINE_AA)
# Draw circle
img = cv2.circle(img, (256, 256), 30, (256, 256, 256), -1, cv2.LINE_AA)
# Draw rectangle
img = cv2.rectangle(img, (100, 226), (412, 286), (100, 256, 0), 1, cv2.LINE_AA)
# Draw polygon
points = np.array([[11, 24], [500, 24], [500, 488]], np.int32)
points = points.reshape((-1, 1, 2)) # however many num of rows, 1 col, 2 in 3rd dim
img = cv2.polylines(img, [points], True, (0, 200, 200), 2, cv2.LINE_AA)
# Insert text
img = cv2.putText(img, "vishruth@", (300, 500), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 100, 256))

# Show image
while(True):
    cv2.imshow("Image", img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# Close everything
cv2.destroyAllWindows()
