import os
#to read rge env variables
from dotenv import load_dotenv
#to interact with openai
from openai import OpenAI

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

print("API KEY LOADED:",api_key is not None)

question=input("Ask your Data Engineer Assistant : ")  
client=OpenAI(api_key=api_key)
response=client.responses.create(
model="gpt-6-luna",
instructions="""
You are an expert Data Engineering assistant.
Explain concepts in simple language.
Focus on Python, SQL, Spark, ETL, data warehouses,
data pipelines, and cloud data engineering.
""",
input=question)

#to get complete output
#print(response)

#to get the only output from ai excluding all other fields
print(response.output_text)

print(type(response))
print(response.model_dump().keys())

print("STATUS:",response.status)
print("MODEL:",response.model)
print("USAGE:",response.usage)
#USAGE: ResponseUsage(input_tokens=15, input_tokens_details=InputTokensDetails(cache_write_tokens=0, cached_tokens=0), output_tokens=111, output_tokens_details=OutputTokensDetails(reasoning_tokens=29), total_tokens=126)

### TOKENS AND LLM COSTING

#These tokens basically tell us about the costing/usage of the LLM.

#Here `input_tokens` and `output_tokens` are basically related to whenever we prompt the LLM.

#When we give a prompt to the LLM, the tokenizer breaks the input into smaller pieces called tokens. These are counted as `input_tokens`.

#When the LLM generates the output, the generated output is also represented as tokens. These are counted as `output_tokens`.

#For example:

#Input tokens = 15
#Output tokens = 111
#Total tokens = 126

#`total_tokens = input_tokens + output_tokens`

### Reasoning Tokens

#`reasoning_tokens` tells us how many tokens were used for the model's reasoning process, based on the model/API's usage accounting.

#In our example:

#`reasoning_tokens = 29`

#This is a usage count. It does **not** mean that we can see the model's private reasoning/chain-of-thought.

### Important

#Tokens are not exactly the same as words.

#A token can be:

#* a complete word
#* part of a word
#* punctuation
#* or another piece of text

#So token count is different from word count.

#In LLM applications, token usage is important because it can affect:

#* API cost
#* context-window usage
#* response length
#* performance/latency


print("ERROR:",response.error)
print("ANSWER:",response.output_text)

