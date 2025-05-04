# Text-to-SQL Application

This project is a **Text-to-SQL Application** that leverages Google's Gemini Generative AI to convert natural language questions into SQL queries and execute them on a SQLite database. The application is built using Python and Streamlit for a user-friendly interface.

## Features

- Converts English questions into executable SQL queries.
- Executes the generated SQL queries on a SQLite database.
- Displays the results of the queries in a Streamlit web application.
- Predefined database schema for a `STUDENT` table with columns:
  - `NAME` (Text)
  - `CLASS` (Text)
  - `SECTION` (Text)

## How It Works

1. The user inputs a question in natural language.
2. The application uses Google's Gemini Generative AI to generate a SQL query based on the question and the predefined database schema.
3. The generated SQL query is executed on the `student.db` SQLite database.
4. The results are displayed in the Streamlit interface.

## Prerequisites

- Python 3.10 or higher
- A valid Google Gemini API key (set in the `.env` file as `GOOGLE_API_KEY`).

## Installation

1. Clone the repository.
2. Install the required dependencies using `uv`:
   ```bash
   uv init
   ```
3. Set up the `.env` file with your Google Gemini API key:
   ```env
   GOOGLE_API_KEY="your_api_key_here"
   ```
4. Run the `sql.py` script to initialize the database:
   ```bash
   python sql.py
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```
2. Open the application in your browser.
3. Enter a question in the input field and click the "Ask the question" button.
4. View the SQL query results displayed in the application.

## Example Questions

- "How many students are there in total?"
- "Show all students enrolled in the Data Science class."
- "List the names of students in section A."

## Dependencies

- `streamlit`
- `google-generativeai`
- `python-dotenv`
- `sqlite3`
