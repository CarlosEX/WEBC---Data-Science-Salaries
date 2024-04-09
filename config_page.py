import streamlit as st

hide_st_style = """
                        <style>
                        header {visibility: hidden}
                        .block-container {padding:16px}
                        .st-emotion-cache-16txtl3 {padding: 1rem}
                        #MainMenu {visibility:hidden;}
                        .stDeployButton {visibility:hidden;}
                        .viewerBadge_link__qRIco {visibility:hidden;}
                        
                        .viewerBadge_container__r5tak {visibility:hidden;}
                        .viewerBadge_container__r5tak {display: none;}
                        
                        .styles_viewerBadge__CvC9N {visibility:hidden;}
                        .styles_viewerBadge__CvC9N {display: none;}
                        
                        
                        .viewerBadge_link__qRIco {visibility:hidden;}
                        .viewerBadge_link__qRIco {display: none;}
                        .st-emotion-cache-zq5wmm {visibility:hidden;}
                        .st-emotion-cache-zq5wmm {display: none;}
                        .viewerBadge_container__r5tak {pointer-events: none;}
                        .st-emotion-cache-32ts9 {background-color: rgba(1, 1, 255);}
                        footer {visibility:hidden;}
                        </style>
            """
    #
    # 

st.markdown(hide_st_style, unsafe_allow_html=True)