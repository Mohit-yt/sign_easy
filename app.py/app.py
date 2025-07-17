import streamlit as st
from PIL import Image
import time
import os

# Simple list of sign image paths
sign_paths = ["signs/I.gif", "signs/YOU.gif", "signs/GO.gif"]

st.title("Sign Language Visualizer")

if st.button("▶️ Start Showing Signs"):
    for path in sign_paths:
        if os.path.exists(path):
            img = Image.open(path)
            st.image(img, caption=os.path.basename(path))
            time.sleep(1)
        else:
            st.error(f"File not found: {path}")
