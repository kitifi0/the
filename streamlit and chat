import streamlit as st
from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Streamlit app
st.title("Sentiment Analysis")

# Create a sidebar for the chat messages
with st.sidebar:
    st.write("Chat History")
    messages = st.container()

# Chat input
prompt = st.chat_input("Say something")

# Process the input and perform sentiment analysis
if prompt:
    # Display user message
    with messages:
        st.chat_message("user").write(prompt)

    # Append user message to history
    st.session_state.history.append({"role": "user", "content": prompt})

    # Perform sentiment analysis
    sentiment_result = sentiment_pipeline(prompt)
    sentiment = sentiment_result[0]['label']
    score = sentiment_result[0]['score']

    # Display sentiment analysis result
    with messages:
        st.chat_message("assistant").write(f"Sentiment: {sentiment} (score: {score:.2f})")

# Display chat history
with messages:
    for msg in st.session_state.history:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])
