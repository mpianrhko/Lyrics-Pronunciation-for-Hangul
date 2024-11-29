
# Song Lyrics Pronunciation & Translation App 🎵

This Streamlit app allows users to enter the name of a famous song and get:
1. The full lyrics of the song.
2. The English pronunciation in Hangul (Korean alphabet).
3. A formal Korean translation of the lyrics.

---

## Features ✨

- **Dynamic Lyrics Retrieval**: Fetch lyrics for famous songs based on their title.
- **English Pronunciation in Hangul**: Convert English text into its Korean phonetic representation.
- **Korean Translation**: Provide a formal and accurate Korean translation of the lyrics.

---

## Demo 🚀

Check out the app live: [Song Lyrics Pronunciation & Translation App]([https://your-streamlit-app-url.streamlit.app](https://lyrics-pronunciation-for-hangul.streamlit.app/))  

**Enter a Song Name**:
   - Type the name of a famous song (e.g., *"Jesus Loves Me"*) into the input box.
   - Click "Generate" to fetch:
     - Song lyrics
     - Pronunciation in Hangul
     - Korean translation
---

## Example 🎤

### Input:
Song Name: *Jesus Loves Me*

### Output:
1. **Song Lyrics**:
   ```
   Jesus loves me, this I know
   For the Bible tells me so
   Little ones to Him belong...
   ```

2. **English Pronunciation in Hangul**:
   ```
   지저스 러브스 미, 디스 아이 노우...
   ```

3. **Korean Translation**:
   ```
   예수님은 나를 사랑하시죠, 저는 알고 있어요...
   ```
   
---

## Tech Stack 🛠️

This app is built using the following technologies:

### Backend:
- **Google Generative AI (gemini-1.5-flash)**: To generate song lyrics, English-to-Hangul phonetic transliteration, and Korean translations.
- **Python**: Core programming language for building the app.

### Frontend:
- **Streamlit**: A lightweight Python web framework for creating interactive and shareable web apps.

### Environment & Dependency Management:
- **python-dotenv**: To securely manage local environment variables during development.
- **Streamlit Secrets Manager**: For securely storing API keys in a deployed environment.

### Hosting:
- **Streamlit Community Cloud**: Free and simple platform for hosting Streamlit apps.

---

## Acknowledgments 🙏

Special thanks to:
- **Google Generative AI** for powering the app's natural language processing capabilities.
- **Streamlit** for providing an easy-to-use web app framework.
- This project is dedicated to my maternal grandfather, who wanted to learn and sing in English. His enthusiasm for learning inspired me to create this app.

---

## FAQ ❓

**Q: What if the app cannot fetch lyrics for a song?**  
A: The app uses an AI model to retrieve lyrics. If the song is very obscure or unavailable in the model’s dataset, the app may fail to fetch the lyrics. Try using more famous or widely known songs.

**Q: Are there limits to API usage?**  
A: Yes, the app relies on Google Generative AI, which may have rate limits depending on your API plan. Heavy usage could lead to temporary restrictions.

