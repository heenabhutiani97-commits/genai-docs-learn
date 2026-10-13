import warnings
from transformers import AutoTokenizer

#supress unnecessary warnings
warnings.filterwarnings("ignore")
print(",,,"*50)
print("GPT-2 Tokenization demo")
print(",,,"*50)


#LOAD PRETRAINED GPT-2 TOKENIZER
tokenizer=AutoTokenizer.from_pretrained("gpt2")
#GET USER INPUT

text=input("\nEnter a sentence: ").strip()


#check for empty input
if not text :
    print("\n Error: Invalid input ")
    exit()

#Generate token

tokens=tokenizer.tokenize(text)
token_ids=tokenizer.encode(text)


#DISPLAY RESULTS

print("\n" + ",,"*50)
print("original Text")

print("-"*50)
print(text)
print("\ntokens")
print("-"*50)

print(tokens)