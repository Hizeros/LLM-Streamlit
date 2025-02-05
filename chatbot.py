from promptulate.llms import ChatOpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key",
                                   type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/hizeros/llm-streamlit/blob/master/Chatbot.py)"  # noqa

st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by Promptulate")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant",
                                     "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    llm: ChatOpenAI = ChatOpenAI(model="gpt-3.5-turbo",
                                 messages=st.session_state.messages)
    response: str = llm(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
