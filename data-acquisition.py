import sqlite3
import cv2
import numpy as np

face_cascade_file = 'cascade classifier/face-detect.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_file)

conn = sqlite3.connect('database/mahasiswa.db')
c = conn.cursor()

total_images = 10
nim = int(input("Masukkan NIM\t\t: "))
nama = input("Masukkan Nama Mahasiswa\t: ")
c.execute("INSERT INTO mahasiswa VALUES (?, ?)", (nim, nama))
conn.commit()

c.execute("SELECT * FROM mahasiswa")
print(c.fetchall())
conn.commit()

camera = cv2.VideoCapture(-1)
counter = 1
while True and counter != 11:
    _, frame = camera.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 3)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        if cv2.waitKey(1) & 0xff == ord('c'):
            roi_face = frame_gray[y:y+h, x:x+w]
            cv2.imwrite(f'faces data/mahasiswa.{nim}.{nama}.{counter}.jpg', roi_face)
            
            print(f"{counter} Images of {nama} Captured")
            counter += 1
            if counter > total_images:
                break
    cv2.imshow('Face Data Acquisition', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
c.execute("SELECT * FROM mahasiswa")
print("Student Who Have Submitted:\n")
print(c.fetchall())
conn.commit()
conn.close()