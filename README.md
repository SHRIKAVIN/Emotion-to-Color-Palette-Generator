🎭 Emotion-to-Color Palette Generator

An interactive web application built using Streamlit, DeepFace, and OpenCV that detects emotions from images or webcam captures and generates a matching color palette. The app also suggests a Spotify playlist based on the detected emotion.

⸻

📖 Table of Contents
	•	Features
	•	Installation
	•	Usage
	•	How it Works
	•	Technologies Used
	•	License

⸻

✨ Features
	•	Emotion Detection: Detects dominant emotions from uploaded images or webcam captures.
	•	Color Palette Generator: Generates a color palette that corresponds to the detected emotion (Happy, Sad, Angry, etc.).
	•	Spotify Playlist Suggestions: Provides a Spotify playlist link based on the detected emotion.
	•	No Continuous Loop: Captures a single image from the webcam without looping, making it simpler to use.

⸻

🛠️ Installation

To get started with this project, follow these steps:

 1.	Clone the Repository:
 git clone https://github.com/yourusername/emotion-color-palette-generator.git

	2.	Navigate to the project directory:
 cd emotion-color-palette-generator

 	3.	Install Dependencies:
Make sure you have Python 3.7+ installed. Then, install the required dependencies using pip:

pip install -r requirements.txt

⸻

🏃‍♂️ Usage
	1.	Run the App:
After the dependencies are installed, run the Streamlit app:
streamlit run emotion_palette_app.py

2.	Interact with the App:
	•	You can either upload an image or use your webcam to detect emotions.
	•	Once the emotion is detected, a color palette and a related Spotify playlist will be displayed.

⸻

🔧 How it Works
	1.	Emotion Detection:
	•	The app uses the DeepFace library to analyze the uploaded image or webcam snapshot and detect the dominant emotion (Happy, Sad, Angry, etc.).
	2.	Color Palette Generation:
	•	Based on the detected emotion, a color palette is generated using predefined colors mapped to each emotion. The app uses Matplotlib to create and display the palette.
	3.	Spotify Playlist Suggestions:
	•	A Spotify playlist related to the detected emotion is displayed as a link. Clicking the link opens a playlist curated for that mood.
	4.	Real-Time Emotion Detection (Webcam Mode):
	•	When using the webcam, the app takes a single snapshot and performs emotion detection on that image, showing the result immediately.

⸻

💻 Technologies Used
	•	Streamlit: Framework for building the interactive web app.
	•	DeepFace: Used for emotion recognition from images.
	•	OpenCV: For webcam handling and image processing.
	•	Matplotlib: For generating and displaying color palettes.
	•	Spotify API: For generating mood-based playlists.

