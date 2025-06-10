import os
import openai

#Free Tier API Key- Replace to run the code
#openai.api_key = "API-KEY-HERE"

def summarize_and_extract(text):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant specialized in summarizing legal documents."
        },
        {
            "role": "user",
            "content": (
                "Please summarize the following legal document in a concise paragraph, "
                "and then extract 3 key bullet points from it:\n\n" + text
            )
        }
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=300,
        temperature=0.5,
    )
    
    # Extract the assistant's reply
    return response.choices[0].message.content

if __name__ == "__main__":
    legal_text = """
    This Agreement is entered into by and between Party A and Party B. Party A agrees to provide services as outlined in Schedule A.
    Party B shall compensate Party A according to the terms stated in Schedule B. Both parties agree to confidentiality and dispute resolution clauses.
    The term of this agreement is one year, with an option to renew upon mutual consent.
    """
    
    result = summarize_and_extract(legal_text)
    print("\n=== Summary & Key Points ===\n")
    print(result)
