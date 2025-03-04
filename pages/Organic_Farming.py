import streamlit as st
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

# Page Configuration
st.set_page_config(page_title="Organic Farming Tips", page_icon="🌿")

# Title and Description
st.title("Organic Farming Tips")
st.write(
    "Explore practical techniques to improve your farming methods using sustainable, eco-friendly practices."
)

# User Input: Select Category
categories = ["General Tips", "Pest Control", "Soil Health", "Composting"]
selected_category = st.selectbox("Choose a category to explore tips:", categories)

# Define Tips by Category
organic_tips = {
    "General Tips": [
        "Practice crop rotation to maintain soil fertility.",
        "Grow cover crops to suppress weeds and reduce soil erosion.",
        "Avoid synthetic fertilizers and use organic alternatives.",
        "Encourage biodiversity by planting native species."
    ],
    "Pest Control": [
        "Use neem oil or garlic spray as natural pest repellents.",
        "Introduce beneficial insects like ladybugs to control aphids.",
        "Plant marigolds to deter nematodes in the soil.",
        "Rotate crops to break pest life cycles."
    ],
    "Soil Health": [
        "Add compost and organic manure to enrich the soil.",
        "Test soil pH regularly and adjust with lime or sulfur if needed.",
        "Use green manure (cover crops) to boost nitrogen content.",
        "Avoid over-tilling to prevent soil compaction."
    ],
    "Composting": [
        "Layer green (nitrogen-rich) and brown (carbon-rich) materials in the compost.",
        "Keep the compost pile moist but not waterlogged.",
        "Turn the compost regularly to aerate and speed up decomposition.",
        "Avoid adding meat, dairy, or oily foods to the compost."
    ],
}

# Display Tips for Selected Category
st.subheader(f"Tips for {selected_category}")
tips_to_display = organic_tips[selected_category]
for tip in tips_to_display:
    st.write(f"• {tip}")

# Translate and speak tips
if st.button(f"Read Tips in Telugu for {selected_category}"):
    tips_text = " ".join(tips_to_display)
    telugu_translation = translate_to_telugu(tips_text)
    st.write(f"**Translation (Telugu):** {telugu_translation}")
    audio_file = text_to_speech(telugu_translation)
    audio_bytes = open(audio_file, "rb").read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
    os.remove(audio_file)  # Clean up

# Expandable Sections for Additional Details
st.markdown("### Additional Resources")
with st.expander("What is Organic Farming?"):
    content = (
        "Organic farming avoids synthetic chemicals and emphasizes sustainable techniques. "
        "This includes crop rotation, composting, and the use of natural pest controls."
    )
    st.write(content)

    if st.button("Read Explanation in Telugu"):
        telugu_translation = translate_to_telugu(content)
        st.write(f"**Translation (Telugu):** {telugu_translation}")
        audio_file = text_to_speech(telugu_translation)
        audio_bytes = open(audio_file, "rb").read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        os.remove(audio_file)  # Clean up

with st.expander("How to Start Composting"):
    content = (
        "Start by creating a compost pile or bin. Add green materials (like vegetable scraps) and brown materials "
        "(like dry leaves). Keep the pile moist and turn it regularly to speed up decomposition."
    )
    st.write(content)

    if st.button("Read Composting Tips in Telugu"):
        telugu_translation = translate_to_telugu(content)
        st.write(f"**Translation (Telugu):** {telugu_translation}")
        audio_file = text_to_speech(telugu_translation)
        audio_bytes = open(audio_file, "rb").read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        os.remove(audio_file)  # Clean up

with st.expander("Pest Control Methods"):
    content = (
        "Natural pest control methods include:\n"
        "- Using natural repellents like neem oil.\n"
        "- Encouraging beneficial insects like ladybugs.\n"
        "- Planting pest-repelling crops like marigolds."
    )
    st.write(content)

    if st.button("Read Pest Control Methods in Telugu"):
        telugu_translation = translate_to_telugu(content)
        st.write(f"**Translation (Telugu):** {telugu_translation}")
        audio_file = text_to_speech(telugu_translation)
        audio_bytes = open(audio_file, "rb").read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        os.remove(audio_file)  # Clean up

# Search Bar for Tips
st.markdown("### Search Organic Farming Techniques")
search_query = st.text_input("Search for a specific technique or tip:")
if search_query:
    matching_tips = [
        tip for tips in organic_tips.values() for tip in tips if search_query.lower() in tip.lower()
    ]
    if matching_tips:
        st.write("### Search Results:")
        for tip in matching_tips:
            st.write(f"• {tip}")

        if st.button("Read Search Results in Telugu"):
            tips_text = " ".join(matching_tips)
            telugu_translation = translate_to_telugu(tips_text)
            st.write(f"**Translation (Telugu):** {telugu_translation}")
            audio_file = text_to_speech(telugu_translation)
            audio_bytes = open(audio_file, "rb").read()
            st.audio(audio_bytes, format="audio/mp3", start_time=0)
            os.remove(audio_file)  # Clean up
    else:
        st.warning("No tips found for your query. Try another term!")

# Set background image
set_background("Organic_Bg.jpg")

# Footer
st.markdown("---")
st.markdown(
    "🌟 **Explore more about sustainable agriculture at [FAO](http://www.fao.org).**"
)
