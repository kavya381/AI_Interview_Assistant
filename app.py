import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Assistant", page_icon="🥰", layout="centered")
st.title("AI Interview Assistance")
st.caption("Practice and Prepare for your placements here")

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFoundError):
    st.error("API key is missing. Add it in advanced settings")
    st.stop()

role = st.selectbox("Job Title", ["select", "devops", "AI Engineer", "Data Analyst", "Test engineer", "other"])

if role == "other":
    role = st.text_input("Enter your Job Title", "XXXXXX")

gen_model = st.selectbox("Model", ["select", "openai/gpt-oss-20b", "openai/gpt-oss-120b"])

level = st.selectbox("Difficulty Level", ["select", "Advanced", "Intermediate", "Beginner"])

mode = st.radio("Activity", ["Generate Questions", "Generate Code Questions", "Evaluate Answers", "Improve the Answers"])

if mode == "Generate Questions":
    count = st.slider("Number of Questions", 1, 10, 5)

elif mode == "Generate Code Questions":
    topic = st.selectbox("Topics", ["AIML", "C/C++", "PYTHON", "JAVA", "DSA", "DEVOPS", "SQL", "MYSQL"])
    count = st.slider("Number of Questions", 1, 10, 5)

else:
    question = st.text_area("Enter Interview Question Here!!")
    answer = st.text_area("Enter Your Answer", height=160)

btn = st.button("Generate AI Response")

if btn:

    if mode in ["Evaluate Answers", "Improve the Answers"] and (not question.strip() or not answer.strip()):
        st.warning("Please Enter a valid Question and Answer")
        st.stop()

    if role == "select" or not role.strip() or gen_model == "select" or level == "select":
        st.warning("Please select all the required options")
        st.stop()

    if mode == "Generate Questions":
        task = "Generate " + str(count) + " frequently asked Interview questions, including theoretical and technical questions. Do not give answers, give hints."

    elif mode == "Generate Code Questions":
        task = "Generate " + str(count) + " frequently asked coding questions on topic " + topic + " and give hints to solve them. Be accurate."

    elif mode == "Evaluate Answers":
        task = "Question: " + question + "\nMy answer is: " + answer + "\nEvaluate this answer based on concept, relevance, communication and length of answer."

    elif mode == "Improve the Answers":
        task = "Question: " + question + "\nMy answer is: " + answer + "\nImprove this answer based on choice of words, keywords and professional communication."

    bg = "Job role: " + role + "\nDifficulty level: " + level

    with st.spinner("Generating your answers....!"):
        try:
            response = client.chat.completions.create(
                model=gen_model,
                messages=[
                    {"role": "system", "content": "Act as a senior Interviewer, both HR and Technical expert"},
                    {"role": "user", "content": bg + task}
                ],
                temperature=0.7,
                max_tokens=1000
            )

            output = response.choices[0].message.content

            st.subheader("AI Response")
            st.markdown(output)

            st.download_button("Download Response", output, file_name="Interview_Response.txt", mime="text/plain")

            st.success("Response generated successfully!")

        except Exception as e:
            st.error(f"API Connection was unsuccessful: {e}")
            st.info("Please check your API key and rate limits")

    st.write("Welcome!")
    st.write("Good Morning...")
