import streamlit as st
from groq import Groq
st.set_page_config(page_title = 'Placement practice' , layout='centered')
st.title("AI Interview Assistent")
st.caption("Practice and Prepare for your Placements here")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API Key is missing. Add it in Advanced settings")
  st.stop()
role = st.selectbox('Job Title',['Machine Learning Engineer', 'Senior Software Engineer', 'Devops Engineer', 'Others'])
