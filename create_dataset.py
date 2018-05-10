import cv2

cap = cv2.VideoCapture('gate_video.MP4')

imageNumber = 0
while(cap.isOpened()):

	ret, frame = cap.read()

	if ret :
		cv2.imshow("frame",frame)
		cv2.imwrite("image"+str(imageNumber)+".jpg",frame)
		imageNumber+=1
		
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
