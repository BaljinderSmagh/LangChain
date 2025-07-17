from pydantic import BaseModel, Field #data validation library
from typing import Optional
from langchain.chat_models   import init_chat_model
from dotenv import load_dotenv
load_dotenv()


# Step 1: Define a Retail Schema using Pydantic
class ProductInfo(BaseModel):
    product_name: str = Field(description="The name of the product")
    brand: Optional[str] = Field(default=None, description="The brand of the product")
    price: Optional[float] = Field(default=None, description="The price of the product in USD")
    category: Optional[str] = Field(default=None, description="Product category such as 'clothing', 'electronics', etc.")
    availability: Optional[str] = Field(default=None, description="Availability status, e.g. 'in stock', 'out of stock'")

# Step 2: Initialize the Chat Model
llm=init_chat_model("gemini-2.0-flash", model_provider="google_genai")


# Step 3: Wrap the model with structured output
structured_llm_output=llm.with_structured_output(ProductInfo)

# Step 4: Provide some retail product text to extract from
input_text = """
Introducing the all-new Echo SoundBar by EchoTech. With immersive surround sound and deep bass, this device is perfect for home theaters.
Currently available for just $129.99. Limited stock left!
"""
# Step 5: Invoke the model to extract structured data
result=structured_llm_output.invoke(input_text)

# Step 6: Print the structured output
print(result)
print(f"Product Name: {result.product_name}")
print(f"Brand: {result.brand}")
print(f"Price: ${result.price}")
print(f"Category: {result.category}")
print(f"Availability: {result.availability}")
