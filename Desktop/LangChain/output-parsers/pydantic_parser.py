from pydantic import BaseModel, Field
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

# Step 1: Define your structured schema
class Product(BaseModel):
    name: str = Field(description="The product name")
    category: str = Field(description="The product category")
    price: float = Field(description="The product price in USD")

# Step 2: Initialize the Pydantic parser
parser = PydanticOutputParser(pydantic_object=Product)

# Step 3: Set up prompt with format instructions
prompt = PromptTemplate(
    template="Describe a product in JSON format with the following fields:\n{format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Step 4: Connect to a local model like Mistral via Ollama
llm = ChatOllama(model="mistral")  # Make sure `ollama run mistral` is active

# Step 5: Run prompt through the model and parse the output
chain = prompt | llm | parser
result = chain.invoke({})
# response = llm.invoke(prompt.format())
# parsed = parser.parse(response.content)

# Step 6: Display the result
print(result)
# print("Parsed Product Info:")
# print(type(parsed))
# print(f"Name: {parsed.name}")
# print(f"Category: {parsed.category}")
# print(f"Price: ${parsed.price}")
