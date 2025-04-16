# Emotion-to-Color Palette Generator 🎨

# **AI-Powered Emotion Detection and Color Palette Creation**


# **📌 Project Overview**
Emotion-to-Color Palette Generator is an interactive web application that detects emotions from images or webcam captures using AI and generates a matching color palette. It also suggests a Spotify playlist based on the detected emotion, creating a unique and engaging user experience.  


# **🔥 Features**

✅ Emotion Detection: Detects dominant emotions (Happy, Sad, Angry, etc.) from uploaded images or webcam snapshots.  
✅ Color Palette Generator: Creates a color palette based on the detected emotion.  
✅ Spotify Playlist Suggestions: Provides a curated Spotify playlist link matching the detected mood.  
✅ Single Snapshot Webcam Capture: Captures a single image without continuous looping for simplicity.  
✅ User-Friendly Interface: Built with Streamlit for seamless interaction.


# **🏗️ Tech Stack**

Frontend: Streamlit  
AI Model: DeepFace (Emotion Recognition)  
Image Processing: OpenCV  
Visualization: Matplotlib  
API Integration: Spotify API


**🚀 Installation & Setup**

1️⃣ Clone the Repository

```bash
git clone https://github.com/SHRIKAVIN/emotion-color-palette-generator.git
```
```bash
cd emotion-color-palette-generator
```
2️⃣ Install Dependencies

Ensure you have Python 3.7+ installed, then run:  
```bash
pip install -r requirements.txt
```

3️⃣ Run the Application
Start the Streamlit app with:  
```bash
streamlit run emotion_palette_app.py
```

4️⃣ Access the Web App
Once the server is running, open your browser and go to:  
```bash
http://localhost:8501
```

# **📌 Usage**
1️⃣ Upload an Image or Use Webcam: Choose to upload an image or allow webcam access for a snapshot.
2️⃣ Emotion Detection: The app analyzes the image and detects the dominant emotion.
3️⃣ View Results: A color palette and a Spotify playlist link are displayed based on the detected emotion.  

# **🔧 How it Works**

Emotion Detection: DeepFace analyzes the image or webcam snapshot to identify the dominant emotion.  
Color Palette Generation: Predefined colors mapped to emotions are used to create a palette, displayed via Matplotlib.  
Spotify Playlist Suggestions: A curated Spotify playlist link is provided based on the detected emotion.  
Webcam Mode: Captures a single image for analysis, ensuring a lightweight and efficient process.


# **📜 License**
This project is licensed under the MIT License - see the LICENSE file for details.
