from openai import OpenAI
client = OpenAI(
    api_key="",
)

# response = client.responses.create(
#     model="gpt-5.2",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

print(response.output_text)