import cv2
import numpy as np
from PIL import Image, ImageChops


#TODO Image size comparison filter


file1 = Image.open("addedpixel11.png")
file2 = Image.open("addedpixel.png")

print(file1.getpixel((20,20)))

print(file2.getpixel((20,20)))

img = ImageChops.difference(file1,file2)

print(img.getpixel((20,20)))

img.save('imageout4.png')

img2 = np.array(img)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

print(img2[20,20])

grey_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

print(grey_img[20,20])

poo,thresh1 = cv2.threshold(grey_img,0,255,cv2.THRESH_BINARY)

print(thresh1[20,20])
print(thresh1[5,5])

cv2.imwrite('thersh1.png',thresh1)

contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print(contours)

intialimage = np.array(file1)
initialimage = cv2.cvtColor(intialimage,cv2.COLOR_BGR2RGB)

contoured = cv2.drawContours(initialimage, contours, -1, (0,0,255), 5)


cv2.imwrite('locationofstuckpixel.jpg', contoured)


