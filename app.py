import streamlit as st
import requests
from PIL import Image
import io

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/remove-bg/"

st.title("Image Background Remover")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Convert image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Send image to FastAPI backend
    with st.spinner("Removing background..."):
        response = requests.post(API_URL, files={"file": ("image.png", img_byte_arr, "image/png")})

        if response.status_code == 200:
            output_img = Image.open(io.BytesIO(response.content))
            st.image(output_img, caption="Background Removed", use_column_width=True)

            # Provide download option
            buf = io.BytesIO()
            output_img.save(buf, format='PNG')
            st.download_button("Download Processed Image", buf.getvalue(), file_name="no_bg.png", mime="image/png")
        else:
            st.error("Failed to process image. Try again.")
