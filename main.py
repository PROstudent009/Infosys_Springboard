from summarizer import generate_summary

if __name__ == "__main__":
    user_query = "Summarize the contract clauses on termination."
    summary = generate_summary(user_query)
    print(f"Summary: {summary}")
