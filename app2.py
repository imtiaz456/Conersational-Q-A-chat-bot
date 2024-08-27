# Conersational Q&A chat bot
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
import os

## streamllit ui

st.set_page_config(page_title = "Conversational Q&A chatbot")
st.header("Hey let's chat")


from dotenv import load_dotenv
load_dotenv()

chat = ChatOpenAI(temperature = 0.5)

# we created this if condition after creation of session_state function bellow
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] =[
        SystemMessage(content = "You are a commedian ai assistant")
    ]

# Function to load OpenAI model and get response

def get_chatmodel_response(question):
    st.session_state["flowmessages"].append(HumanMessage(content=question)) # we can initialize a new value we want thorugh session state..
                                                                            #available in streamlit documentation.
    answer = chat(st.session_state['flowmessages'])
    st.session_state["flowmessages"].append(AIMessage(content=answer.content))
    return answer.content

# Now we will initiallizes our streamlit app

input = st.text_input("input: ", key="input")
response = get_chatmodel_response(input)

# now we will find a way to get user input
submit = st.button("Ask a Question")

# if ask button is clicked
if submit:
    st.subheader("The response is: ")
    st.write(response)