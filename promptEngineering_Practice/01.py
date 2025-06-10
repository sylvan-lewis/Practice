import openai
#Free Tier API Key- Replace to run the code
#openai.api_key = "API-KEY-HERE"
def simple_summarize(text):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Summarize this legal text:\n\n" + text}
        ]
    )
    return response.choices[0].message.content

legal_text = """
This agreement is made between the Company and the Contractor. The Contractor agrees to provide services starting June 1, 2025, for a duration of 12 months. Payment terms include monthly invoicing.
"""

summary = simple_summarize(legal_text)
print("Summary:\n", summary)