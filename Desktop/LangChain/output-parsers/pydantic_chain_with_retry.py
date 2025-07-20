from pydantic import BaseModel, Field
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser, RetryWithErrorOutputParser
from langchain.chains import LLMChain

# Step 1: Define the structured schema
class Product(BaseModel):
    name: str = Field(description="The product name")
    category: str = Field(description="The product category")
    price: float = Field(description="The product price in USD")

# Step 2: Create the base parser
base_parser = PydanticOutputParser(pydantic_object=Product)

# Step 3: Initialize LLM
llm = ChatOllama(model="mistral")

# Step 4: Create prompt template with format instructions
prompt = PromptTemplate(
    template="Describe a fictional product as JSON with the following fields:\n{format_instructions}\n\n{query}",
    input_variables=["query"],
    partial_variables={"format_instructions": base_parser.get_format_instructions()}
)

# Step 5: Create the retry parser
parser = RetryWithErrorOutputParser.from_llm(
    parser=base_parser,
    llm=llm
)

# Step 6: Create and execute the chain using LLMChain
llm_chain = LLMChain(llm=llm, prompt=prompt)

chain = (
    {"query": lambda x: "Create a fictional tech product"}
    | llm_chain
    | (lambda x: parser.parse_with_prompt(x["text"], prompt))
)

try:
    # Execute the chain
    result = chain.invoke({})
    
    # Print the results
    print("\nParsed with Retry Logic:")
    print(f"Name: {result.name}")
    print(f"Category: {result.category}")
    print(f"Price: ${result.price}")
except Exception as e:
    print(f"Error in chain execution: {e}")