import streamlit as st
from PIL import Image

st.title('Yakiniku')

uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg'])

if uploaded_file is not None: #noneがnot、つまり変数に何も入ってなかったら実行
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    