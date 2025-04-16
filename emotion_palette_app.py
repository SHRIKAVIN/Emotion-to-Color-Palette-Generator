import streamlit as st
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import tempfile
import os

# Set the page configuration for better UI
st.set_page_config(page_title="Emotion-to-Color Palette Generator", layout="wide")

# Set custom styling for a clean design
st.markdown("""
    <style>
        .css-1v3fvcr { 
            text-align: center;
        }
        .css-1dp5r7m { 
            background-color: #F0F4F8; 
        }
        .stButton>button {
            background-color: #FF8C00;
            color: white;
            font-size: 18px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #FF6A00;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎭 Emotion-to-Color Palette Generator")
st.markdown("Upload an image or use your webcam to detect your emotion, generate a matching color palette, and get a bonus **Spotify playlist** based on your mood! 🎶")

# Emotion to color + Spotify map
emotion_data = {
    "happy": {
        "colors": ['#FFE066', '#FFB703', '#FF8C00'],
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"
    },
    "sad": {
        "colors": ['#26547C', '#3B9C9C', '#4B6587'],
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWVV27DiNWxkR"
    },
    "angry": {
        "colors": ['#D7263D', '#FF5733', '#900C3F'],
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWXnscMH24yOc"
    },
    "surprise": {
        "colors": ['#FFD700', '#FFDD00', '#E7C547'],
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX2pSTOxoPbx9"
    },
    "neutral": {
        "colors": ['#A9A9A9', '#B0BEC5', '#CFD8DC'],
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6"
    },
    "fear": {
        "colors": ['#6A0572', '#AB83A1', '#A239CA'],
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWZwtERXCS82H"
    },
    "disgust": {
        "colors": ['#556B2F', '#6B8E23', '#8FBC8F'],
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWWzVPEmatsUB"
    }
}

# Let the user choose to upload or use the webcam
option = st.radio("Select an option", ('Upload Image', 'Use Webcam'))

# Initialize image path
img_path = None

if option == 'Upload Image':
    uploaded_file = st.file_uploader("📁 Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        img_path = os.path.join(tempfile.gettempdir(), uploaded_file.name)
        with open(img_path, "wb") as f:
            f.write(uploaded_file.read())
        st.image(img_path, caption="Uploaded Image", use_container_width=True)

elif option == 'Use Webcam':
    camera_image = st.camera_input("📷 Take a selfie with your webcam")
    if camera_image:
        img_path = os.path.join(tempfile.gettempdir(), "webcam.jpg")
        with open(img_path, "wb") as f:
            f.write(camera_image.getbuffer())
        st.image(img_path, caption="Webcam Capture", use_container_width=True)

# Function to display the color palette
def display_palette_for_emotion(emotion):
    colors = emotion_data.get(emotion, {}).get('colors', ['#FFFFFF'])
    spotify_link = emotion_data.get(emotion, {}).get('spotify', None)

    st.markdown(f"### 🎨 Your Mood Palette")
    
    fig, ax = plt.subplots(figsize=(6, 1))
    for i, color in enumerate(colors):
        ax.fill_between([i, i + 1], 0, 1, color=color)
    ax.set_xticks([])
    ax.set_yticks([])
    st.pyplot(fig)

    if spotify_link:
        st.markdown(f"### 🎧 Spotify Playlist")
        st.markdown(f"[Open Playlist]({spotify_link})")

# Function to detect emotion from an image
def detect_emotion_from_image(img_path):
    try:
        result = DeepFace.analyze(img_path=img_path, actions=["emotion"], enforce_detection=True)
        return result
    except Exception as e:
        st.error("No face detected. Please upload a clear image or take a selfie where your face is visible.")
        return None

# Detect emotion and display results
if img_path:
    with st.spinner("Analyzing your emotion..."):
        result = detect_emotion_from_image(img_path)
        if result:  # If face is detected
            emotion = result[0]['dominant_emotion'].lower()
            st.success(f"🎯 Detected Emotion: **{emotion.capitalize()}**")
            # Display the corresponding color palette and Spotify link
            display_palette_for_emotion(emotion)
