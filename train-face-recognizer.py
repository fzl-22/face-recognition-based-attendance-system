import os
import cv2
import numpy as np

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

path_images = os.listdir("faces data")
image_array_list = []
image_nim_list = []
image_name_list = []

for path_image in path_images:
    split_path = path_image.split('.')
    image_nim = int(split_path[1])
    image_name = split_path[2]
    image_path = os.path.join('faces data', path_image)
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_array = np.array(image)
    image_array_list.append(image_array)
    image_nim_list.append(image_nim)

face_recognizer.train(image_array_list, np.array(image_nim_list))
face_recognizer.save('face recognizer/face_recognizer.yml')
print("Face Recognizer Has Been Successfully Trained!")