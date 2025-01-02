import streamlit as st
import numpy as np
import pickle
from PIL import Image

# Konfigurasi halaman
def setup_page():
    st.set_page_config(
        page_title="Prediksi Jenis Ikan",
        page_icon="🐟",
        layout="centered"
    )

# Load model dan komponen terkait
@st.cache_resource
def load_models():
    model = pickle.load(open('models/random_forest_model.pkl', 'rb'))
    scaler = pickle.load(open('models/scaler.pkl', 'rb'))
    label_encoder = pickle.load(open('models/label_encoder.pkl', 'rb'))
    return model, scaler, label_encoder

# Fungsi untuk memuat gambar ikan
def get_fish_image(species):
    try:
        image_path = f"images/{species.replace(' ', '_')}.jpeg"
        return Image.open(image_path)
    except:
        return None

# Fungsi untuk input data
def get_user_input():
    col1, col2 = st.columns(2)
    with col1:
        length = st.number_input(
            "Panjang Ikan (cm)", 
            min_value=6.36, 
            max_value=33.86, 
            value=10.0
        )
    with col2:
        weight = st.number_input(
            "Berat Ikan (kg)", 
            min_value=2.05, 
            max_value=6.29, 
            value=3.0
        )
    return length, weight

# Fungsi untuk menghitung rasio
def calculate_wl_ratio(length, weight):
    return weight / length if length > 0 else 0

# Fungsi untuk melakukan prediksi
def make_prediction(features, model, scaler, label_encoder):
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)
    return label_encoder.inverse_transform(prediction)[0]

# Fungsi untuk menampilkan hasil
def show_prediction(species):
    st.success(f"Ikan ini diprediksi sebagai spesies: **{species}**")
    fish_image = get_fish_image(species)
    if fish_image:
        st.image(fish_image, caption=f"Gambar Ikan {species}")
    else:
        st.warning("Maaf, gambar untuk spesies ini tidak tersedia")

# Fungsi untuk menampilkan informasi model
def show_model_info():
    with st.expander("ℹ️ Informasi Model"):
        st.write("""
        Model ini menggunakan Random Forest Classifier untuk memprediksi jenis ikan berdasarkan:
        - Panjang ikan (cm)     [6.36 - 33.86]
        - Berat ikan (kg)       [2.05 - 6.29]
        - Rasio berat/panjang   [0.08 - 0.64]
        """)

# Footer
def show_footer():
    st.markdown(
        """
        ---
        <div style='text-align: center'>
        Delia Saniar Komalasari | NPM: 2213020145
        </div>
        """, unsafe_allow_html=True)

def main():
    # Setup awal
    setup_page()
    model, scaler, label_encoder = load_models()
    
    # Tampilan utama
    st.title("🐟 Aplikasi Prediksi Jenis Ikan")
    st.write("Masukkan data pengukuran ikan untuk memprediksi jenisnya")
    
    # Input dan kalkulasi
    length, weight = get_user_input()
    ratio = calculate_wl_ratio(length, weight)
    st.info(f"Rasio Berat/Panjang: {ratio:.2f}")
    
    # Prediksi
    if st.button("Prediksi Jenis Ikan"):
        input_data = np.array([[length, weight, ratio]])
        species = make_prediction(input_data, model, scaler, label_encoder)
        show_prediction(species)

    show_model_info()
    
    show_footer()

if __name__ == "__main__":
    main()
