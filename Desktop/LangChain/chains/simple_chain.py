from langchain.chat_models   import init_chat_model
from dotenv import load_dotenv
load_dotenv()
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


#Step 1: Create a simple prompt template
prompt=PromptTemplate(
    template="Translate the following sentence into Spanish:\n\n{sentence}",
    input_variables=["sentence"])

#Step 2: Initialize the chat model
llm=init_chat_model("gemini-2.0-flash", model_provider="google_genai")

#Step 3: Use a basic output parser
parser=StrOutputParser()

#Step 4: Build the chain that combines the prompt, LLM, and output parser
chain=prompt | llm | parser



#step 5: Run the chain with an example input
input_text = "Hello, how are you?"
result= chain.invoke({"sentence": input_text})

#print the result
print(result)
