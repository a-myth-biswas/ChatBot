from azure_config import AzureConfig
from utils import load_resources
import numpy as np

config = AzureConfig()
azure_embeddings = config.embedding_initialize()


def retrieve_documents(query, k=12):
    """Retrieve top-k documents for the query using Azure embeddings"""
    # Load resources
    docstore, faiss_index, index_to_docstore_id = load_resources()

    # Generate query embedding using Azure embeddings
    query_embedding = azure_embeddings.embed_query(query)
    
    # Convert query embedding to numpy float32 (required for FAISS)
    query_embedding = np.array(query_embedding, dtype="float32").reshape(1, -1)
    
    # Ensure the query embedding matches FAISS index dimensions
    if query_embedding.shape[1] != faiss_index.d:
        raise ValueError(f"Dimension mismatch: query embedding ({query_embedding.shape[1]}) "
                         f"and FAISS index ({faiss_index.d}) do not match.")
    
    # Perform similarity search in the FAISS index
    _, indices = faiss_index.search(query_embedding, k)  # Get top-k results
    
    # Retrieve document IDs from the indices and map them to docstore
    retrieved_docs = []
    for idx in indices[0]:
        # Ensure index is valid
        if str(idx) in index_to_docstore_id:
            doc_id = index_to_docstore_id[str(idx)]
            doc = docstore.get(doc_id, None)
            if doc:
                retrieved_docs.append(doc)
    
    if not retrieved_docs:
        print("No documents retrieved.")
    else:
        print(f"Retrieved {len(retrieved_docs)} documents.")
    
    return retrieved_docs
