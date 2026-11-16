import json
import time
from pathlib import Path
from src.extractor import extract_purchase_order


def run_evaluation():
    test_cases = json.loads(Path("tests/test_cases.json").read_text(encoding="utf-8"))
    total = len(test_cases)
    schema_valid_count = 0
    valid_flag_correct = 0
    null_expected_total = 0
    null_predicted_correct = 0
    field_total = 0
    field_exact_matches = 0
    rows = []

    scalar_fields = [
        "is_valid_po",
        "customer_name",
        "contact_email",
        "required_date",
        "budget_amount",
        "currency",
    ]

    for idx, tc in enumerate(test_cases, start=1):
        print(f"[{idx}/{total}] Running {tc['id']}...")
        pred_obj = extract_purchase_order(tc["input_text"])
        schema_valid_count += 1
        pred = pred_obj.model_dump()
        exp = tc["expected"]

        if pred["is_valid_po"] == exp["is_valid_po"]:
            valid_flag_correct += 1

        case_matches = 0
        for f in scalar_fields:
            field_total += 1
            exp_val = exp[f]
            pred_val = pred[f]

            if exp_val is None:
                null_expected_total += 1
                if pred_val is None:
                    null_predicted_correct += 1

            if isinstance(exp_val, str) and isinstance(pred_val, str):
                match = exp_val.strip().lower() == pred_val.strip().lower()
            else:
                match = exp_val == pred_val

            if match:
                field_exact_matches += 1
                case_matches += 1

        status = "PASS" if case_matches == len(scalar_fields) else f"PARTIAL ({case_matches}/{len(scalar_fields)})"
        rows.append(
            f"| {tc['id']} | {tc['category']} | {status} | {pred['is_valid_po']} | {pred['customer_name']} | {pred['budget_amount']} |"
        )
        time.sleep(0.5)

    schema_rate = (schema_valid_count / total) * 100
    field_acc = (field_exact_matches / field_total) * 100
    null_recall = (null_predicted_correct / null_expected_total) * 100 if null_expected_total else 100.0
    hallucination_rate = 100.0 - null_recall
    valid_acc = (valid_flag_correct / total) * 100

    report = f"""# Evaluation Report — Structured PO Extractor

## Summary Metrics ({total} Test Cases)
| Metric | Score |
| :--- | :---: |
| **JSON Schema Compliance** | {schema_rate:.1f}% ({schema_valid_count}/{total}) |
| **Scalar Field Exact Match** | {field_acc:.1f}% ({field_exact_matches}/{field_total}) |
| **Null Recall (Anti-Hallucination)** | {null_recall:.1f}% ({null_predicted_correct}/{null_expected_total}) |
| **Hallucination Rate (False Non-Nulls)** | {hallucination_rate:.1f}% |
| **Valid/Invalid PO Classification** | {valid_acc:.1f}% ({valid_flag_correct}/{total}) |

## Per-Case Results
| Test ID | Category | Result | Valid PO | Extracted Customer | Extracted Budget |
| :--- | :--- | :---: | :---: | :--- | :---: |
""" + "\n".join(rows)

    Path("results/evaluation_report.md").write_text(report, encoding="utf-8")
    print("\nSaved evaluation report to results/evaluation_report.md")
    print(f"Schema Compliance: {schema_rate:.1f}% | Field Accuracy: {field_acc:.1f}% | Hallucination Rate: {hallucination_rate:.1f}%")


if __name__ == "__main__":
    run_evaluation()