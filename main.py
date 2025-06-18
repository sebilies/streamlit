import streamlit as st
#st.write("Hello ,let's learn how to build a streamlit app together")
st.title("This is the app title") # Affiche un titre principal en haut de l'application
st.header("This is the header")# Affiche un en-tête de niveau 1 (juste en dessous du titre)
st.markdown("This is the markdown")# Affiche un texte formaté en markdown (permet des styles comme gras, italique, listes, etc.)
st.subheader("This is the subheader")# Affiche un sous-titre (niveau en dessous de header)
st.caption("This is the caption")# Affiche une légende ou un texte d’accompagnement en petit (souvent pour des explications)
st.code("x = 2021") # Affiche un bloc de code avec coloration syntaxique
st.latex(r''' a+a r^1+a r^2+a r^3 ''')# Affiche une formule mathématique en LaTeX (utile pour les équations

st.subheader("Image")
st.image("kid.jpg", caption="A kid playing")
st.subheader("Audio") 
with open("D:/DataScience-bootcamp-gomycode/streamlint/fail-sound-comedy-reaction-309057.mp3", "rb") as audio_file:
    st.audio(audio_file.read(), format="audio/mp3")#st.video("video.mp4")
#"rb" = read binary, c’est obligatoire pour lire des fichiers comme des sons, images, PDF, etc.
#Le mot-clé with garantit que le fichier est bien fermé automatiquement après la lecture.
#audio_file est un objet contenant le contenu du fichier audio
st.subheader("video : ")
st.video("video.mp4")