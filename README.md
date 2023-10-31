# Laporan Proyek Machine Learning
### Nama  : **Ihsan Darojatul U'la**
### Nim   : 231352001
### Kelas : Malam A

# Memahami Kualitas Air Dengan Teknologi : Aplikasi Data Mining dalam memprediksi Kualitas Air menggunakan Python
### **Summary**
Kualitas air merupakan salah satu komponen lingkungan yang sangat penting dan sebagai indikator sehatnya suatu daerah aliran sungai. Sejalan dengan perkembangan jumlah penduduk dan meningkatnya kegiatan masyarakat dan industri mengakibatkan perubahan fungsi lingkungan.     

### **Business Understanding**
Teknologi dan metode ilmu data (data mining) telah menjadi alat yang sangat berguna dalam pemahaman dan prediksi kualitas air. Dalam konteks ini, data mining digunakan untuk menganalisis sejumlah besar data material yang mencakup informasi tentang kualitas kadar air.


### **Goals**
Dengan menggunakan teknik-teknik data mining, kita dapat mengidentifikasi pola dan hubungan dalam data ini untuk memprediksi risiko atau kemungkinan kualitas air adalah aman atau tidak. Dalam  Aplikasi ini akan memungkinkan pengguna untuk memasukkan informasi material seperti aluminium, amonia, arsenik, barium, kadmium, kloramin, kromium, tembaga, flouride, bakteri, virus, dan lainnya. Lalu akan memberikan prediksi tentang apakah kualitas air tersebut aman atau tidak.


### **Solution statements**
Saya akan mencoba mengembangkan sebuah aplikasi menggunakan bahasa pemrograman Python dan teknik data mining untuk memprediksi kualitas air.

### **Data Understanding**
Dalam proyek ini, saya menggunakan dataset dari [Kaggle](https://www.kaggle.com). Dataset ini, yang disebut [Water Quality](https://www.kaggle.com/datasets/mssmartypants/water-quality)
, berisi data material yang kita gunakan untuk menganalisis dan memprediksi kualitas air. dataset [Water Quality](https://www.kaggle.com/datasets/mssmartypants/water-quality) ini dipilih karena relevansi atribut-atributnya dalam proyek ini."

###  **Variabel-variabel pada Aplikasi Data Mining dalam memprediksi Kualitas Air menggunakan Python** 
Selanjutnya variabel atau fitur pada data ini adalah sebagai berikut :  

    -) aluminium - berbahaya jika lebih besar dari 2,8
    -) amonia - berbahaya jika lebih besar dari 32,5
    -) arsenik - berbahaya jika lebih besar dari 0,01
    -) barium - berbahaya jika lebih besar dari 2
    -) kadmium - berbahaya jika lebih besar dari 0,005
    -) kloramin - berbahaya jika lebih besar dari 4 dan 0(< 120 mg/dL)
    -) kromium - berbahaya jika lebih besar dari 0,1
    -) tembaga - berbahaya jika lebih besar dari 1,3
    -) flouride - berbahaya jika lebih besar dari 1,5
    -) bakteri - berbahaya jika lebih besar dari 0setelah latihan fisik)
    -) virus - berbahaya jika lebih besar dari 0
    -) timbal - berbahaya jika lebih besar dari 0,015
    -) nitrat - berbahaya jika lebih besar dari 10
    -) merkuri - berbahaya jika lebih besar dari 0,002
    -) perklorat - berbahaya jika lebih besar dari 56
    -) radium - berbahaya jika lebih besar dari 5
    -) selenium - berbahaya jika lebih besar dari 0,5
    -) perak - berbahaya jika lebih besar dari 0,1
    -) uranium - berbahaya jika lebih besar dari 0,3
    -) is_safe - atribut kelas {0 - tidak aman, 1 - aman}

Adapun tipe data dalam dataset [Water Quality](https://www.kaggle.com/datasets/mssmartypants/water-quality) yaitu:

 No|  Column    |  Non-Null Count | Dtype  |
---|------------|-----------------|--------| 
 0 | aluminium  | 7999 non-null   | float64|
 1 | ammonia    | 7999 non-null   | object |
 2 | arsenic    | 7999 non-null   | float64|
 3 | barium     | 7999 non-null   | float64|
 4 | cadmium    | 7999 non-null   | float64|
 5 | chloramine | 7999 non-null   | float64|
 6 | chromium   | 7999 non-null   | float64|
 7 | copper     | 7999 non-null   | float64|
 8 | flouride   | 7999 non-null   | float64|
 9 | bacteria   | 7999 non-null   | float64|
 10| viruses    | 7999 non-null   | float64|
 11| lead       | 7999 non-null   | float64|
 12| nitrates   | 7999 non-null   | float64|
 13| nitrites   | 7999 non-null   | float64|
 14| mercury    | 7999 non-null   | float64|
 15| perchlorate| 7999 non-null   | float64|
 16| radium     | 7999 non-null   | float64|
 17| selenium   | 7999 non-null   | float64|
 18| silver     | 7999 non-null   | float64|
 19| uranium    | 7999 non-null   | float64|
 20| is_safe    | 7999 non-null   | object |
dtypes: float64(19), object(2)

## Data Preparation
Teknik data preparation yang dilakukan adalah :
- Menentukan library yang akan digunakan
- Membaca dataset [Water Quality](https://www.kaggle.com/datasets/mssmartypants/water-quality) yang telah didownload, yaitu file waterQuality.csv  
- Deskripsi dataset
- Memisahkan datasets
- Membuat model training
- Membuat model evaluasi
- Membuat model prediksi
- Simpan model untuk proses deploy ke streamlit


## Modeling
Prediksi Aplikasi Data Mining dalam memprediksi kualitas air menggunakan Python menggunakan algoritma logistic regression, Alasan mengapa menggunakan algoritma logistic regression untuk model prediksi kualitas airt dalam proyek ini adalah sebagai berikut:

    1. Sangat efektif untuk klasifikasi data biner
    2. Sangat mudah diimplementasikan dan diinterpretasikan
    3. Dapat digunakan pada dataset yang memiliki banyak variable input

## Evaluation
Sebelum membuat model prediksi saya mencoba membuat evaluasi tingkat akurasi data menggunakan algoritma logistic regression. berikut :

Matrik konfusi adalah alat evaluasi yang umum digunakan dalam pemodelan klasifikasi untuk mengukur sejauh mana model klasifikasi dapat memprediksi dengan benar kelas-kelas target. Matriks konfusi biasanya dibagi menjadi empat sel atau komponen, yang mencakup True Positives (TP), False Positives (FP), True Negatives (TN), dan False Negatives (FN). Dan dari hasil menggunakan metrik (Akurasi) saya berhasil mendapatkan tingkat akurasi dalam model prediksi ini adalah sekitar 89% - 90%.

Dari hasil Laporan klasifikasi ini sesuai dengan konteks data yang memberikan gambaran tentang sejauh mana model klasifikasi berhasil dalam memprediksi kelas is_safe(kualitas air), baik untuk kelas 0(tidak) maupun kelas 1(ya). 


## Deployment
Berikut hasil dari akhir proyek https://tugasutsmachinglearning-raq5hrqnjcrhvcthdp59qc.streamlit.app/

**---Ini adalah bagian akhir laporan---**
