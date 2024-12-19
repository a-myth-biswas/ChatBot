from sentence_transformers import SentenceTransformer, util


def rerank_documents(queries, documents, k=4):
    reranker_model = SentenceTransformer("BAAI/bge-large-en-v1.5")
    doc_texts = [doc.page_content for doc in documents]
    query_embedding = reranker_model.encode(queries, convert_to_tensor=True)
    doc_embeddings = reranker_model.encode(doc_texts, convert_to_tensor=True)
    similarities = util.cos_sim(query_embedding, doc_embeddings).squeeze(0)
    top_k_indices = similarities.argsort(descending=True)[:k]
    return [documents[i] for i in top_k_indices]
