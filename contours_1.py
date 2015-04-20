import numpy as np
import cv2
 
im = cv2.imread('cropped.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(im,contours,-1,(0,255,0),3)

people = 0

for i in contours:

	m = cv2.moments(i)
	area = cv2.contourArea(i)

	if (m['m00'] != 0) and (area > 10):
		centroid_x = int(m['m10']/m['m00'])
		centroid_y = int(m['m01']/m['m00'])

		print "area: ", area
		print "x: ", centroid_x, "y: ", centroid_y

		cv2.drawContours(im,i,-1,(0,255,0),3)
		people = people + 1

print "number of people: ", people

cv2.imshow("Contours", im)
cv2.waitKey(0)