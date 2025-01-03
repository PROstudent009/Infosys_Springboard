import pinecone
from sentence_transformers import SentenceTransformer
from ingestion import cleaned_text

pinecone.init(api_key="pcsk_3nHUAq_4eYNeCjENNqpFdcc6mMau2vHGCSBEM2PCm42n13hQYFn5VDDXMq1Zgmy9CBv9BR", environment="us-west1-gcp")
index_name = "legal-docs"

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_index(index_name):
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(index_name, dimension=768) 
    return pinecone.Index(index_name)

def index_document(text, index):
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    embeddings = model.encode(chunks)  
    ids = [str(i) for i in range(len(chunks))]
    
    index.upsert(vectors=zip(ids, embeddings))
    return ids, embeddings

index = create_index(index_name)
ids, embeddings = index_document(cleaned_text, index)
