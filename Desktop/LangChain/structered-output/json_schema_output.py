from langchain.chat_models   import init_chat_model
from dotenv import load_dotenv
load_dotenv()

# Step 1: Define JSON Schema directly (same structure as before)
product_schema = {
    "title": "ProductInfo",
    "type": "object",
    "properties": {
        "product_name": {
            "type": "string",
            "description": "The name of the product"
        },
        "brand": {
            "type": "string",
            "description": "The brand of the product"
        },
        "price": {
            "type": "number",
            "description": "The price of the product in USD"
        },
        "category": {
            "type": "string",
            "description": "Product category such as 'clothing', 'electronics', etc."
        },
        "availability": {
            "type": "string",
            "description": "Availability status, e.g. 'in stock', 'out of stock'"
        }
    },
    "required": ["product_name"]
}

# Step 2: Initialize the Chat Model
llm=init_chat_model("gemini-2.0-flash", model_provider="google_genai")


# Step 3: Wrap the model with structured output
structured_llm_output=llm.with_structured_output(product_schema)

# Step 4: Input text for the model to process
input_text = """
The SmartChef Deluxe Air Fryer by CookMaster is a premium kitchen appliance. Priced at $89.99, it features 10 cooking presets and a 6-quart basket.
Currently in stock and available in most stores.
"""
# Step 5: Invoke the model
result = structured_llm_output.invoke(input_text)

print(result)
