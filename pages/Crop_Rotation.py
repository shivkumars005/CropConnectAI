import streamlit as st
from utils.tips import get_rotation_tips
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

# Page Title
st.title("Crop Rotation Tips")
st.write(
    "Improve soil health and maximize yield with effective crop rotation practices. "
    "Enter your current crop and region to get personalized recommendations."
)

# User Inputs
crop = st.text_input("Enter your current crop", placeholder="E.g., Wheat, Rice, Corn")
region = st.selectbox(
    "Select your region",
    ["North America", "South Asia", "Europe", "Africa", "Other"],
    help="Choose your region for tailored tips."
)

# Display Rotation Tips
if crop:
    tips = get_rotation_tips(crop, region)
    if tips and isinstance(tips, dict):
        try:
            # Extract rotation tips safely
            primary = tips.get('primary', "No primary recommendation available")
            alternatives = tips.get('alternatives', [])
            region_tip = tips.get('region_tip', "No region-specific advice available")
            
            st.subheader(f"Recommended Crop Rotation for {crop}")
            tips_text = f"""
            Primary Recommendation: Rotate your crop with {primary} to enhance soil fertility and break pest cycles.
            Additional Suggestions:
            Alternative Crops: {', '.join(alternatives) if alternatives else 'None'}
            Region-Specific Advice: {region_tip}
            """
            st.markdown(
                f"""
                ### 🌾 **Primary Recommendation**
                Rotate your crop with **{primary}** to enhance soil fertility and break pest cycles.
                
                ### 🌱 **Additional Suggestions**
                - **Alternative Crops:** {', '.join(alternatives) if alternatives else 'None'}
                - **Region-Specific Advice:** {region_tip}
                """
            )
            
            # Visualize Crop Rotation as a Cycle
            st.subheader("Crop Rotation Plan")
            if alternatives:
                rotation_plan = [crop] + alternatives[:2]  # Limit to two alternatives
                st.graphviz_chart(f"""
                digraph {{
                    {' -> '.join(rotation_plan + [crop])};
                }}
                """)
            else:
                st.warning("No alternative crops available to visualize a rotation plan.")
            
            # Translate and speak out tips
            telugu_translation = translate_to_telugu(tips_text)
            st.write(f"**Translation (Telugu):** {telugu_translation}")
            audio_file = text_to_speech(telugu_translation)
            audio_bytes = open(audio_file, "rb").read()
            st.audio(audio_bytes, format="audio/mp3", start_time=0)
            os.remove(audio_file)  # Clean up
        except Exception as e:
            error_message = f"An error occurred while displaying tips: {e}"
            st.error(error_message)

            # Translate and speak error
            telugu_translation = translate_to_telugu(error_message)
            st.write(f"**Translation (Telugu):** {telugu_translation}")
            audio_file = text_to_speech(telugu_translation)
            audio_bytes = open(audio_file, "rb").read()
            st.audio(audio_bytes, format="audio/mp3", start_time=0)
            os.remove(audio_file)  # Clean up
    else:
        warning_message = f"No specific tips are available for **{crop}** in the selected region."
        st.warning(warning_message)

        # Translate and speak warning
        telugu_translation = translate_to_telugu(warning_message)
        st.write(f"**Translation (Telugu):** {telugu_translation}")
        audio_file = text_to_speech(telugu_translation)
        audio_bytes = open(audio_file, "rb").read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        os.remove(audio_file)  # Clean up
else:
    info_message = "Please enter your crop to see tailored recommendations."
    st.info(info_message)

    # Translate and speak info
    telugu_translation = translate_to_telugu(info_message)
    st.write(f"**Translation (Telugu):** {telugu_translation}")
    audio_file = text_to_speech(telugu_translation)
    audio_bytes = open(audio_file, "rb").read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
    os.remove(audio_file)  # Clean up

# Expandable Section for General Guidelines
with st.expander("🌍 General Guidelines for Crop Rotation"):
    st.markdown(
        """
        - Alternate between crops that consume a lot of nitrogen (e.g., cereals) and those that replenish nitrogen (e.g., legumes).
        - Avoid planting the same crop family consecutively to reduce the risk of pests and diseases.
        - Incorporate cover crops like clover or rye to suppress weeds and improve soil health.
        - Diversify crop selection to encourage biodiversity and long-term sustainability.
        """
    )

# Set background image
set_background("Crop_Rot_Bg.jpg")

# Footer
st.markdown("---")
st.markdown("🌟 **Tip:** Combine crop rotation with organic farming for the best results!")
