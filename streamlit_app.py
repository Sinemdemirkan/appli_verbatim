
import streamlit as st
from PIL import Image
import requests
import base64


BASE_URL = "https://ml-dl-dark-sorcery-65ddmnvcwa-ew.a.run.app/"
corresponding = {0: "a1", 1: "a2", 2: "b1", 3: "b2", 4: "c1", 5: "c2"}

default_text_C1 = """To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream—ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause—there's the respect
That makes calamity of so long life.
"""

default_text_B1 = """Hagrid raised a gigantic fist and knocked three times
on the castle door.
The door swung open at once. A tall, black-haired
witch in emerald-green robes stood there. She had a very
stern face and Harry’s first thought was that this was not
someone to cross.
‘The firs’-years, Professor McGonagall,’ said Hagrid.
‘Thank you, Hagrid. I will take them from here.’
She pulled the door wide. The Entrance Hall was so big
you could have fitted the whole of the Dursleys’ house in
it. The stone walls were lit with flaming torches like the
ones at Gringotts, the ceiling was too high to make out,
and a magnificent marble staircase facing them led to
the upper floors.

"""

text = 'default_text_B1'

cefr='def'

# Set Streamlit page config
st.set_page_config(
    page_title="Verbatim",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📚",
)

# Load custom css sheet
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css?family=Fira+Mono');
body {
    font-family: 'Fira Mono', sans-serif;
}
</style>
""", unsafe_allow_html=True)


#Sidebar
st.sidebar.markdown("<div style='font-size: 25px; font-family: Fira Mono;'>Menu</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='font-size: 16px; font-family: Fira Mono;'>About</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='font-size: 16px; font-family: Fira Mono;'>Who for?</div>", unsafe_allow_html=True)


# Header and introductory content
st.markdown("<div align='center', style='font-size: 70px; font-family: Fira Mono;'>verbatim_</span>",unsafe_allow_html=True)
file_ = open("streamlit_vid.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f"<div><img src='data:image/gif;base64,{data_url}' width='100%'></div>",
    unsafe_allow_html=True,
)
st.markdown(" ")
st.markdown("<div style='font-family: Fira Mono; font-size: 16px'>Find texts adapted to your level,<span style='color: #00b050'> read smart  <br/></span></div> \n", unsafe_allow_html=True)
st.markdown(" ")
st.markdown(" ")

slider_values = [0,1]
slider_strings = ['Shakespeare','Harry Potter']
#n_text = st.slider('',0,1)
def stringify(i:int = 0) -> str:
    return slider_strings[i]
n_text = st.select_slider('Select the text for the demo: ',
                    options = slider_values,
                    value =0,
                    format_func = stringify)
st.markdown(" ")
st.markdown("<div style='font-family: Fira Mono; font-size: 16px'>Please insert your text here 👇 (at least 110 words):</div> \n", unsafe_allow_html=True)
st.markdown(" ")


if n_text == 0:
    text = 'default_text_C1'
if n_text == 1 :
    text = 'default_text_B1'

# Text inputer
if text == 'default_text_C1':
    txt = st.text_area(label='', value=default_text_C1, height=400)
    st.markdown(f"<div style='font-family: Fira Mono; font-size: 16px'>Word count: <span style='color: #00b050'>{len(txt.split())}</span>", unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown("<div style='font-family: Fira Mono; font-size: 16px'>Estimate your text level:</div>", unsafe_allow_html=True)
    st.markdown(" ")
if text == 'default_text_B1':
    txt = st.text_area(label='', value=default_text_B1, height=400)
    st.markdown(f"<div style='font-family: Fira Mono; font-size: 16px'>Word count: <span style='color: #00b050'>{len(txt.split())}</span>", unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown("<div style='font-family: Fira Mono; font-size: 16px'>Estimate your text level:</div>", unsafe_allow_html=True)
    st.markdown(" ")


col1, col2, col3, col4, col5 = st.columns(5)


# ML button

with col2:
    if st.button('machine learning!'):
        len_txt = len(txt.split())
        if len_txt < 110:
            st.error('Please insert a longer text (at least 110 words)')
        else:
            result = requests.get(f"{BASE_URL}ml_predict", params={"text": txt}).json()
            level = result["estimated_level"]
            cefr = corresponding[level]
            print('Simple button clicked!')

# DL button
with col4:
    if st.button('deep learning!'):
        len_txt = len(txt.split())
        if len_txt < 110:
            st.error('Please insert a longer text (at least 110 words)')
        else:
            result = requests.get(f"{BASE_URL}dl_predict", params={"text": txt}).json()
            level = result["estimated_level"]
            cefr = corresponding[level]
            print('Composite button clicked!')


st.image(f'output_img/{cefr}.png')


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
