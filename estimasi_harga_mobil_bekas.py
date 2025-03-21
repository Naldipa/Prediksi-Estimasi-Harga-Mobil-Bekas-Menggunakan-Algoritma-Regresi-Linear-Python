import pickle
import streamlit as st
import pandas as pd
from datetime import datetime

# Memuat model yang disimpan
model = pickle.load(open('mobil_price_prediction_model.sav', 'rb'))

# Membuat judul web
st.title('Estimasi Harga Mobil Bekas BMW yang Lebih Akurat')

# Membuat formulir input
year = st.number_input('Tahun Mobil', min_value=2000, max_value=2023)
mileage = st.number_input('Kilometer Mobil', min_value=0)
condition = st.selectbox('Kondisi Mobil', ['Baru', 'Bekas', 'Bekas (Bagus)'])
variant = st.selectbox('Varian', ['Z3', 'M6', 'i8', 'M2', 'M3', 'M5', '8 Series', 'i3', 'X7', '7 Series', 'X6', 'Z4', '6 Series', 'M4', 'X4', 'X2', 'X5', 'X3', 'X1', '4 Series', '5 Series', '2 Series', '1 Series', '3 Series'])
transmission = st.selectbox('Transmisi', ['Automatic', 'Manual'])
fuelType = st.selectbox('Tipe Bahan Bakar', ['Petrol', 'Diesel'])
tax = st.number_input('Pajak (per tahun)', min_value=0)
mpg = st.number_input('Efisiensi Bahan Bakar (MPG)', min_value=0.0)
engineSize = st.number_input('Ukuran Mesin (Liter)', min_value=0.0)
location = st.selectbox('Lokasi', ['Jakarta', 'Bandung', 'Surabaya'])
purchase_date = st.date_input('Tanggal Pembelian')

# Memproses data input sebelum membuat prediksi
if st.button('Estimasi Harga'):
    # Membuat DataFrame untuk input model
    data = pd.DataFrame({
        'year': [year],
        'mileage': [mileage],
        'condition': [condition],
        'variant': [variant],
        'transmission': [transmission],
        'fuelType': [fuelType],
        'tax': [tax],
        'mpg': [mpg],
        'engineSize': [engineSize],
        'location': [location],
        'purchase_date': [purchase_date]
    })

    ### **1️⃣ Mengonversi Tanggal ke Format Numerik**
    data['purchase_date'] = pd.to_datetime(data['purchase_date'])
    data['purchase_days'] = (data['purchase_date'] - datetime(2000, 1, 1)).dt.days
    data.drop(columns=['purchase_date'], inplace=True)

    ### **2️⃣ One-Hot Encoding untuk Data Kategorikal (Termasuk `variant`)**
    categorical_features = ['condition', 'variant', 'transmission', 'fuelType', 'location']
    data = pd.get_dummies(data, columns=categorical_features, drop_first=True)

    ### **3️⃣ Mengisi Data yang Hilang dengan Median**
    data.fillna(data.median(), inplace=True)

    ### **4️⃣ Memastikan Semua Kolom Sesuai dengan Model**
    required_columns = list(model.feature_names_in_)
    for col in required_columns:
        if col not in data.columns:
            data[col] = 0  # Tambahkan kolom yang hilang dengan nilai 0

    # Urutkan kolom agar sesuai dengan input model
    data = data.reindex(columns=model.feature_names_in_, fill_value=0)

    ### **5️⃣ Prediksi Harga**
    try:
        predicted_price = model.predict(data)[0]  # Mendapatkan harga prediksi dalam Pound Sterling
        
        # Konversi dari Pound Sterling ke Rupiah (1 Pound = Rp 19.500)
        price_rupiah = predicted_price * 19500
        
        # Konversi ke format juta Rupiah
        price_juta = price_rupiah / 1000000
        
        # Konversi dari Pound Sterling ke Dollar (1 Pound = 1.27 USD)
        price_dollar = predicted_price * 1.27

        # Menampilkan hasil dengan format yang lebih rapi
        st.write(f'Estimasi Harga Mobil Bekas: Rp {price_rupiah:,.2f}')
        st.write(f'Dalam Dollar: ${price_dollar:,.2f}')
        st.write(f'Pajak yang Dimasukkan: Rp {tax:,.0f}')
    except Exception as e:
        st.error(f"Terjadi kesalahan selama prediksi: {e}")
