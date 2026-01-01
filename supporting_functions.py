import re
import streamlit as st
import time
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

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

def get_transcript(video_id, language):
    ytt_api= YouTubeTranscriptApi()
    try:
        transcript= ytt_api.fetch(video_id, languages=[language])
        full_transcript= " ".join([i.text for i in transcript])
        time.sleep(10)
        return full_transcript
    except Exception as e:
        st.error(f"Error fething video {e}")


