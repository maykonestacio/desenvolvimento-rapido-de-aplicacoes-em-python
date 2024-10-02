from Model.Database import Database
import streamlit as st
from Tools.Validator import Validator

class SignUp:

    @staticmethod
    def register():

        valid = True

        if "username" in st.session_state:
            if st.session_state.username == None or st.session_state.username == "":
                st.error("Username is required!", icon=":material/error:")
                valid = False
        else:
            valid = False

        if "confirmPassword" in st.session_state and "password" in st.session_state:

            if st.session_state.confirmPassword != st.session_state.password:
                st.error("Passwords don't match!", icon=":material/error:")
                valid = False

            if (st.session_state.confirmPassword == None and st.session_state.password == None)\
            or (st.session_state.confirmPassword == "" and st.session_state.password == ""):
                st.error("Passwords are required!", icon=":material/error:")
                valid = False
        else:
            valid = False

        if "email" in st.session_state:
            if  st.session_state.email == None or st.session_state.email == "":
                st.error("E-mail is required!", icon=":material/error:")

            elif not Validator.validateEmail(st.session_state.email):
                st.error("E-mail is not valid!", icon=":material/error:")
                valid = False
        else:
            valid = False

        print(f"Controller: {st.session_state}")

        if (valid):

            st.session_state.respose = {"status":"ok", "message":"User created successfully!"}

database = Database()

database.cursor.execute("SELECT * FROM User")

rows = database.cursor.fetchall()

# for row in rows:
#     st.write(dict(row))
