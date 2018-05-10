import cv2
import os
referencePoint = []
FILE = open("locations.txt","a")
imageNumberStart = int(input("Enter starting image number:- "))
imageNumberEnd = int(input("Enter ending image number:- "))
def click_function(event,x,y,flags,params):
	global referencePoint

	if event == cv2.EVENT_LBUTTONDOWN:
		referencePoint=[(x,y)]
		

	elif event == cv2.EVENT_LBUTTONUP:
		referencePoint.append((x,y))
		

		cv2.rectangle(image,referencePoint[0],referencePoint[1],(255,0,0),2)
		cv2.imshow("image",image)
	
cv2.namedWindow("frame")
cv2.setMouseCallback("frame",click_function)
imageNumber = imageNumberStart

while imageNumber<=imageNumberEnd:
	image = cv2.imread("dataset/positive/"+str(imageNumber)+".jpg")
	
	cv2.imshow("frame",image)
	
	imageNumber+=1
	cv2.waitKey(0)
	print referencePoint
	FILE.write(str(imageNumber-1))
	FILE.write(" ")
	FILE.write(str(referencePoint))
	FILE.write("\n")

	


