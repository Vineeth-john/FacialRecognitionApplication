#importing necessary packages
import cv2, sys, numpy, os
from deepface import DeepFace

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

size = 4
haar_file = (cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #Note the change
datasets = 'C:\\Users\\deshr\\OneDrive\\Desktop\\Final Year Project\\datasets'


print('Recognizing Face Please Be in sufficient Lights...')

# Create a list of images and a list of corresponding names
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
	for subdir in dirs:
		names[id] = subdir
		subjectpath = os.path.join(datasets, subdir)
		for filename in os.listdir(subjectpath):
			path = subjectpath + '/' + filename
			label = id
			images.append(cv2.imread(path, 0))
			labels.append(int(label))
		id += 1
(width, height) = (130, 100)

# Create a Numpy array from the two lists above
(images, labels) = [numpy.array(lis) for lis in [images, labels]]

# OpenCV trains a model from the images

model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

# Implememting the facial identification and expression recognition functions in real time
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)
while True:
    ret, frame = webcam.read()
    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))	
        # Try to recognize the face
        prediction = model.predict(face_resize)		
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        if prediction[1]<80:
            cv2.putText(frame, names[prediction[0]], (x-10, y-10),cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            cv2.putText(frame, result['dominant_emotion'],(x, y+h+20),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2,cv2.LINE_4)
        
        else:
            cv2.putText(frame, 'not recognized',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    
    cv2.rectangle(frame, (200, 75), (425, 300), (0, 255, 255), 2)
    cv2.imshow('OpenCV', frame)
    key = cv2.waitKey(10)
    
    if key == 27:
        break
    	
	
	
		
