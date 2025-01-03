from rag_pipeline import summarize_document

def generate_summary(query):
    summary = summarize_document(query)
    return summary

# Test the summarization with user input
query = "Summarize the main points of the contract regarding confidentiality."
summary = generate_summary(query)
print(summary)
