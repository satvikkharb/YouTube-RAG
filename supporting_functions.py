import re
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def extract_video_id_url(url):
    """
    Extracts video id from a valid Youtube URL link
    """
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if match:
        return match.group(1)
    st.error("Invalid YouTube URL. Please provide a valid YouTube URL")
    return None

print(extract_video_id_url("https://www.youtube.com/watch?v=_yoNnoVk4gc"))
