import streamlit as st
import requests
import numpy as np
import pandas as pd

st.markdown("""# Verbatim APP""")
corresponding = {0:"A1", 1:"A2", 2:"B1", 3:"B2", 4:"C1", 5: "C2"}

BASE_URL = "https://nb-api-opti-65ddmnvcwa-ew.a.run.app/"

txt = st.text_area('Enter an english text extract. Our model will give you its CEFR mark:', """I would say to the House, as I said to those who have joined this government: 'I have nothing to offer but blood, toil, tears and sweat'. We have before us an ordeal of the most grievous kind. We have before us many, many long months of struggle and of suffering. You ask, what is our policy? I can say: It is to wage war, by sea, land and air, with all our might and with all the strength that God can give us; to wage war against a monstrous tyranny, never surpassed in the dark, lamentable catalogue of human crime.That is our policy You ask, what is our aim? I can answer in one word: It is victory, victory at all costs, victory in spite of all terror, victory, however long and hard the road may be; for without victory, there is no survival""")

st.write('Word count:', len(txt.split()))
# and used to select the displayed lines



if st.button('Simple'):

    len = len(txt.split())

    if len < 110:
        st.error('Please enter a longer text (at least 110 words)!')

    else:
        # st.info('Wait for it...')
        result = requests.get(f"{BASE_URL}simple_predict", params={"text":txt}).json()
        st.write(result)
        level = result["naive_bayes_level"]
        cefr=corresponding[level]
        st.write(cefr)
        st.balloons()

    # print is visible in the server output, not in the page
        print('button clicked!')

if st.button('Composite'):

    len = len(txt.split())

    if len < 110:
        st.error('Please enter a longer text (at least 110 words)!')

    else:
        # st.info('Wait for it...')
        result = requests.get(f"{BASE_URL}composite_predict", params={"text":txt}).json()
        st.write(result)
        # level = result["naive_bayes_level"]
        # cefr=corresponding[level]
        # st.write(cefr)
        # st.balloons()

    # print is visible in the server output, not in the page
        print('composite button clicked!')


# if 'stage' not in st.session_state:
#     st.session_state.stage = 0

# def set_state(i):
#     st.session_state.stage = i

# if st.session_state.stage == 0:
#     st.button('Begin', on_click=set_state, args=[1])

# if st.session_state.stage >= 1:
#     name = st.text_input('Insert text here:)', on_change=set_state, args=[2])

# if st.session_state.stage >= 2:
#     st.write(f'Hello {name}!')
#     color = st.selectbox(
#         'Rank my text',
#         [None, 'red', 'orange', 'green', 'blue', 'violet'],
#         on_change=set_state, args=[3]
#     )
#     if color is None:
#         set_state(2)

# if st.session_state.stage >= 3:
#     st.write(f':{color}[Thank you!]')
#     st.button('Start Over', on_click=set_state, args=[0])



# def markdown_progress(x: float) -> str:
#     '''
#     Returns a bar from a number between 0 and 100.
#     '''
#     return(f"""![](https://geps.dev/progress/{x})""")
# df = pd.DataFrame({"thing":["Python", "C++", "JS"], "x": [20, 50, 90]})
# df["bar"] = df["x"].map(markdown_progress)
# st.markdown(df.to_markdown())












# result = requests.get(BASE_URL)
# result.json()

# st.write(result.json())

# predict?text=toto
