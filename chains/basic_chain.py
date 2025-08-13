# chains/basic_chain.py
from langchain.prompts import PromptTemplate
# from langchain.llms import Ollama
# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM



def run_chain(prompt_text):
    # llm = Ollama(model="llama2")
    llm = OllamaLLM(model="llama2")
    prompt = PromptTemplate.from_template("Answer clearly: {question}")
    chain = prompt | llm
    return chain.invoke({"question": prompt_text})
