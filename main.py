from dotenv import load_dotenv
load_dotenv()
import os

import streamlit as st
import sqlite3

import google.generativeai as genai

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load google gemini model and provide sql query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve the query form the sql database
def read_sql_query(sql,db):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connect.commit()
    connect.close()
    for row in rows:
        print(row)
    return rows

# Define Your Prompt
prompt = [
    """
    You are a professional SQL query generator.

Your task is to convert English questions into clean, executable SQL queries based on the following database schema.

Database Name: STUDENT  
Table: STUDENT  
Columns:
- NAME (Text)
- CLASS (Text)
- SECTION (Text)

Instructions:
1. Return ONLY the raw SQL query—do NOT include explanations, markdown formatting (like ``` or "sql"), or any extra commentary.
2. Ensure proper SQL syntax. Use double quotes for string values if needed (e.g., CLASS = "Data Science").
3. Avoid using LIMIT or OFFSET unless explicitly requested in the question.
4. Never hallucinate column names—only use: NAME, CLASS, SECTION.
5. Your output must be a single SQL command that is syntactically valid and can run directly on a SQLite database.

Examples:

Q: How many students are there in total?  
A: SELECT COUNT(*) FROM STUDENT;

Q: Show all students enrolled in the Data Science class.  
A: SELECT * FROM STUDENT WHERE CLASS = "Data Science";

Q: List the names of students in section A.  
A: SELECT NAME FROM STUDENT WHERE SECTION = "A";

Now, based on this schema and style, convert the next question into SQL:

    """
]

# Streamlit app

st.set_page_config(page_title="I can Retrieve any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit=st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data=read_sql_query(response, "student.db")
    st.subheader("The Response is: ")
    for row in data:
        print(row)
        st.header(row)