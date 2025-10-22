import cv2
import numpy as np
import face_recognition
from face_recognition import face_locations

imgelon=face_recognition.load_image_file("musk1.jpg")
imgelon=cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
imgtest=face_recognition.load_image_file("musk2.jpg")
imgtest=cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)


faceloc=face_locations(imgelon)[0]
encodeelon=face_recognition.face_encodings(imgelon)[0]
cv2.rectangle(imgelon,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)


faceloctest=face_locations(imgtest)[0]
encodeelontest=face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(faceloctest[3],faceloctest[0]),(faceloctest[1],faceloctest[2]),(255,0,255),2)

results =face_recognition.compare_faces([encodeelon],encodeelontest)
facedist=face_recognition.face_distance([encodeelon],encodeelontest)

print(results,facedist)

cv2.putText(imgtest,f'{results}{round(facedist[0],2)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.imshow("RGB",imgelon)
cv2.imshow("TEST",imgtest)
cv2.waitKey(0)