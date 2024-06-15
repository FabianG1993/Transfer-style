import streamlit as st
from PIL import Image
import numpy as np
import os
from transfer_style import transfer_style

# Función para guardar la imagen resultante
def save_image(image, path):
    Image.fromarray(image).save(path)

# Definir los estilos disponibles
styles = {
    'Monet': 'D:\Transfer Style\styles\Monet.jpg',
    'Da Vinci': 'D:\Transfer Style\styles\Da vinci.jpg',
    'Van Gogh': 'D:\Transfer Style\styles\Van gogh.jpg'
}

# Título de la app
st.title("Transferencia de Estilo")

# Subida de imagen
uploaded_file = st.file_uploader("Elige una imagen...", type="jpg")

# Selección del estilo
style = st.selectbox("Selecciona un estilo:", list(styles.keys()))

# Iteraciones
iterations = st.slider("Número de iteraciones:", min_value=3, max_value=50, value=20)

# Tamaño de la imagen
img_height = st.slider("Altura de la imagen procesada:", min_value=200, max_value=800, value=400)

if uploaded_file is not None:
    # Mostrar la imagen cargada
    st.image(uploaded_file, caption='Imagen Cargada', use_column_width=True)
    
    # Guardar la imagen subida
    target_image_path = "target_image.jpg"
    with open(target_image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    style_image_path = styles[style]

    if st.button("Aplicar Transferencia de Estilo"):
        with st.spinner("Procesando..."):
            result_img = transfer_style(target_image_path, style_image_path, iterations, img_height)
            result_path = "result_image.jpg"
            save_image(result_img, result_path)
        
        st.image(result_path, caption='Imagen Generada', use_column_width=True)
