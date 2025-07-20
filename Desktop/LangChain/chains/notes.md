##   Chains 

### 1. Simple Chain

* Pipe (`|`) style: `prompt | llm | parser`
* Best for: Linear, single-step flows
* Example: Translate a sentence or extract structured info

---

### 2. 🔁 Sequential Chain

* Runs multiple steps one after another
* Output of one step feeds into the next
* Best for: Step-by-step processing
* Example: Generate product → summarize product

---

### 3. 🔀 Parallel Chain

* Runs multiple chains at the same time
* Same input → multiple prompts/LLMs
* Best for: Multi-style generation, voting, comparisons
* Example: Pitch a product to a kid, investor, scientist

---

### 4. 🤖 Conditional Chain

* Selects a chain to run **based on logic** (input-dependent)
* Uses `RunnableBranch`
* Best for: Intent routing, dynamic workflows
* Example: If refund → refund response, if complaint → escalate

---

### 🔍 When to Use What?

| Use Case             | Chain Type        |
| -------------------- | ----------------- |
| Single task          | Simple Chain      |
| Multi-step pipeline  | Sequential Chain  |
| Multi-angle response | Parallel Chain    |
| Smart routing        | Conditional Chain |

---

### 🧰 Tips

* You can combine these (e.g. conditional + sequential)
* All chains are composable with `Runnable` API
* Use `StrOutputParser` for plain text, `PydanticOutputParser` for structured


