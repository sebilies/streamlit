import streamlit as st
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