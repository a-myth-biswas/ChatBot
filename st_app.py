import streamlit as st
from main import main_function  # Assuming the code provided is saved in `main.py`

# Streamlit app
def main():
    st.title("Changi Airport Information Chatbot")
    st.markdown("Ask any question about Changi Airport!")

    # Text input for the query
    query = st.text_input("Enter your query:", placeholder="Type your question here...")

    # Submit button
    if st.button("Get Answer"):
        if query.strip():
            try:
                st.info("Processing your query, please wait...")
                # Get the answer by calling the main_function
                answer = main_function(query)
                st.success("Answer:")
                st.write(answer)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()
