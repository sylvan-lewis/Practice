import openai
import os

# Set your API key from an environment variable for security
openai.api_key = os.getenv("OPENAI_API_KEY")

# Sample legal draft content (could be replaced with file input or database retrieval)
legal_draft = """
This Agreement is entered into between the Client and the Provider, effective as of the date signed. 
The Provider shall render services as outlined in Exhibit A, subject to the terms of compensation, liability, 
and confidentiality stated herein. Disputes arising under this Agreement shall be governed by the laws 
of the Province of Ontario.
"""

def ask_legal_question(draft_text: str, question: str) -> str:
    """Queries GPT-4 with the legal draft and user question, returns a focused legal answer."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": (
                    "You are a legal assistant trained in Canadian contract law. "
                    "Use only the provided draft text to answer legal questions. Be precise, concise, and do not fabricate."
                )},
                {"role": "user", "content": f"Legal Draft:\n{draft_text}"},
                {"role": "user", "content": f"Question: {question}"}
            ],
            temperature=0.3,
            max_tokens=500
        )
        answer = response.choices[0].message['content'].strip()
        return answer
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("📄 Legal Draft Question Answering Tool")
    print("Type a question related to the draft. Type 'exit' to quit.\n")

    while True:
        question = input("Ask your legal question: ")
        if question.lower() in ('exit', 'quit'):
            print("Goodbye.")
            break
        answer = ask_legal_question(legal_draft, question)
        print("\n📌 Answer:")
        print(answer)
        print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    main()
