# Aplikasi Prediksi Jenis Ikan

Aplikasi ini menggunakan model Random Forest Classifier untuk memprediksi jenis ikan berdasarkan panjang, berat, dan rasio berat/panjang ikan. Aplikasi ini dibangun menggunakan Streamlit untuk antarmuka pengguna yang interaktif.

## Fitur

- Prediksi jenis ikan berdasarkan input panjang dan berat.
- Visualisasi confusion matrix dan imporatance feature.
- Informasi model yang digunakan.
- Gambar spesies ikan yang diprediksi.

## Instalasi

1. **Clone repositori ini:**

   ```bash
   git clone https://github.com/deliasaniark/app-predict-fish.git
   cd app-predict-fish
   ```

2. **Buat dan aktifkan lingkungan virtual (opsional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Di Windows gunakan `venv\Scripts\activate`
   ```

3. **Instal dependensi:**

   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Aplikasi

1. **Jalankan aplikasi Streamlit:**

   ```bash
   streamlit run app.py
   ```

2. **Akses aplikasi di browser:**

   Buka `http://localhost:8501` di browser Anda.

## Struktur Proyek

- `app.py`: Skrip utama untuk menjalankan aplikasi Streamlit.
- `models/`: Direktori yang berisi model yang telah dilatih dan komponen terkait.
- `images/`: Direktori yang berisi gambar spesies ikan.
- `notebook/rf.ipynb`: Notebook Jupyter yang digunakan untuk melatih dan mengevaluasi model Random Forest.
- `Dockerfile`: File untuk membangun image Docker.
- `Procfile`: File konfigurasi untuk deployment di platform seperti Heroku atau Railway.
- `requirements.txt`: File yang berisi semua dependensi yang diperlukan untuk aplikasi ini.

## Deployment

Aplikasi ini dapat dideploy menggunakan Docker. Gunakan `Dockerfile` yang disediakan untuk membangun image dan menjalankan container.
