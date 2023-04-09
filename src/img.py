import matplotlib.pyplot as plt
import cv2

img = cv2.imread("../data/images/camera_calibration.jpeg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()