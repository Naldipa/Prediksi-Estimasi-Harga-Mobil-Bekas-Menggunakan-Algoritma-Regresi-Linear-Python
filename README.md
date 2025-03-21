# Prediksi-Estimasi-Harga-Mobil-Bekas-Menggunakan-Algoritma-Regresi-Linear-Python

# Estimasi Harga Mobil Bekas Menggunakan Algoritma Regresi Linier dengan Python

<img width="559" alt="image" src="https://github.com/user-attachments/assets/979145bc-3e12-4ef3-b599-a4c52441bfe1" />

## Deskripsi Proyek

Proyek ini bertujuan untuk mengembangkan sistem prediksi harga mobil bekas menggunakan algoritma **Regresi Linier** dengan bahasa pemrograman **Python**. Sistem ini dirancang untuk membantu konsumen dan penjual mobil bekas dalam menentukan harga yang akurat, objektif, dan efisien berdasarkan faktor-faktor seperti tahun produksi, jarak tempuh, pajak, konsumsi bahan bakar (MPG), dan ukuran mesin.

Dengan memanfaatkan dataset publik dari **Kaggle**, proyek ini melakukan analisis data, pembersihan data, dan visualisasi untuk memahami pola dan hubungan antar variabel. Model regresi linier kemudian dilatih untuk memprediksi harga mobil bekas berdasarkan fitur-fitur yang relevan.

## Fitur Utama

- **Prediksi Harga Mobil Bekas**: Sistem dapat memprediksi harga mobil bekas berdasarkan input pengguna seperti tahun produksi, jarak tempuh, pajak, konsumsi bahan bakar, dan ukuran mesin.
- **Visualisasi Data**: Proyek ini menggunakan **Matplotlib** dan **Seaborn** untuk menampilkan visualisasi data seperti heatmap korelasi, histogram distribusi, dan diagram batang.
- **Antarmuka Pengguna**: Aplikasi web sederhana dibangun menggunakan **Streamlit** untuk memungkinkan pengguna memasukkan data mobil dan mendapatkan estimasi harga secara langsung.
- **Penyimpanan Model**: Model regresi linier yang telah dilatih disimpan menggunakan **Pickle** untuk memudahkan penggunaan ulang tanpa perlu melatih ulang model.

## Teknologi yang Digunakan

- **Bahasa Pemrograman**: Python
- **Library Python**:
  - **NumPy**: Untuk operasi matematika dan manipulasi array.
  - **Pandas**: Untuk manipulasi dan analisis data.
  - **Scikit-Learn**: Untuk implementasi algoritma regresi linier dan evaluasi model.
  - **Matplotlib/Seaborn**: Untuk visualisasi data.
- **IDE**: Jupyter Notebook, PyCharm
- **Framework Web**: Streamlit
- **Penyimpanan Model**: Pickle

## Dataset

Dataset yang digunakan dalam proyek ini diperoleh dari **Kaggle** dan berisi informasi tentang mobil bekas, termasuk:
- **Model**: Jenis atau seri mobil.
- **Year**: Tahun produksi mobil.
- **Mileage**: Jarak tempuh mobil.
- **Tax**: Pajak kendaraan.
- **MPG (Miles Per Gallon)**: Efisiensi bahan bakar.
- **Engine Size**: Ukuran mesin mobil.
- **Price**: Harga aktual mobil (variabel target).

Link dataset: [Used Car Dataset - Kaggle](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes)

## Cara Menggunakan

1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/Prediksi-Estimasi-Harga-Mobil-Bekas-Menggunakan-Algoritma-Regresi-Linear-Python.git
   cd repository-name
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi Streamlit**:
   ```bash
   python -m streamlit run estimasi_harga_mobil_bekas.py
   ```

4. **Masukkan Data Mobil**:
   - Masukkan informasi mobil seperti tahun, jarak tempuh, pajak, konsumsi bahan bakar, dan ukuran mesin.
   - Klik tombol "Estimasi Harga" untuk mendapatkan prediksi harga mobil bekas.

## Hasil dan Pembahasan

Model regresi linier yang dikembangkan memiliki akurasi sebesar **64.22%** dalam memprediksi harga mobil bekas. Visualisasi data seperti heatmap korelasi dan histogram distribusi membantu dalam memahami pola data dan hubungan antar variabel. Aplikasi web yang dibangun menggunakan Streamlit memberikan pengalaman pengguna yang interaktif dan mudah digunakan.

## Revisi yang Disarankan

1. **Masalah Nominal Pajak**: Menyesuaikan nominal pajak dalam bentuk Rupiah.
2. **Penghapusan Tahun Mobil 1900-an**: Menghapus data mobil dengan tahun produksi 1900-an yang tidak relevan.
3. **Output dalam Juta Rupiah**: Menghapus output dalam bentuk Rupiah yang terlalu besar dan menggantinya dengan format yang lebih mudah dibaca.

## Kontribusi

Proyek ini dikembangkan oleh tim mahasiswa Universitas Esa Unggul:
- Naldi Pradipta
- Muhammad Sakha Al Gazali
- Ilham Bayu Pratama
- Dendi Fathir Muhammad
- Iqbal Maulana
- Daffa Jenaro
- Joy Face Herodian

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

Dengan proyek ini, diharapkan dapat memberikan manfaat bagi konsumen dan penjual mobil bekas dalam menentukan harga yang akurat dan objektif. Selamat mencoba! 🚗💨
