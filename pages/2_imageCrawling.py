from google_images_download import google_images_download   
import streamlit as st
import pandas as pd
import random
from string import ascii_uppercase

st.set_page_config(
    page_title= "이미지 크롤링",
    layout="wide",
)
a = str(input("월하는 이미지를 기입하시오:"))

response = google_images_download.googleimagesdownload()  
arguments = {"keywords": a, "limit": 20, "print_urls": True, "format": "jpg"}   
paths = response.download(arguments)   
print(paths)
