import streamlit as st
import openai
from decouple import config
import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vision_key.json'
openai.api_key = config("OPENAI_API_KEY")

def detect_text(content):
    image = vision.Image(content=content)
    vision_client = vision.ImageAnnotatorClient()
    response = vision_client.text_detection(image=image)
    text = response.text_annotations[0].description
    return text

def generate_prompt(text: str, takeaways_num) -> str:
    """
    Generate prompt for summarization model
    :param text:
    :return:
    """
    newline = '\n'
    return f"Can you see any common pattern in these actions? Can you name top {takeaways_num} themes?: {newline}{text}{newline}Tl;dr"

def app():
    st.title('Welcome to retrospective summarizer!')
    is_text = st.checkbox('I have my notes as text')
    if is_text:
        st.text_input("Paste your notes here", key="meeting_notes")
        meeting_notes = st.session_state.meeting_notes
    else:
        uploaded_file = st.file_uploader("Drop a photo of your sticky notes / screenshot from the board")
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            meeting_notes = detect_text(bytes_data)
        else:
            meeting_notes = None
    takeaways_num = st.slider('How many topics do you want to extract?', 1, 5, 3)
    if meeting_notes is not None:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(meeting_notes, takeaways_num),
            temperature=0.7,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1
        )
        summary = response.choices[0].text
        st.write(summary)


app()