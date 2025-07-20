from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama


#1 Load a plain text model like Llama
# Make sure ollama server is running in the background when using LangChain.
llm = ChatOllama(model='mistral')

#2 Define a simple prompt template

prompt= PromptTemplate(template="Explain the following text in simple terms: {text}",
                       input_variables=["text"])


prompt2= PromptTemplate(template="Write a 2 line Summary on the following text. /n {text}",
                       input_variables=["text"])
#3 Create an output parser that converts the model's output to a string
output_parser = StrOutputParser()

#4 Build the chain that combines the prompt, LLM, and output parser
chain= prompt | llm | output_parser | prompt2 | llm | output_parser

#5 Run the chain with an example input
result = chain.invoke({"text": "The mitochondria is the powerhouse of the cell."})

#6 Print the result
print(result)

