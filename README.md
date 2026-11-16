# Structured Purchase Order (PO) Information Extractor

A hallucination-free structured information extraction pipeline that converts unstructured purchase order emails, memos, and chat messages into strict, schema-validated JSON using **Python**, **Pydantic**, **Streamlit**, and the **Google GenAI SDK (`gemini-3.5-flash-lite`)**.

## Key Features
- **Strict Pydantic Schema Enforcement:** Guarantees exact field types (`is_valid_po`, `customer_name`, `contact_email`, `items`, `required_date`, `budget_amount`, `currency`, `ambiguity_notes`).
- **Zero-Hallucination Policy:** Missing or vague details explicitly return `null` rather than guessed values, and invalid/spam/prompt-injection inputs set `is_valid_po: false`.
- **Interactive Streamlit UI:** Side-by-side unstructured text input and structured JSON viewer with built-in sample test cases.
- **24-Case Automated Evaluation Suite:** Benchmarks schema compliance, field-level exact match, and null recall across standard, missing-info, ambiguous, and invalid categories (`results/evaluation_report.md`).

## Project Structure
```text
├── prompts/
│   └── extraction_prompt.txt   # System instructions & anti-hallucination rules
├── results/
│   └── evaluation_report.md    # 24-case automated benchmark report (100% accuracy)
├── schema/
│   └── po_schema.json          # Exported JSON Schema
├── src/
│   ├── app.py                  # Streamlit web application
│   ├── extractor.py            # Gemini structured extraction client with retries
│   └── models.py               # Pydantic data models
├── tests/
│   ├── evaluate.py             # Automated evaluation runner
│   └── test_cases.json         # 24 curated test cases
└── requirements.txt