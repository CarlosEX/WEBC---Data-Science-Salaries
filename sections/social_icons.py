import streamlit as st

def linkedin_icon(link, width=30):
    st.markdown(
        f'<a href="{link}" target="_blank"><img src="https://logospng.org/download/linkedin/logo-linkedin-icon-2048.png" width="{width}"></a>',
        unsafe_allow_html=True,
    )

def yutube_icon(link, width=30):
    st.markdown(
        f'<a href="{link}" target="_blank"><img src="https://logolook.net/wp-content/uploads/2021/06/Symbol-Youtube.png" width="{width}"></a>',
        unsafe_allow_html=True,
    )

