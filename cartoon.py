import cv2
import numpy as np


imagen = cv2.imread("barack.png")
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)



color = cv2.bilateralFilter(imagen, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

#cv2.imshow("Image", imagen)
#cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

