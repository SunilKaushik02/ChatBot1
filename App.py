import streamlit as st

from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

st.title('check GPT')

chat = ChatOpenAI(temperature=0.1,openai_api_key="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")

template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = st.text_input('Please enter to be translated query:')
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

chain = LLMChain(llm=chat, prompt=chat_prompt)
if human_template:
    res=chain.run(input_language="English", output_language="French", text="I love programming.")
    st.write(res)
