import os
import time
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import errors, types
from src.models import PurchaseOrder

load_dotenv()

SYSTEM_PROMPT = Path("prompts/extraction_prompt.txt").read_text(encoding="utf-8")
MODELS_TO_TRY = ["gemini-3.5-flash-lite", "gemini-3.8-flash"]


def get_client() -> genai.Client:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or "paste_your" in api_key:
        raise ValueError("Missing GEMINI_API_KEY in .env file.")
    return genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(timeout=15_000),
    )


def extract_purchase_order(raw_text: str) -> PurchaseOrder:
    if not raw_text or not raw_text.strip():
        return PurchaseOrder(
            is_valid_po=False,
            ambiguity_notes="Empty or whitespace-only input.",
        )

    client = get_client()
    last_error = None

    for attempt in range(4):
        for model_name in MODELS_TO_TRY:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=raw_text,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        response_mime_type="application/json",
                        response_schema=PurchaseOrder,
                        temperature=0.0,
                    ),
                )
                return PurchaseOrder.model_validate_json(response.text)
            except (errors.ServerError, errors.ClientError, Exception) as e:
                last_error = e
                continue
        time.sleep(2 * (attempt + 1))

    raise RuntimeError(f"Extraction failed: {last_error}")


if __name__ == "__main__":
    sample_email = (
        "Hi Team, We are ABC Pvt Ltd (procurement@abcpvt.in). "
        "Please supply 25 Laptops by 15 October 2026. "
        "Our approved budget is ₹18,00,000."
    )
    extracted = extract_purchase_order(sample_email)
    print(extracted.model_dump_json(indent=2))