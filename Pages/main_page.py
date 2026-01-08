import streamlit as st 
from few_shot import FewShotPosts
from post_generator import generate_post

length_options = ['Short', 'Medium', 'Long']
language_options = ['English', 'Hinglish']


def main_page():
    st.title("LinkedIn Post Generator")

    fs = FewShotPosts()
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_title = st.selectbox(
            "Title",
            options=sorted(list(fs.get_tags()))
        )

    with col2:
        selected_length = st.selectbox("Length", length_options)

    with col3:
        selected_language = st.selectbox("Language", language_options)

    top_left, top_right = st.columns([6 ,1])
    with top_left:
        if st.button("Generate"):
            post = generate_post(
                selected_length,
                selected_language,
                selected_title
            )
            st.write(post)

    with top_right:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.page = "login"
            st.rerun()
