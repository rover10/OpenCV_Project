import cv2
import time
cam = cv2.VideoCapture(0)
rad = 2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #print gray
    print img.shape
    breadth = img.shape[0]
    hegith = img.shape[1]
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    leftMargin = (breadth/7)*3
    rightMargin = (breadth/7)*4
    print leftMargin
    print rightMargin 
    for (x,y,w,h) in faces:
    	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    	roi_gray = gray[y:y+h, x:x+w]
    	roi_color = img[y:y+h, x:x+w]
    	eyes = eye_cascade.detectMultiScale(roi_gray)
    	for (ex,ey,ew,eh) in eyes:
    		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		#if eyes detected move robot towards it
		# decide the side of the face
		if x+w < leftMargin:
			#Turn left to position the face towards the face
			print "Left"
		elif x > rightMargin:
			#Turn right
			print "Right"
		else:
			#move forward
			print "Centre"
		time.sleep(0.5)	
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Detect keypoints and descriptors in greyscale image
  #  keypoints, descriptors = surf.detect(gray, None, False)

    #Draw a small red circle with the desired radius
    #at the (x, y) location for each feature found

    #Display colour image with detected features
    cv2.imshow("features", img)

    #Sleep infinite loop for ~10ms
    #Exit if user presses <Esc>
    if cv2.waitKey(10) == 27:
        break
