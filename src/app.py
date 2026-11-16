import streamlit as st
from src.extractor import extract_purchase_order

st.set_page_config(page_title="PO Structured Extractor", layout="wide")
st.title("Purchase Order Structured Information Extractor")
st.caption("Extracts strict, hallucination-free JSON from unstructured emails and messages.")

sample_options = {
    "Standard PO (Complete)": "From: procurement@abcpvt.in\nWe are ABC Pvt Ltd. We need 25 Laptops delivered by 15 October 2026. Approved budget is ₹18,00,000.",
    "Missing Budget & Email": "Hello, Zenith Corp needs 50 ergonomic office chairs by 2026-11-30. Please send a quote.",
    "Ambiguous Date & Revision": "Hi, this is Rohan from Apex Tech. Need 10 MacBook Pros—actually make that 12 units. Need them ASAP, budget around 15 lakhs.",
    "Invalid / Spam Input": "Congratulations! You have won a free vacation voucher. Click here to claim now.",
}

selected = st.selectbox("Load a sample test case:", list(sample_options.keys()))

col1, col2 = st.columns(2)
with col1:
    raw_text = st.text_area("Unstructured Input Text", value=sample_options[selected], height=220)
    run_btn = st.button("Extract Structured JSON", type="primary")

with col2:
    st.subheader("Extracted JSON Output")
    if run_btn:
        with st.spinner("Extracting..."):
            result = extract_purchase_order(raw_text)
            st.json(result.model_dump())