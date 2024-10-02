import streamlit as st
from Controller.SignUp import SignUp
from types import SimpleNamespace


if ("respose" in st.session_state and st.session_state.respose != None):

    if st.session_state.respose["status"] == "ok":
        st.success(st.session_state.respose["message"])

    elif st.session_state.respose["status"] == "error":
        st.error(st.session_state.respose["message"])

    st.session_state.respose = None


st.title("Sign Up")

with st.form("signup_form"):


    # TODO: Add verification if username already exists in database

    username = st.text_input("Username", value=None, max_chars=255, key="username")

    # TODO: Add verification if email already exists in database

    email = st.text_input("E-mail", value=None, max_chars=255, key="email")

    password = st.text_input("Password", value=None, max_chars=255, key="password", type="password")

    confirmPassword = st.text_input(label="Confirm Password", value=None, max_chars=255, key="confirmPassword", type="password")

    st.session_state.signup_formSubmitter = st.form_submit_button("Submit", on_click=SignUp.register)


print(f"View: {st.session_state}")