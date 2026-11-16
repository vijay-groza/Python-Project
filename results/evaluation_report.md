# Evaluation Report — Structured PO Extractor

## Summary Metrics (24 Test Cases)
| Metric | Score |
| :--- | :---: |
| **JSON Schema Compliance** | 100.0% (24/24) |
| **Scalar Field Exact Match** | 100.0% (144/144) |
| **Null Recall (Anti-Hallucination)** | 100.0% (63/63) |
| **Hallucination Rate (False Non-Nulls)** | 0.0% |
| **Valid/Invalid PO Classification** | 100.0% (24/24) |

## Per-Case Results
| Test ID | Category | Result | Valid PO | Extracted Customer | Extracted Budget |
| :--- | :--- | :---: | :---: | :--- | :---: |
| TC_01_STD_BASIC | standard | PASS | True | ABC Pvt Ltd | 1800000.0 |
| TC_02_STD_MULTI_ITEM | standard | PASS | True | Nova Logistics | 2500.0 |
| TC_03_STD_EUR | standard | PASS | True | EuroTech GmbH | 12000.0 |
| TC_04_STD_GBP | standard | PASS | True | Thames Retail Ltd | 45000.0 |
| TC_05_STD_FORMAL_MEMO | standard | PASS | True | Sri Venkateswara Auto Components | 90000.0 |
| TC_06_STD_SHORT_MSG | standard | PASS | True | MedCare Clinics | 900.0 |
| TC_07_MISS_BUDGET | missing_info | PASS | True | Zenith Corp | None |
| TC_08_MISS_DATE | missing_info | PASS | True | Orbit Systems | 1250000.0 |
| TC_09_MISS_CUSTOMER | missing_info | PASS | True | None | 45000.0 |
| TC_10_MISS_QUANTITY | missing_info | PASS | True | BlueWave Exports | None |
| TC_11_MISS_ONLY_ITEM | missing_info | PASS | True | None | None |
| TC_12_MISS_NO_UNIT_PRICE | missing_info | PASS | True | GreenLeaf Foods | None |
| TC_13_AMB_VAGUE_DATE | ambiguous | PASS | True | Apex Manufacturing | None |
| TC_14_AMB_REVISION | ambiguous | PASS | True | Starlight Studios | None |
| TC_15_AMB_NEXT_WEEK | ambiguous | PASS | True | Metro Builders | None |
| TC_16_AMB_TBD_BUDGET | ambiguous | PASS | True | Delta Pharma | None |
| TC_17_AMB_CONDITIONAL | ambiguous | PASS | True | PixelWorks | None |
| TC_18_AMB_MIXED_LANGUAGE | ambiguous | PASS | True | Surya Textiles | 200000.0 |
| TC_19_INV_EMPTY | invalid | PASS | False | None | None |
| TC_20_INV_SPAM | invalid | PASS | False | None | None |
| TC_21_INV_HR_LEAVE | invalid | PASS | False | None | None |
| TC_22_INV_OTP | invalid | PASS | False | None | None |
| TC_23_INV_GIBBERISH | invalid | PASS | False | None | None |
| TC_24_INV_PROMPT_INJECTION | invalid | PASS | False | None | None |