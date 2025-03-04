import streamlit as st
import pandas as pd
from utils.mock_data import get_mock_prices
from utils.visualization import plot_price_trend
from googletrans import Translator
from gtts import gTTS
import base64
import os

# Function to encode local image to Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded_string}"

def set_background(image_path):
    base64_image = get_base64_image(image_path)
    background_css = f"""
    <style>
    .stApp {{
        background-image: url("{base64_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)

def translate_to_telugu(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='te')
    return translated.text

def text_to_speech(text, lang='te'):
    tts = gTTS(text=text, lang=lang)
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file

# App title and description
st.title("Crop Market Price Alerts")
st.image("images\logo.png", width=100)
st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <h2>Stay informed with market prices to maximize profit</h2>
    </div>
""", unsafe_allow_html=True)

# User input
crop = st.text_input("Enter the crop name (e.g., Wheat, Rice):")
region = st.text_input("Enter your region (optional):")

if st.button("Get Prices"):
    if crop.strip():
        with st.spinner("Fetching data..."):
            data = get_mock_prices(crop, region)
            if data and "error" not in data:
                # Display data
                df = pd.DataFrame(data["prices"])
                st.table(df)
                st.plotly_chart(plot_price_trend(df, crop))

                # Generate voice output
                output_text = f"Here are the market prices for {crop}. Please check the table and graph for more details."
                telugu_translation = translate_to_telugu(output_text)
                st.write(f"**Translation (Telugu):** {telugu_translation}")

                # Convert translated text to speech
                audio_file = text_to_speech(telugu_translation)
                audio_bytes = open(audio_file, "rb").read()
                st.audio(audio_bytes, format="audio/mp3", start_time=0)
                os.remove(audio_file)  # Clean up
            else:
                error_message = data.get("error", "No data available for the selected crop.")
                st.error(error_message)

                # Voice assistant for errors
                telugu_translation = translate_to_telugu(error_message)
                st.write(f"**Translation (Telugu):** {telugu_translation}")

                # Convert error message to speech
                audio_file = text_to_speech(telugu_translation)
                audio_bytes = open(audio_file, "rb").read()
                st.audio(audio_bytes, format="audio/mp3", start_time=0)
                os.remove(audio_file)  # Clean up
    else:
        st.error("Please enter a crop name.")
        # Voice assistant for missing input
        telugu_translation = translate_to_telugu("Please enter a crop name.")
        st.write(f"**Translation (Telugu):** {telugu_translation}")

        # Convert message to speech
        audio_file = text_to_speech(telugu_translation)
        audio_bytes = open(audio_file, "rb").read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        os.remove(audio_file)  # Clean up

# Set background image
set_background("images\Home_Bg.jpg") 

# Footer
st.markdown("---")
st.markdown(
    "🌟 **Developed by AI Hackathon Team** | 💡 [Contact Us](mailto:shivakumarsouta18@gmail.com) | 📢 [GitHub Repo](https://github.com/shivkumars005)"
)
