from typing import Annotated
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain.output_parsers import PydanticOutputParser
from langchain_openai import OpenAI
# from textwrap import dedent
from llm_wrapper import llm_func
from spr_parser.parser import SPREncodingOutputParser, SPRDecodingOutputParser
from pydantic import BaseModel, Field


from langchain_core.output_parsers import BaseOutputParser
# Initialize Ollama
def initialize_ollama(model='openhermes', verbose=False):
    print(f"Initializing LLM model: {model}")
    if model == 'openai':
        llm = OpenAI()
    else:
        llm = Ollama(model=model, verbose=verbose, )
    return llm


llm_openai=initialize_ollama(model='openai')
llm_openhermes=initialize_ollama(model='openhermes')
#llm_openhermes = llm_openai


    

enc_parser = SPREncodingOutputParser({"llm" :llm_openhermes})
dec_parser = SPRDecodingOutputParser({"llm" : llm_openhermes})
prompt = PromptTemplate(
            template="{query}\n",
            input_variables=["query"]
        )
chain = prompt | llm_openhermes 
config = {"query": f"Write the biography of Abraham Lincoln."}
print(f"Query: {config['query']}")
response = chain.invoke(config)
print(response)
print("###############")
print("Encoding")
response_enc = enc_parser.parse(response)
print(response_enc)
print("###############")
print("Decoding")
response_dec = dec_parser.parse(response_enc)
print(response_dec)