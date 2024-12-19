from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers.json import SimpleJsonOutputParser
from langchain_core.output_parsers.string import StrOutputParser
from azure_config import AzureConfig
config = AzureConfig()
llm = config.llm_initialize()

template_gpt = """
You are an intelligent bot, expert in providing information about Jewel Changi Airport. 
Understand the question properly and generate the response succinctly and accurately. 
If the question asks for details about specific locations, services, or events, provide the relevant information clearly. 
If asked about attractions, amenities, or specific areas within the airport, focus the response on the most relevant sections. 
The response should be based solely on the relevant documents retrieved from the Jewel Changi Airport website, without adding any additional context.
Please convert any double quotes to single quotes in the response. 
Only provide the exact information asked for; do not add extra details.
The response should be based solely on the relevant documents retrieved, without adding any additional context.

---------------------------
Context : {context},
---------------------------
Question : {query},
---------------------------
Response :
"""

prompt_gpt = PromptTemplate(
    input_variables=["context", "query"],
    template=template_gpt,
)


# Function to get the final response
def get_final_response(top_docs, query):
    # Combine the documents' text into the context for the prompt
    context = "\n\n".join([doc.page_content for doc in top_docs])
    json_parser = SimpleJsonOutputParser()
    str_parser = StrOutputParser()
    chain = prompt_gpt | llm | str_parser
    response = chain.invoke({"context": context, "query": query})
    # Create the RunnableSequence to combine the prompt and the LLM
    # qa_sequence = RunnableSequence([prompt_gpt, llm])

    # # Execute the sequence to generate the response
    # response = qa_sequence.invoke({"context": context, "query": query})

    return response
