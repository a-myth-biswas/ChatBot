import pickle
import faiss
import json

def load_resources():
    """Load FAISS index, document store, and index-to-docstore ID mapping"""
    # Load docstore (Document store containing the actual documents)
    with open('docstore_final_test.pkl', 'rb') as f:
        docstore = pickle.load(f)

    # Load FAISS index
    faiss_index = faiss.read_index('faiss_index_test.bin')

    # Load index to docstore id mapping
    with open('index_to_docstore_id.json', 'r') as f:
        index_to_docstore_id = json.load(f)

    return docstore, faiss_index, index_to_docstore_id
