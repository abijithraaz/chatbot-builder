import os

import streamlit as st

st.header(body='Chatter', divider='rainbow')
st.markdown(body= 'Chatter is also known as Chat Bot Builder')

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

# tab1, tab2 = st.tabs(tabs=['chatbot', 'Manager'])

# with tab1:
st.subheader(body='ChatBot')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display history of app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])

# Accept user input and process
if query := st.chat_input('Please write your query...'):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})

# Chat response
with st.chat_message('assistant'):
    st.markdown('Good question!!!')
# Adding response to history
st.session_state.messages.append({"role":"assistant", "content":"Good question!!!"})


    