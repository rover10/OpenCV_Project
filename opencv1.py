import cv2

#Create object to read images from camera 0
cam = cv2.VideoCapture(0)

#Initialize SURF object
#surf = cv2.SURF(85)

#Set desired radius
rad = 2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    #Get image from webcam and convert to greyscale
    ret, img = cam.read()
    

	#img = cv2.imread('messi.jpeg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
    	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    	roi_gray = gray[y:y+h, x:x+w]
    	roi_color = img[y:y+h, x:x+w]
    	eyes = eye_cascade.detectMultiScale(roi_gray)
    	for (ex,ey,ew,eh) in eyes:
    		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

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
