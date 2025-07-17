Structured Output Comparison: TypedDict vs Pydantic vs JSON Schema
This project demonstrates three ways to define structured output schemas for use with LangChain’s with_structured_output() function.

✅ 1. TypedDict (Python built-in)
✔️ Simple and lightweight

⚠️ No runtime validation

⚠️ No default values or nested model support

✅ Good for quick prototyping or static type checking

When to use:

You want minimal setup and Python-only typing

Ideal for small internal tools, demos, and fast experimentation

✅ 2. Pydantic (Python class-based schema)
✅ Supports runtime validation and parsing

✅ Allows default values, descriptions, and nested fields

✅ Converts easily to JSON Schema

✅ Provides rich developer experience and integrations

When to use:

You need robust validation or field control

Suitable for production APIs, LangChain agents, or external model interfaces

✅ 3. JSON Schema (language-agnostic schema format)
✅ Works across programming languages and platforms

✅ Supports rich schema definitions and validation rules

⚠️ Not type-safe in Python directly (must be interpreted)

When to use:

You generate schema dynamically

You’re building tools that interact with OpenAPI, Swagger, or frontend systems

You need full schema control without Python class definitions

| Feature              | TypedDict             | Pydantic        | JSON Schema                       |
| -------------------- | --------------------- | --------------- | --------------------------------- |
| Type-safe in Python  | ✅                     | ✅               | ❌                                 |
| Runtime validation   | ❌                     | ✅               | ✅ (external tools)                |
| Default values       | ❌                     | ✅               | ✅                                 |
| Nested support       | ⚠️ Manual              | ✅               | ✅                                 |
| Descriptions         | ✅ (with extra typing) | ✅               | ✅                                 |
| LangChain compatible | ✅                     | ✅               | ✅                                 |
| Best for             | Prototypes            | Production APIs | Cross-language or dynamic systems |
