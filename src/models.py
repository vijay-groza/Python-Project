import json
from pathlib import Path
from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class LineItem(BaseModel):
    product_name: Optional[str] = Field(
        None, description="Name or model of the requested product; null if unclear"
    )
    quantity: Optional[int] = Field(
        None, description="Exact numeric quantity requested; null if not specified"
    )
    unit_price: Optional[float] = Field(
        None, description="Explicit price per unit if stated; otherwise null"
    )


class PurchaseOrder(BaseModel):
    is_valid_po: bool = Field(
        ...,
        description="True if the text represents a valid purchase order or procurement enquiry; False if spam, irrelevant, or gibberish",
    )
    customer_name: Optional[str] = Field(
        None, description="Company or buyer name placing the order; null if not stated"
    )
    contact_email: Optional[str] = Field(
        None, description="Contact email address if explicitly present; null otherwise"
    )
    items: List[LineItem] = Field(
        default_factory=list,
        description="List of line items requested; empty list if none found",
    )
    required_date: Optional[str] = Field(
        None,
        description="Delivery deadline normalized to YYYY-MM-DD; null if missing or vague (e.g., 'ASAP')",
    )
    budget_amount: Optional[float] = Field(
        None,
        description="Total numeric budget without currency symbols or commas; null if not stated",
    )
    currency: Optional[Literal["INR", "USD", "EUR", "GBP"]] = Field(
        None,
        description="ISO currency code if budget/price is stated; null if no monetary amount exists",
    )
    ambiguity_notes: Optional[str] = Field(
        None,
        description="Notes on vague deadlines, conflicting revisions, or missing critical info; null if clean",
    )


def export_json_schema(output_path: str = "schema/po_schema.json") -> None:
    schema_dict = PurchaseOrder.model_json_schema()
    Path(output_path).write_text(json.dumps(schema_dict, indent=2), encoding="utf-8")
    print(f"Schema exported to {output_path}")


if __name__ == "__main__":
    export_json_schema()