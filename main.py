from webscraper import load_data
from chunking import chunking
from db import db_creation
from azure_config import AzureConfig
from retriever import retrieve_documents
from reranker import rerank_documents
from llm import get_final_response

changiairport_url = "https://www.changiairport.com/sitemap.xml"
def main_function(query):
    # print("process started")
    # data = load_data(sitemap_url=changiairport_url)
    # print("data loaded")
    # docs = chunking(data=data)
    # print("chunking done")
    # db_creation(docs)
    # print("db creation done, with index creation, id and document store")
    good_docs = retrieve_documents(query)
    print("document retrieved for given query")
    reranked_docs = rerank_documents(query, good_docs, k = 4)
    print("got reranked document")
    answer = get_final_response(reranked_docs, query)
    print("response generated by llm")
    return answer


if __name__=="__main__":
    answer = main_function(query="give a brief on changi airport")
    print(answer)