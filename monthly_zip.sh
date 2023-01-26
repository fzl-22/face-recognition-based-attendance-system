#!/bin/bash

month=$(date +%B)
year=$(date +%Y)
file_name="$month-$year-Attendance"

cd /home/ahmadfaisal/Documents/College/Semester_3/Tugas_Besar/Revisi_Digital_Image_Processing/face-recognition-based-attendance-system/result

zip $file_name.zip *csv
rm *csv
