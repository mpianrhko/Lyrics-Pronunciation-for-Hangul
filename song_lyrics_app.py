import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Retrieve API key
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Generative AI
genai.configure(api_key=api_key)

# Functions to fetch lyrics, pronunciation, and translation
def fetch_lyrics(song_name):
    """Fetch the lyrics of a song based on its title."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = (
        f"Provide the full lyrics for the song '{song_name}'. "
        f"Do not include any commentary or additional information."
    )
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_english_pronunciation_in_hangul(input_text):
    """Generate the Hangul pronunciation of English text."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = (
        f"Convert the English text below into its pronunciation in Hangul (Korean alphabet). "
        f"Not Korean pronunciation in Hangul, but the pronunciation of English words in Hangul. "
        f"Provide only the Hangul text. \n\n{input_text}"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_korean_translation(input_text):
    """Generate the Korean translation of English text."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = (
        f"Translate the English text below into Korean. "
        f"The translation must be formal and appropriate. "
        f"Provide only the Korean translation. \n\n{input_text}"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit UI
st.title("Song Lyrics Pronunciation & Translation App")
st.write("Enter the name of a famous song to get its lyrics, English pronunciation in Hangul, and Korean translation.")

# Input for song name
song_name = st.text_input("Enter Song Name:")

if st.button("Generate"):
    if song_name.strip():
        with st.spinner("Fetching song details..."):
            # Fetch lyrics
            try:
                lyrics = fetch_lyrics(song_name)
                pronunciation = generate_english_pronunciation_in_hangul(lyrics)
                translation = generate_korean_translation(lyrics)
                
                # Display results
                st.subheader("Song Lyrics:")
                st.text(lyrics)
                
                st.subheader("English Pronunciation in Hangul:")
                st.text(pronunciation)
                
                st.subheader("Korean Translation:")
                st.text(translation)
            except Exception as e:
                st.error("An error occurred. Please try again later.")
    else:
        st.warning("Please enter a valid song name.")
