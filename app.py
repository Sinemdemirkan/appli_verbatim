import streamlit as st
from PIL import Image
import requests

# Set Streamlit page config
st.set_page_config(
    page_title="Verbatim",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="📚"
)

# Header and introductory content
st.markdown("<h1 style='text-align: center; background-color: #000045; color: #ece5f6'>VERBATIM</h1>", unsafe_allow_html=True)
st.markdown(
    "<style>"
    "@keyframes dance {"
    "  0% { transform: translateY(0) rotate(0deg); }"
    "  25% { transform: translateY(-20px) rotate(20deg); }"
    "  50% { transform: translateY(0) rotate(-20deg); }"
    "  75% { transform: translateY(20px) rotate(20 deg); }"
    "  100% { transform: translateY(0) rotate(10 deg); }"
    "}"
    "</style>"
    "<div style='display: flex; flex-direction: row; justify-content: center; align-items: center; "
    "height: 100px; background-color: 'white'; border-radius: 50px;'>"
    "<h4 style='text-align: center; color: #2e2249; margin: 0; padding: 10px; font-family: \"Roboto\", sans-serif;'>Your Language Guide</h4>"
    "<h4 style='text-align: center; font-size: 72px; margin: 0; padding: 0; color: #6c5ce7; animation: dance 2s linear infinite;'>&#128221;</h4>"
    "</div>",
    unsafe_allow_html=True
)
st.markdown("<h4 style='text-align: center; background-color: #000045; color: #ece5f6; padding: 20px; font-family: \"Roboto\", sans-serif;'>Find texts adapted to your level, read smart.</h4>", unsafe_allow_html=True)


# Menu data (you can use this later as needed)
menu_data = [
    {'id': 1, 'label': "How To", 'key': "md_how_to", 'icon': "fa fa-home"},
    {'id': 2, 'label': "Individual Document", 'key': "md_run_analysis"},
    {'id': 3, 'label': "Document Collection", 'key': "md_document_collection"},
    {'id': 4, 'label': "Semantic Q&A", 'key': "md_rag"}
]

# Verbatim App section

corresponding = {0: "A1", 1: "A2", 2: "B1", 3: "B2", 4: "C1", 5: "C2"}
BASE_URL = "https://nb-api-opti-65ddmnvcwa-ew.a.run.app/"

default_text = "Please insert your text here 👇 (at least 110 words): "
txt = st.text_area("", value=default_text, height=400)

st.markdown(
    """
    <style>
    .stTextInput {
        width: 100%;
        padding: 12px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        margin-bottom: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.write('Word count:', len(txt.split()))

# Simple button
if st.button('Simple'):
    len_txt = len(txt.split())
    if len_txt < 110:
        st.error('Please insert a longer text (at least 110 words)')
    else:
        result = requests.get(f"{BASE_URL}simple_predict", params={"text": txt}).json()
        level = result["estimated_level"]
        cefr = corresponding[level]
        st.write(cefr)
        st.balloons()
        print('Simple button clicked!')

# Composite button
if st.button('Composite'):
    len_txt = len(txt.split())
    if len_txt < 110:
        st.error('Please enter a longer text (at least 110 words)')
    else:
        result = requests.get(f"{BASE_URL}composite_predict", params={"text": txt}).json()
        level = result["estimated_level"]
        cefr = corresponding[level]
        st.write(cefr)
        st.balloons()
        print('Composite button clicked!')


# Image display and rotation button
image_path = "/Users/fahirdemirkan/Desktop/try.png"
if st.button('Show Image and Rotate'):
    pil_image = Image.open(image_path)
    st.image(pil_image)
    st.markdown(
        f"""
        <style>
        @keyframes rotate {{
            0% {{ transform: translate(-50%, -50%) rotate(0deg); }}
            100% {{ transform: translate(-50%, -50%) rotate(360deg); }}
        }}
        .rotating-image {{
            animation: rotate 4s linear infinite;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }}
        </style>
        <img src="data:image/png;base64,{pil_image}" alt="Rotating Image" class="rotating-image"/>
        """,
        unsafe_allow_html=True
    )

dictionary_book_recommendation = {'A1': ["The North Wind and the Sun, Jill O'Sullivan, Ed. Our World Readers. ",
  'The Four Blind Men, Vikram Gulaty, Ed. Our World Readers. '],
 'A2': ['Mystery in San Francisco, Gina D.B Clemen - Ed. Black Cat',
  'The Mozart Question, Michael Morpugo',
  'Fantastic Mr. Fox, Roald Dahl',
  'Billionaire Boy, David Walliams'],
 'B2': ["Harry Potter and the Philosopher's Stone, J. K. Rowling",
  'Wonder, Palacio. R.J.',
  'Peter Pan, J. M. Barrie',
  'The Jungle Book, Rudyard Kipling'],
 'C1': ['Holes, Louis Sachar',
  'Divergent, Veronica Roth',
  'Hunger Games, Suzanne Collins',
  'Lessons in Chemistry, Bonnie Garmus',
  'They Both Die at the End, Adam Silvera',
  'The Adventures of Sherlock Holmes, Arthur Conan Doyle',
  'The Strange Case of Dr. Jekyll and Mr. Hyde, Robert Louis Stevenson']}
