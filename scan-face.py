import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[1]
imagePath = []
for i in range(1,1004):
    imagePath.append(str(i)+'.jpg')
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
for i in imagePath:
    image = cv2.imread(i)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.02,
        minNeighbors=50,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces)), '\t',i
    


#Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
