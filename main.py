import streamlit as st

st.title("AI Web Scraper")
url = st.text_input("Ente a Website URL: ")

if st.button("Scrap Site"):
    st.write("Scraping the Website")