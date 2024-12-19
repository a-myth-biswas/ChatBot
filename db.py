from langchain.vectorstores import FAISS
import numpy as np
import faiss
from langchain.schema import Document
import pickle
from azure_config import AzureConfig
import json


config = AzureConfig()
azure_embeddings = config.embedding_initialize()

def db_creation(docs, batch_size = 60):

    # Breaking into chunks for avoiding RateLimit Error, we can change the batch size according to document size
    batches = [docs[i:i + batch_size] for i in range(0, len(docs), batch_size)]
    
    # Create the FAISS index
    embedding_dim = 1536
    faiss_index = faiss.IndexFlatL2(embedding_dim)

    docstore = {}
    index_to_docstore_id = {}

    # Process each batch
    for batch_idx, batch in enumerate(batches):
        embeddings_batch = [azure_embeddings.embed_query(doc.page_content) for doc in batch]
        embeddings_batch = np.vstack(embeddings_batch).astype("float32")
        faiss_index.add(embeddings_batch)
        
        # docstore.update({i + batch_idx * batch_size: doc for i, doc in enumerate(batch)})
        for i, doc in enumerate(batch):
            doc_id = batch_idx * batch_size + i
            docstore[doc_id] = doc
            index_to_docstore_id[doc_id] = doc_id


    # Save the FAISS index and document store
    faiss.write_index(faiss_index, "faiss_index_test.bin")
    with open("docstore_final_test.pkl", "wb") as f:
        pickle.dump(docstore, f)
    
    with open("index_to_docstore_id.json", "w") as f:
        json.dump(index_to_docstore_id, f)
    print("Vector store saved successfully.")