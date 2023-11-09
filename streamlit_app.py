__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st
from langchain.llms import OpenAI

### customize your title here ###
st.title('🦜🔗 My first App with LLM')

# openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    ### customize temperature between 0 to 1 ####
    # Higher temperatures introduce randomness/diverse output, which is beneficial for creative tasks.
    # In contrast, a temperature of zero ensures consistent/deterministic responses,
    # making GPT a reliable tool for obtaining determined outputs with no variation.
    ###

    llm = OpenAI(temperature=1, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    ### customize your text area here ###
    openai_api_key = st.text_input('OpenAI API Key', type='password')
    txt_input = st.text_area('Enter text:', 'enter your text here')

    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(txt_input)
