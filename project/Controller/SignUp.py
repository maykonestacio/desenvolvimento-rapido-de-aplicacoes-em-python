from Model.Database import Database
import streamlit as st
from types import SimpleNamespace

class SignUp:

    @staticmethod
    def register(session_state):

        print(f"Controller: {st.session_state}")

        if (session_state.valid and ("FormSubmitter:signup_form-Submit" in session_state)):

            session_state.respose = SimpleNamespace(status="ok", message="User created successfully!")

            st.rerun(scope="fragment")

database = Database()

database.cursor.execute("SELECT * FROM User")

rows = database.cursor.fetchall()

# for row in rows:
#     st.write(dict(row))
