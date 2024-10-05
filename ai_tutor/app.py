# app.py
import streamlit as st
from openai_helper import get_openai_response

# Set up the Streamlit app
st.title("AI Tutor")
st.write("Ask me anything!")

# Create a text input box for user to enter a question
user_question = st.text_input("Enter your question:")

# If the user submits a question, call the OpenAI API and display the result
if st.button("Get Answer"):
    if user_question:
        with st.spinner('Getting your answer...'):
            answer = get_openai_response(user_question)
            st.success("AI says:")
            st.write(answer)
    else:
        st.warning("Please enter a question!")
