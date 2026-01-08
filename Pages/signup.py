import streamlit as st
from Config.auth import signup

def signup_ui():
    st.title("Create Account")

    name = st.text_input("Enter Your Name")
    email = st.text_input("Enter Your Email")
    password = st.text_input("Enter Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    col1, col2 = st.columns([4, 1])

    with col1:
        if st.button("Sign Up"):
            # Validate form
            if not name or not email or not password or not confirm_password:
                st.error("❌ All fields are required")
            elif password != confirm_password:
                st.error("❌ Passwords do not match")
            else:
                try:
                    signup(name, email, password)
                    st.success("✅ Account created successfully")
                    st.session_state.page = "login"
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error creating account: {str(e)}")

    with col2:
        if st.button("Back to Login"):
            st.session_state.page = "login"
            st.rerun()
