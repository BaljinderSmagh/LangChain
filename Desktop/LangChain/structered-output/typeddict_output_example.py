from typing import TypedDict, Annotated
from langchain.chat_models   import init_chat_model
from dotenv import load_dotenv
load_dotenv()

llm=init_chat_model("gemini-2.0-flash", model_provider="google_genai")



#provuide the structure of the output expected from a model
class ExtractedData(TypedDict):
    """
    A TypedDict for structured output.
    This can be used to define the structure of the output expected from a model.
    """
    name:str
    date: str
    location: str


class ExtractedDatawithAnnotated(TypedDict, total=False):# All fields optional
    """
    A TypedDict for structured output with optional fields.
    This can be used to define the structure of the output expected from a model.
    """
    content: Annotated[str, "Full raw text content (as-is from the document)"]
    language: Annotated[str, "Language of the content, such as 'English' or 'Spanish'"]

    

# Initialize the model with structured output
structured_output_model_1=llm.with_structured_output(ExtractedData)
structured_output_model_2=llm.with_structured_output(ExtractedDatawithAnnotated)

result=structured_output_model_1.invoke('John Smith visited London on July 15, 2023.')
#For the second model, you can use:
result_2=structured_output_model_2.invoke('LangChain is an open-source framework that helps you create applications powered by LLMs. It integrates with tools like FAISS, Chroma, OpenAI, and more.' \
'Language: English')

 
# print(result)
# print(result['name'])  
# print(result['date'])
# print(result['location'])
print(result_2) 
print(result_2.get('content'))

print(result_2.get('language'))


