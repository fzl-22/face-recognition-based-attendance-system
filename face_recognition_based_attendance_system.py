import sqlite3
import numpy as np
import cv2
import pandas as pd

face_cascade = cv2.CascadeClassifier('cascade classifier/face-detect.xml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("face recognizer/face_recognizer.yml")
font = cv2.FONT_HERSHEY_COMPLEX

conn = sqlite3.connect('database/mahasiswa.db')
c = conn.cursor()

camera = cv2.VideoCapture(-1)
while True:
    _, frame = camera.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 3)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        roi_face = frame_gray[y:y+h, x:x+w]
        nim_mhs, dist = face_recognizer.predict(roi_face)
        c.execute("SELECT full_name FROM mahasiswa WHERE nim=?", ([nim_mhs]))
        full_name = c.fetchone()
        full_name = full_name[0]
        conn.commit()
        cv2.putText(frame, f"{full_name}", (x-20, y-20), font, 0.5, (0, 255, 0), 3)
    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
conn.close()

        

conn.close()
    