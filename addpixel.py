import cv2
import numpy as np

img = cv2.imread('addedpixel.jpg')

img.itemset((20,20,0),180)
img.itemset((20,20,1),75)
img.itemset((20,20,2),75)


cv2.imwrite('addedpixel.png',img)

#img = cv2.imread("DSCF4516.JPG")

#img2 = cv2.imread("DSCF4496.JPG")

#img3 =cv2.imread("thresh1.jpg")

#img2_grey = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#px = img[249,140]
#px2 = img2[249,140]
#px3 = img3[249,140]

#print(px)

#print(px2)

img2 = cv2.imread('addedpixel.png')

px = img2[20,20]

print(px)
