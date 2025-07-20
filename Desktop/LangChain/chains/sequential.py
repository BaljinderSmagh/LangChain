from langchain.chat_models   import init_chat_model
from dotenv import load_dotenv
load_dotenv()
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

#step 1 Initialize the chat model
llm=init_chat_model("gemini-2.0-flash", model_provider="google_genai")



#Step 2:Create prompt template
product_prompt=PromptTemplate(
    template='Generate a new fictional tech product idea')

parser=StrOutputParser()


summary_prompt=PromptTemplate(
    template='Summarize this product in one sentence:{product}')


#Step 3: Build the chain that combines the prompt, LLM, and output parser
chain=product_prompt | llm | parser | summary_prompt | llm | parser


#Step 4: Run the chain with an example input
result=chain.invoke({})

# Print the result
print(result)