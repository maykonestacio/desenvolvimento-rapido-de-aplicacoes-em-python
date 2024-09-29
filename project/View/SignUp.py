import streamlit as st
from Tools.Validator import Validator
from Controller.SignUp import SignUp
from types import SimpleNamespace


if ("respose" in st.session_state and type(st.session_state.respose) == type(SimpleNamespace())):

    if st.session_state.respose.status == "ok":
        st.success(st.session_state.respose.message)

    elif st.session_state.respose.status == "error":
        st.error(st.session_state.respose.message)

    st.session_state.respose = None


st.title("Sign Up")

with st.form("signup_form"):

    st.session_state.valid = True

    if "confirmPassword" in st.session_state and "password" in st.session_state:

        if st.session_state.confirmPassword != st.session_state.password:
            st.error("Passwords don't match!", icon=":material/error:")
            st.session_state.valid = False

        if (st.session_state.confirmPassword == None and st.session_state.password == None)\
        or (st.session_state.confirmPassword == "" and st.session_state.password == ""):
            st.error("Passwords are required!", icon=":material/error:")
            st.session_state.valid = False
    else:
        st.session_state.valid = False

    if "email" in st.session_state:
        if  st.session_state.email == None or not Validator.validateEmail(st.session_state.email):
            st.error("E-mail is not valid!", icon=":material/error:")
            st.session_state.valid = False
    else:
        st.session_state.valid = False

    # TODO: Add verification if username already exists in database

    username = st.text_input("Username", value=None, max_chars=255, key="username")

    # TODO: Add verification if email already exists in database

    email = st.text_input("E-mail", value=None, max_chars=255, key="email")

    password = st.text_input("Password", value=None, max_chars=255, key="password", type="password")

    confirmPassword = st.text_input(label="Confirm Password", value=None, max_chars=255, key="confirmPassword", type="password")

    st.session_state.signup_formSubmitter = st.form_submit_button("Submit", on_click=SignUp.register, args=[st.session_state])

print(f"View: {st.session_state}")