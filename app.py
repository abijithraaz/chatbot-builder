import os

import streamlit as st
from llm_chat.openai_llm import OpenAiLLM
from prompt_augmentor import PromptAugmentor
from embedding.openai_embedd_generator import OpenaiEmbeddGenarator


# Env variables

# os.environ['OPENAI_API_KEY'] = ''
# os.environ['OPENAI_EMBEDD_MODEL'] = 'text-embedding-ada-002'
# os.environ['PINECONE_API_KEY'] = ''
# os.environ['PINECONE_ENVIRONMENT'] = 'gcp-starter'
# os.environ['PINECONE_INDEX_NAME'] = 'chatter-db'

# calling openai service
openai_chat = OpenAiLLM()
rag_client = PromptAugmentor()
embedd = OpenaiEmbeddGenarator()

# UI section
st.header(body='Chatbot-Builder 🤗💬', divider='rainbow')
st.markdown(body= 'Chatter wil help you to create customized Chatbot.')
st.subheader(body='Customized-Chatbot')

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
        # chat_response = openai_chat.llmchat(query)
        chat_response = rag_client.augment_prompt(query=query,embedd=embedd.embed,llm=openai_chat.client)
        st.markdown(chat_response)
    # Adding response to history
    st.session_state.messages.append({"role":"assistant", "content":chat_response})

# Clear chat button
with st.sidebar:
    if button := st.button('CLEAR CHAT', type='primary',use_container_width=True):
        if "messages" in st.session_state:
            st.session_state.messages = []

    
