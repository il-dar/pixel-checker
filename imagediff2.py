import cv2
import numpy as np
from PIL import Image, ImageChops


#TODO Image size comparison 


file1 = Image.open("addedpixel11.png")
file2 = Image.open("addedpixel.jpg")

#file1[20,20] = (255,255,255)
#file1.itemset((20,20,1),255)
#file1.itemset((20,20,2),255)

print(file1.getpixel((20,20)))

print(file2.getpixel((20,20)))

img = ImageChops.difference(file1,file2)

print(img.getpixel((20,20)))

img.save('imageout4.png')

img2 = cv2.imread('/home/i/Desktop/20/Programming/pythonopencv/imageout4.png')

print(img2[20,20])

grey_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

print(grey_img[20,20])

poo,thresh1 = cv2.threshold(grey_img,0,255,cv2.THRESH_BINARY)

print(thresh1[20,20])
print(thresh1[5,5])

cv2.imwrite('thersh1.jpg',thresh1)

contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print(contours)

contoured = cv2.drawContours(img2, contours, -1, (0,0,255), 5)

#params = cv2.SimpleBlobDetector_Params()
#params.minThreshold = 0
#params.maxThreshold = 20


#detector = cv2.SimpleBlobDetector_create(params)
#keypoints = detector.detect(thresh1)

#im_with_keypoints = cv2.drawKeypoints(thresh1, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imwrite('imageout.png', contoured)
#cv2.imshow('img',im_with_keypoints)
#cv2.waitKey(0)

