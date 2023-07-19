import streamlit as st

# from langchain import LLMChain
# from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
# from langchain.prompts.chat import (
#     ChatPromptTemplate,
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
# )

st.title('check GPT')
pr=st.text_input('Enter text here')

# chat = ChatOpenAI(temperature=0.1,openai_api_key="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")
chat = OpenAI(temperature=0.9,openai_api_key="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")

if pr:
    resp=chat(pr)
    st.response(resp)

# template = "You are a helpful assistant that translates {input_language} to {output_language}."
# system_message_prompt = SystemMessagePromptTemplate.from_template(template)
# human_template = st.text_input('Please enter to be translated query:')
# human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
# chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# chain = LLMChain(llm=chat, prompt=chat_prompt)
# if human_template:
#     res=chain.run(input_language="English", output_language="French", text="I love programming.")
#     st.write(res)
