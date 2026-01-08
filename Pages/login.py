import streamlit as st 
from Config.auth import login

def login_ui():

    error_box = st.empty()

    st.title("LinkedIn Post Generator")
    email = st.text_input("Enter Your Email")
    password = st.text_input("Enter Password")

    btn_col1, btn_col2, btn_col3= st.columns([1,6,2])

    with btn_col1:
        if st.button("Login"):
            user = login(email,password)
            if user == False:
                error_box.error("❌ User Not Found")
            else:
                st.session_state.logged_in = True
                st.session_state.username = user
                st.session_state.page = "main"
                st.rerun()
    with btn_col2:
        if st.button("Forgot Password?"):
            st.session_state.page = "forgot_password"
            st.rerun()
    with btn_col3:
        if st.button("Create Account"):
            st.session_state.page = "signup"
            st.rerun()
