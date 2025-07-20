# What Are Output Parsers?
Output parsers in LangChain convert raw LLM responses (usually plain text or JSON) into structured Python objects — like dictionaries, lists, or Pydantic models.




## 🔧 Core Built-in Parsers
1. StrOutputParser
    * Returns raw text as a string.
    * Best for simple use cases without structure.

2. CommaSeparatedListOutputParser
    * Parses comma-separated strings into a list.
    * Useful for tags, labels, or short item lists.

3. PydanticOutputParser
    * Parses output into a validated Pydantic model.
    * Provides runtime validation and type-safe output.
    * Works best when using BaseModel with field descriptions.
    * Works well with OpenAI or Anthropic models

4. StructuredOutputParser
    * Uses a JSON schema to guide and validate model output.
    * Ideal when using non-Pydantic schemas or dynamic formats.
    * Newer, generic way to parse structured outputs
    * Supports schemas as Pydantic or JSON Schema

5. JsonOutputKeyOutputParser
    * Extracts a specific key from a JSON-formatted string.
    * Great for pinpointing a single field like answer or result.
    * Example: extract just answer from { "answer": "42" }

6. RetryWithErrorOutputParser
    * Wraps another parser and retries on failure.
    * Sends error context to the LLM to improve output.
