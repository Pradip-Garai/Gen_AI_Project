import streamlit as st
from Config.send_otp import send_otp_email
from Config.database_connection import cursor


def forgot_password_ui():
    st.title("🔐 Forgot Password")

    email = st.text_input("Enter your registered email")

    col1, col2 = st.columns([1, 4])

    with col1:
        if st.button("Reset Password"):

            if not email:
                st.warning("⚠️ Please enter your email")
                return

            sql = "SELECT PASSWORD FROM USERS WHERE EMAIL = %s"
            cursor.execute(sql, (email,))
            row = cursor.fetchone()

            if row:
                password = row["PASSWORD"]
                send_otp_email(email, password)
                st.success("📩 Password sent to your registered email")
                st.session_state.page = "login"
            else:
                st.error("❌ User Not Found")

    with col2:
        if st.button("⬅ Back to Login"):
            st.session_state.page = "login"
            st.rerun()
