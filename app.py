import streamlit as st
import pandas as pd
import os
from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI

# Initialize session state
if "past_queries" not in st.session_state:
    st.session_state.past_queries = []

def main():
    
    st.title("Data Query Agent")

    # File uploader
    uploaded_file = st.file_uploader("Upload CSV or Excel file", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        # Load file data
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        else:
            st.error("Unsupported file format. Please upload a CSV or Excel file.")
            return
        
        st.write("Uploaded file data:")
        st.write(df)

        # Backend setup
        os.environ["OPENAI_API_KEY"] = ""
        agent = create_csv_agent(OpenAI(temperature=0), uploaded_file.name, verbose=True)

        # Query input
        query = st.text_input("Enter your query:")
        
        # Buttons in a single row with reduced space
        col = st.columns(6)
        with col[0]:
            if st.button("Run Query"):
                result = agent.run(query)
                st.write("Query Result:")
                st.write(result)
                # Store query and result
                st.session_state.past_queries.append((query, result))
        with col[1]:
            if st.button("Clear"):
                query = ""  # Clear the query input field

        # Display past queries
        st.write("")
        st.write("Past Queries")
        with st.expander("Past Queries", expanded=False):
            for i, (past_query, past_result) in enumerate(st.session_state.past_queries):
                st.write(f"Query: {past_query}")
                st.write(f"Result: {past_result}")
                # Add a "Clear" button next to each query
                if st.button(label="Clear", key=f"clear_button_{i}"):
                    del st.session_state.past_queries[i]

if __name__ == "__main__":
    main()
