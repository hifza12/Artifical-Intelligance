#BLACK AND WHITE AND GREY
import cv2
  
originalImage = cv2.imread('C:/Users/ONE10.COMPUTER/Desktop/pic.PNG')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow('Original image',originalImage)
cv2.imshow('Gray image', grayImage)
  
cv2.waitKey(0)

############# ROTATE ############
import cv2 
import numpy as np 
img = cv2.imread('C:/Users/ONE10.COMPUTER/Desktop/pic.PNG')
h,w = img.shape[0:2]
print(h)
print(w)
# cols-1 and rows-1 are the coordinate limits.
M = cv2.getRotationMatrix2D((w/5,h/3),60,.5)
dst = cv2.warpAffine(img,M,(w,h))
cv2.imshow('Rotate image', dst)
  
cv2.waitKey(0)

#############  CROP  ########
import cv2 
import numpy as np 
img = cv2.imread('C:/Users/ONE10.COMPUTER/Desktop/pic.PNG')
h,w = img.shape[0:2]
print(h)
print(w)
SR=int(h*.3)
SC=int(w*.3)
ER=int(h*.7)
EC=int(w*.7)
cropped_img=img[SR:ER,SC:EC]
cv2.imshow('Original image', img)
cv2.imshow('crop image', cropped_img)
  
cv2.waitKey(0)

############ RESIZE  ############
import cv2 
import numpy as np 
image = cv2.imread('C:/Users/ONE10.COMPUTER/Desktop/pic.PNG') 

half = cv2.resize(image, (0, 0), fx = .15, fy = .25) 
bigger = cv2.resize(image, (900, 1010)) 
  
cv2.imshow('Original image', image)
cv2.imshow('halfsize image', half)
cv2.imshow('biggersize image', bigger)
  
cv2.waitKey(0)

###########  FLIP  #############
import cv2

originalImage = cv2.imread('C:/Users/ONE10.COMPUTER/Desktop/pic.PNG')
flipVertical = cv2.flip(originalImage, 0)
flipHorizontal = cv2.flip(originalImage, 1)
flipBoth = cv2.flip(originalImage, -1)
cv2.imshow('Original image', originalImage)
cv2.imshow('Flipped vertical image', flipVertical)
cv2.imshow('Flipped horizontal image', flipHorizontal)
cv2.imshow('Flipped both image', flipBoth)

cv2.waitKey(0)


#########   BLACK AND WHITE AND GREY     #################
import cv2
  
originalImage = cv2.imread('C:/Users/ONE10.COMPUTER/Desktop/pic.PNG')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow('Original image',originalImage)
cv2.imshow('Gray image', grayImage)
  
cv2.waitKey(0)
