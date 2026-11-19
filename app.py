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
model = st.selectbox('gen_model',['qwen/qwen3.8-27b', 'openai/gpt-oss-120b'])
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
  if mode in ['Evaluate Answers', 'Improve Answer'] and (not question.strip()) or (not answer.strip()):
   st.warning ("Please enter the valid Question and Answer")
   st.stop()                                                                               
if mode == "Generate Questions":
  task = "Generate" + str(count) + "Frequently asked Interview Questions, 3 theory and 2 scenario questions. Do not give answers. Give Hints"
elif mode == " Generate Code Questions":
  task = "Generate" + str(count) + "Frequently asked coding questions on topic" + topic + "and give hints to solve them. Be accurate." 
elif mode == "Evaluate Answers":
       task = "Question : " + question + "My Answer : " + answer +"Evaluate this answer basd on concepts,relevence, communication length of answer.Give each rating out of 5"
elif mode == "Improve Answers":
       task = "Question : " + question + "My Answer : " + answer + "improve the answer based on coding ,communication,apptitude ,preparation on interview."
       background = "Job role : " +role+ " Difficulti level " +level
with st.spinner("Generating your answer ..."):
  try:
    response = client.chat.completions.create(
      model = gen_model,
      messages = [{"role":"system ",
                   "content":"Act as a Student"},
                  {"role": "user ",
                  "content" : background + task}],
      temperature = 0.7,
      max_tokens = 1800
    )
    output = response.choices[0].message.content
    st.subheader("AI Response")
    st.markdown(output)
    st.download_button("Download Response", output, file_name = "Interview_Response.txt", mine = 'text/plain')
  except Exception as e:
    st.error("API connection was unsuccessful : ", e)
    st.info ("Please check your API Key and rate limits")
    st.caption("Powered by Streamlit.io and Github.Using LLM API")
