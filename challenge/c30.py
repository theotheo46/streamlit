import streamlit as st
import os
import base64

# Функция для сохранения загруженного файла
def save_uploaded_file(uploaded_file):
    folder = "uploaded_files"
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path

# Функция для создания ссылки для скачивания
def create_download_link(file_path):
    with open(file_path, "rb") as f:
        file_data = f.read()
    b64 = base64.b64encode(file_data).decode()
    file_name = os.path.basename(file_path)
    href = f'<a href="data:file/octet-stream;base64,{b64}" download="{file_name}">Скачать {file_name}</a>'
    return href

# Интерфейс Streamlit
st.title("Загрузка и скачивание файла")

# Кнопка для загрузки файла
uploaded_file = st.file_uploader("Выберите файл для загрузки")

if uploaded_file is not None:
    # Сохранение файла
    file_path = save_uploaded_file(uploaded_file)

    st.success(f"Файл {uploaded_file.name} успешно загружен!")

    # Отображение ссылки для скачивания
    st.markdown(create_download_link(file_path), unsafe_allow_html=True)
