import streamlit as st
from groq import Groq
st.set_page_config(page_title = 'Placement practice' , layout='centered')
st.title("AI Interview Assistent")
st.caption("Practice and Prepare for your Placements here")
st.caption("Launched by Kavya MP")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API Key is missing. Add it in Advanced settings")
  st.stop()
role = st.selectbox('Job Title',['Machine Learning Engineer', 'Senior Software Engineer', 'Devops Engineer', 'Others'])
if role == "Others":
  st.text_input("Enter your Job Title", "XXXXXX")
model = st.selectbox('Model',['qwen/qwen3.8-27b', 'openai/gpt-oss-120b'])
Level = st.selectbox('Difficulty',['Beginner','Intermediate','Advanced'])
mode = st.radio('Activity',['Generate Questions','Generate Code Question','Evaluate Answer','Improve Answer'])
if mode == 'Generate Questions':
    count = st.slider("Number of Questions",1,10,5)
elif mode == 'Generate Code Question':
    topic = st.selectbox('Topics', ['SQL','AIML','Python','DSA','C++/C','JAVA','ADA'])
    count = st.slider("Number of Questions",1,10,5)
else:
  question = st.text_area('Enter Interview Questions here')
  answer = st.text_area('Enter your answer', height=160)
  if st.button ("Generate AI Response",type = "primary"):
if mode == (['Evaluate Answers', 'Improve Answer'] and (not question.strip()) or (not answer.strip()))
 st.warning("Please enter the valid Question and Answer")
 st.stop()                                                                               
