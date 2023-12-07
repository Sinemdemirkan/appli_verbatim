import streamlit as st
from PIL import Image
import requests

BASE_URL = "https://ml-dl-dark-sorcery-65ddmnvcwa-ew.a.run.app/"
corresponding = {0: "A1", 1: "A2", 2: "B1", 3: "B2", 4: "C1", 5: "C2"}

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

default_text_B1 = """
Hagrid raised a gigantic fist and knocked three times
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

cefr='def'

# Set Streamlit page config
st.set_page_config(
    page_title="Verbatim",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📚",
)

#Load custom css sheet
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


#Sidebar
st.sidebar.markdown("<div style='font-size: 25px'>Menu</div>", unsafe_allow_html=True)
st.sidebar.text("About")
st.sidebar.text("Who for?")


# Header and introductory content
st.markdown("<div align='center', style='font-size: 70px;'>verbatim_</span>",unsafe_allow_html=True)
st.markdown("Your Language Guide 🇬🇧/🇺🇸", unsafe_allow_html=True) # à aligner au milieu
st.markdown("Find texts adapted to your level,<span style='color: #00b050'> read smart</span>", unsafe_allow_html=True)


# Text inputer
txt = st.text_area("Please insert your text here 👇 (at least 110 words): ", value=default_text_C1, height=400)
st.write('Word count:', len(txt.split()))

st.text("Estimate you text level:")


col1, col2, col3, col4, col5 = st.columns(5)




# Simple button

with col2:
    if st.button('machine learning!'):
        len_txt = len(txt.split())
        if len_txt < 110:
            st.error('Please insert a longer text (at least 110 words)')
        else:
            result = requests.get(f"{BASE_URL}ml_predict", params={"text": txt}).json()
            level = result["estimated_level"]
            cefr = corresponding[level]
            st.balloons()
            print('Simple button clicked!')

# Composite button
with col4:
    if st.button('deep learning!'):
        len_txt = len(txt.split())
        if len_txt < 110:
            st.error('Please insert a longer text (at least 110 words)')
        else:
            result = requests.get(f"{BASE_URL}dl_predict", params={"text": txt}).json()
            level = result["estimated_level"]
            cefr = corresponding[level]
            st.balloons()
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
