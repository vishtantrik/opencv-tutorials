import cv2
from matplotlib import pyplot as plt

# 1. Read, display, write image
img = cv2.imread('Su-30.jpg', 0) # 0 for grayscale, 1 for color
cv2.imshow("Image", img)
k = cv2.waitKey(0) & 0xFF

if k == 27: # Esc key
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("ReadImage.png", img)
    cv2.destroyAllWindows()

plt.imshow(img, cmap = 'gray')
plt.show()
plt.close()