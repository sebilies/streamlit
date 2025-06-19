<<<<<<< HEAD
import streamlit as st
#st.write("Hello ,let's learn how to build a streamlit app together")
st.title("This is the app title") # Affiche un titre principal en haut de l'application
st.header("This is the header")# Affiche un en-tête de niveau 1 (juste en dessous du titre)
st.markdown("This is the markdown")# Affiche un texte formaté en markdown (permet des styles comme gras, italique, listes, etc.)
st.subheader("This is the subheader")# Affiche un sous-titre (niveau en dessous de header)
st.caption("This is the caption")# Affiche une légende ou un texte d’accompagnement en petit (souvent pour des explications)
st.code("x = 2021") # Affiche un bloc de code avec coloration syntaxique
st.latex(r''' a+a r^1+a r^2+a r^3 ''')# Affiche une formule mathématique en LaTeX (utile pour les équations

st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)
=======
import streamlit as st
st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

>>>>>>> 4892465b7f85f26f4569c8c6e1394b6c4bd434a3
