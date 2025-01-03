import pinecone
import groqcloud  # type: ignore
from sentence_transformers import SentenceTransformer

pinecone.init(api_key="pcsk_3nHUAq_4eYNeCjENNqpFdcc6mMau2vHGCSBEM2PCm42n13hQYFn5VDDXMq1Zgmy9CBv9BR", environment="us-west1-gcp")
index_name = "legal-docs"
index = pinecone.Index(index_name)
model = SentenceTransformer('all-MiniLM-L6-v2')


groq_client = groqcloud.GroqCloud(api_key="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")

def query_retriever(query, index):
    query_embedding = model.encode([query])[0]  
    results = index.query([query_embedding], top_k=3)  
    return [result['id'] for result in results['matches']]

def process_with_groqcloud(chunks):
    response = groq_client.summarize_documents(chunks)
    return response['summary']

def summarize_document(query):
    """Summarize the document based on the query."""
    try:
        chunks = query_retriever(query, index)
        summary = process_with_groqcloud(chunks)
        return summary
    
    except Exception as e:
        return f"Error during summarization: {e}"

query = "Summarize the arguments in this legal contract."
summary = summarize_document(query)
print(summary)
