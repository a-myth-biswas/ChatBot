# Changi Airport Information Chatbot

This project implements a RAG based ChatBot pipeline utilizing Azure OpenAI embeddings, FAISS for vector storage, and a retrieval and reranking mechanism for querying documents efficiently, and Azure OpenAI API for LLM response. Below is a guide to understanding and using this system.

---

## Features

- **Web Scraping:** Extracts data from a provided website/sitemap.
- **Document Chunking:** Splits large documents into manageable chunks for embedding.
- **Vector Storage:** Creates and stores document embeddings using FAISS.
- **Retrieval:** Fetches the most relevant documents for a given query.
- **Reranking:** Optimizes the order of retrieved documents based on similarity scores with Sentence Transformer model.
- **Integration with Azure OpenAI:** Utilizes Azure OpenAI for final response generation.

---

## Project Structure

### Files and Directories

1. **webscraper.py**

   - Handles web scraping to extract data from a given sitemap.
   - Function: `load_data(sitemap_url)`.

2. **chunking.py**

   - Splits large documents into smaller, manageable chunks for embedding.
   - Function: `chunking(data)`.

3. **db.py**

   - Creates FAISS index and document store.
   - Generates mappings between index and document IDs.
   - Function: `db_creation(docs, batch_size=60)`.

4. **azure\_config.py**

   - Initializes and configures Azure OpenAI embeddings and LLM.
   - Class: `AzureConfig`.

5. **retriever.py**

   - Retrieves documents based on FAISS similarity search.
   - Function: `retrieve_documents(query, k=12)`.

6. **reranker.py**

   - Reranks retrieved documents using a sentence transformer model.
   - Function: `rerank_documents(queries, documents, k=4)`.

7. **llm.py**

   - Generates final responses using a language model.
   - Function: `get_final_response(top_docs, query)`.

8. **app.py**

   - FastAPI application for serving the search system as a REST API.

9. **docstore_final_test.pkl**

   - Stores the serialized document store.

10. **faiss_index_test.bin**

    - Stores the FAISS index for vector embeddings.

11. **index_to_docstore_id.json**

    - Maps FAISS indices to document store IDs.

---

## Setup Instructions

### Prerequisites

- Python 3.10+
- Azure OpenAI subscription with an embedding model configured.
- Libraries: `langchain`, `faiss`, `numpy`, `pickle`, `fastapi`, `uvicorn`, `requests`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/a-myth-biswas/ChatBot.git
   cd chatbot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure Azure:

   - Update `azure_config.py` with your Azure credentials and embedding model details.

4. Run the FastAPI server:

   ```bash
   uvicorn app:app --reload
   ```

---

## Usage

### 1. Load and Preprocess Data

- Use `load_data()` to scrape the sitemap and extract raw data.
- Use `chunking()` to break data into chunks for embedding.

### 2. Create Database and Index

- Call `db_creation()` to create FAISS index and document store:
  ```python
  from db import db_creation
  db_creation(docs)
  ```

### 3. Query Documents

- Use `retrieve_documents()` to fetch documents based on a query:
  ```python
  from retriever import retrieve_documents
  results = retrieve_documents(query="Your Query Here")
  ```

### 4. Rerank Results

- Call `rerank_documents()` to refine the order of results:
  ```python
  from reranker import rerank_documents
  reranked_docs = rerank_documents(query, results, k=4)
  ```

### 5. Generate Response

- Use `get_final_response()` to generate the final output from top documents:
  ```python
  from llm import get_final_response
  response = get_final_response(reranked_docs, query)
  print(response)
  ```

### 6. REST API

- Send a POST request to the FastAPI endpoint with the query:
  ```bash
  curl -X POST "http://0.0.0.0:8503/query" -H "Content-Type: application/json" -d '{"query": "Your Query Here"}'
  ```

---

### 7. STreamlit Application
- Use command "streamlit run st_app.py" to run a streamlit application for a userfriendy UI.

## Example Workflow

1. Scrape data from the sitemap:

   ```python
   data = load_data(sitemap_url="https://www.changiairport.com/sitemap.xml")
   ```

2. Chunk the data:

   ```python
   docs = chunking(data)
   ```

3. Create the database:

   ```python
   db_creation(docs)
   ```

4. Query and rerank:

   ```python
   good_docs = retrieve_documents(query="What are the amenities at Changi Airport?")
   reranked_docs = rerank_documents(query="What are the amenities at Changi Airport?", documents=good_docs)
   ```

5. Generate the final response:

   ```python
   answer = get_final_response(reranked_docs, "What are the amenities at Changi Airport?")
   print(answer)
   ```

---

## Notes

1. Ensure your Azure OpenAI configuration is correct in `azure_config.py`.
2. Adjust `batch_size` in `db_creation()` based on document size to avoid rate limits.
3. To handle large document volumes, monitor FAISS and memory usage during index creation.

---

## License

This project is open-source. Feel free to use and modify it as per your needs.

---

## Contributions

Contributions are welcome! Please submit a pull request or raise an issue to contribute.

---

## Contact

For any queries or issues, reach out at: [[www.biswasamit@gmail.com](mailto\:www.biswasamit@gmail.com)]

