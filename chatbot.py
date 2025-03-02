import streamlit as st

# initializing chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Ask me something!")

if user_input:
    # Bot's response
    bot_response = f"Thank you for telling me {user_input}"
    # saving to chat history
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", bot_response))

# displaying chat history
for sender, message in st.session_state.chat_history:
    st.chat_message(sender).write(message)
