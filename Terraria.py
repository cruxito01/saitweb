import streamlit as st

st.set_page_config(
    page_title="Terraria",
    page_icon=":radioactive_sign:",
    layout="centered",
    )
st.logo(
    "logo_content.png",
)
pg = st.navigation(["Intro.py", "NPC'S.py", "Jefes.py"])
pg.run()