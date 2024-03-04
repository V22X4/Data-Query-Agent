
# Data Query Agent

This is a simple web application built using Streamlit, designed to facilitate querying data files. It allows users to upload CSV/XLSX files, run queries on them, and view the results. The application also maintains a history of past queries for reference.

## Features

1. **Upload CSV or Excel File**: Start by uploading your CSV or Excel file using the "Upload File" button.
2. **Query Execution**: Enter your query in the provided text input field and click on the "Run Query" button to execute it.
3. **View Results**: The results of the query will be displayed below.
4. **Query History**: You can view past queries and their results by expanding the "Past Queries" section. Each past query is accompanied by a "Clear" button that allows you to remove it from the history.
   

## Requirements

- Python 3.x
- Streamlit
- openai
- langchain

## Installation

1. Clone this repository:

```
git clone https://github.com/V22X4/Data-Query-Agent.git
```

2. Navigate to the project directory:

```
cd Data-Query-Agent
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:

```
streamlit run app.py
```

The application will launch in your default web browser. You can now start uploading CSV or Excel files, executing queries, and exploring the query history.
