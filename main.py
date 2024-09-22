import streamlit as st
from scrape import scrape_website, clean_body_content, split_dom_content, extract_body_content

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrap Site"):
    st.write("Scraping the Website")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content
    with st.expander("View Dom Content"):
        st.text_area("Dom Content", cleaned_content, height=300)