from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# output parser
output_parser = StrOutputParser()

# prompt template
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond in a friendly and relevant manner."),
        ("user", "Question: {question}")
    ]
)

# streamlit UI
st.title("Parrot v0.1")
adugu = st.text_input("Ask Any Question:")

# LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"))

# chain (LCEL way)
chain = template | llm | output_parser

if adugu:
    response = chain.invoke({"question": adugu})
    st.write(response)
    st.balloons()
