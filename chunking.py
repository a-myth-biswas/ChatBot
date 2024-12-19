from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunking(data): #data is the extraction_data of sitemap_url
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1500, chunk_overlap = 300)
    docs = text_splitter.split_documents(data)
    return docs 
