# face-recognition-based-attendance-system
Face-Recognition-Based Student Attendance System using Haar-Cascade Classifier and Local Binary Pattern Histogram

## 1. Deskripsi Program
Sesuai judul repository, program ini memiliki tujuan untuk melakukan absensi mahasiswa dengan basis pengenalan wajah. Sistem absensi ini juga dibuat dengan mengimplementasikan otomasi pada sistem operasi Linux, sehingga cocok dijalankan di minikomputer seperti Raspberry Pi 4.

## 2. Persiapan
Sebelum menjalankan program, lakukan persiapan berikut (gunakan Python versi 3.10.8):

1. Clone repository ini ke direktori lokal:
`````
git clone https://github.com/fzl-22/face-recognition-based-attendance-system.git
`````

2. Navigasikan ke direktori:
`````
cd face-recognition-based-attendance-system
`````

3. Install package-package yang dibutuhkan di file `requirements.txt`:
`````
pip install -r requirements.txt
`````

4. Buat file crontab:
`````
crontab -e
`````

5. Masukkan script cron untuk otomasi yang mengarah ke file `run.sh` dan `monthly_zip.sh` dengan memakai script yang ada di file `crontab_script.txt` (sesuaikan dengan direktori user).

## 3. Cara Menjalankan Program

1. Izinkan file `run.sh` dan `monthly_zip.sh` agar bisa dieksekusi oleh user:
`````
chmod u+x run.sh monthly_zip.sh
`````
2. Tunggu hingga script dieksekusi oleh cron sesuai perintah pada crontab.

3. (Optional). Eksekusi program secara mandiri dengan perintah berikut:
`````
python main.py
`````
atau
`````
./run.sh
`````
## 6. Penjelasan Setiap Folder dan File
