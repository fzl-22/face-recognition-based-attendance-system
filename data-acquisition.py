import sqlite3
import cv2
import numpy as np

face_cascade_file = 'cascade classifier/face-detect.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_file)

conn = sqlite3.connect('database/mahasiswa.db')
c = conn.cursor()

total_images = 10
counterNIM = 0
c.execute("SELECT * FROM mahasiswa")
list_nim_nama = c.fetchall()

camera = cv2.VideoCapture(-1)
counter = 1
while True and counterNIM != 10:
    _, frame = camera.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 3)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        if cv2.waitKey(1) & 0xff == ord('c'):
            roi_face = frame_gray[y:y+h, x:x+w]
            cv2.imwrite(f'faces data/mahasiswa.{list_nim_nama[counterNIM][0]}.{list_nim_nama[counterNIM][1]}.{counter}.jpg', roi_face)
            
            print(f"{counter} Images of {list_nim_nama[counterNIM][1]} Captured")
            counter += 1
            if counter > total_images:
                counterNIM += 1
                counter = 1
                break
    cv2.imshow('Face Data Acquisition', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
print("Data Acquisition Completed")