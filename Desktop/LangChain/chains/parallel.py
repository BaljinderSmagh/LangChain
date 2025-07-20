
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap

# Step 1: Load local model (e.g., mistral)
llm = ChatOllama(model="mistral")
parser = StrOutputParser()

# Step 2: Define a shared input prompt for a fictional product pitch
input_template = "Pitch the product '{product_name}' to a {persona} audience."

investor_prompt = PromptTemplate.from_template(input_template).partial(persona="tech investor")
kid_prompt = PromptTemplate.from_template(input_template).partial(persona="5-year-old")
scientist_prompt = PromptTemplate.from_template(input_template).partial(persona="scientist")

# Step 3: Create 3 branches (audience-specific pitches)
investor_chain = investor_prompt | llm | parser
kid_chain = kid_prompt | llm | parser
scientist_chain = scientist_prompt | llm | parser

# Step 4: Parallel chain
parallel_chain = RunnableMap({
    "tech_investor_pitch": investor_chain,
    "kid_friendly_pitch": kid_chain,
    "scientific_pitch": scientist_chain
})

# Step 5: Run the chain
input_data = {"product_name": "DreamDuo Smart Pajamas"}
result = parallel_chain.invoke(input_data)

# Step 6: Display outputs
print("\n Audience-Specific Product Pitches:")
for audience, pitch in result.items():
    print(f"\n[{audience.replace('_', ' ').title()}]\n{pitch}")


parallel_chain.get_graph().print_ascii()