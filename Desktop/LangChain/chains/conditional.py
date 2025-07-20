# 📄 03_chains/conditional_chain.py

from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
from langchain.prompts import PromptTemplate

# Step 1: Load local model
llm = ChatOllama(model="mistral")
parser = StrOutputParser()

# Step 2: Define -style prompts
# - If input is a refund request → give refund policy
# - If input is a complaint → acknowledge and escalate
# - Else → general chatbot response

refund_prompt = PromptTemplate.from_template( "A customer is asking for a refund. Politely explain the refund policy:{input}")

complaint_prompt = PromptTemplate.from_template(
    "The following is a customer complaint. Acknowledge the issue and inform them it has been escalated:{input}")

general_prompt = PromptTemplate.from_template(
    "Respond helpfully to the customer's inquiry:{input}")

refund_chain = refund_prompt | llm | parser
complaint_chain = complaint_prompt | llm | parser
general_chain = general_prompt | llm | parser

# Step 3: Define condition functions
def is_refund_request(input: dict) -> bool:
    return "refund" in input["input"].lower()

def is_complaint(input: dict) -> bool:
    keywords = ["not working", "broken", "delay", "missing", "complaint", "frustrated"]
    return any(word in input["input"].lower() for word in keywords)

# Step 4: Create conditional chain
conditional_chain = RunnableBranch(
    (is_refund_request, refund_chain),
    (is_complaint, complaint_chain),
    RunnableLambda(lambda _: True, general_chain)
)

# Step 5: Try real-use-case examples
examples = [
    {"input": "I’d like a refund for the item I purchased last week."},
    {"input": "My order arrived broken and I’m really frustrated."},
    {"input": "What’s your shipping timeline for California?"}
]

for ex in examples:
    print(f"\n Input: {ex['input']}")
    output = conditional_chain.invoke(ex)
    print(f"Output: {output}")
