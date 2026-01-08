import streamlit as st
from Pages.forgot_password import forgot_password_ui
from Pages.login import login_ui
from Pages.signup import signup_ui
from Pages.main_page import main_page


if "page" not in st.session_state:
    st.session_state.page = "login"   # login | signup | main

# ---- SESSION STATE INIT (IMPORTANT) ----
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


def main():
    if st.session_state.page == "login":
        login_ui()

    elif st.session_state.page == "signup":
        signup_ui()

    elif st.session_state.logged_in:
        main_page()

    elif st.session_state.page == "forgot_password":
        forgot_password_ui()



if __name__ == "__main__":
    main()
