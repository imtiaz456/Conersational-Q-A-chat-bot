from langchain_community.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
 
#We will create a function to load OpenAi and get response

def get_openai_response(question):
    llm = OpenAI(openai_api_key = os.environ["OPENAI_API_KEY"], model_name = "gpt-3.5-turbo-instruct", temperature = 0.5)
    response = llm(question)
    return response

# Now we will initiallizes our streamlit app
st.set_page_config(page_title="Q & A Demo")
st.header("Langchain App")

input = st.text_input("input: ", key="input")
response = get_openai_response(input)

# now we will find a way to get user input
submit = st.button("Ask a Question")

# if ask button is clicked
if submit:
    st.subheader("The response is: ")
    st.write(response)
