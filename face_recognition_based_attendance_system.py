import sqlite3
import numpy as np
import cv2
import pandas as pd
import statistics as stats
import time
from datetime import datetime
# import os
# from PyQt5.QtCore import QLibraryInfo

# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(QLibraryInfo.PluginsPath)
# print("Hello World:", time.time())

face_cascade = cv2.CascadeClassifier('/home/ahmadfaisal/Documents/College/Semester_3/Tugas_Besar/Revisi_Digital_Image_Processing/face-recognition-based-attendance-system/cascade classifier/face-detect.xml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("/home/ahmadfaisal/Documents/College/Semester_3/Tugas_Besar/Revisi_Digital_Image_Processing/face-recognition-based-attendance-system/face recognizer/face_recognizer.yml")
font = cv2.FONT_HERSHEY_COMPLEX

conn = sqlite3.connect('/home/ahmadfaisal/Documents/College/Semester_3/Tugas_Besar/Revisi_Digital_Image_Processing/face-recognition-based-attendance-system/database/mahasiswa.db')
c = conn.cursor()

attendance_df = pd.read_sql_query("SELECT * FROM mahasiswa", conn)
attendance_df["attendance"] = "Tidak Hadir"
print(attendance_df)

confidence_list = []

camera = cv2.VideoCapture(-1)

start_time = time.time()
while (time.time() - start_time) < 1800: # open camera for 30 minutes (1800 seconds)
    _, frame = camera.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 3)
    for x, y, w, h in faces:
        if w*h >= 40000 and w*h <= 90000:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            roi_face = frame_gray[y:y+h, x:x+w]
            nim_mhs, dist = face_recognizer.predict(roi_face)
            c.execute("SELECT full_name FROM mahasiswa WHERE nim=?", ([nim_mhs]))
            full_name = c.fetchone()
            full_name = full_name[0]
            conn.commit()
            confidence_list.append(full_name)
            cv2.putText(frame, f"{full_name}", (x-20, y-20), font, 0.5, (0, 255, 0), 3)
            if len(confidence_list) == 50:
                most_common_name = stats.mode(confidence_list)
                if confidence_list.count(most_common_name) >= 40: 
                    attendance_df['attendance'].loc[attendance_df['full_name'] == most_common_name] = "Hadir"
                confidence_list.clear()
    # cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
camera.release()
print(attendance_df)
# cv2.destroyAllWindows()
conn.close()

now = datetime.now()
datetime_string = now.strftime("%d-%m-%Y %H:%M:%S")
attendance_df.to_csv(f"/home/ahmadfaisal/Documents/College/Semester_3/Tugas_Besar/Revisi_Digital_Image_Processing/face-recognition-based-attendance-system/result/PCD {datetime_string}.csv")
