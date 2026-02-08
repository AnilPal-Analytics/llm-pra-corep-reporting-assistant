import streamlit as st
import json

from document_loader import load_documents
from vector_store import create_vector_store
from llm_engine import generate_corep_output
from mapper import map_to_template
from validator import validate

# App title
st.title("PRA COREP Reporting Assistant (Prototype)")

# User inputs
question = st.text_area("Enter your regulatory question")
scenario = st.text_area("Enter reporting scenario")

# Button action
if st.button("Generate COREP"):

    # 1. Load regulatory documents
    docs = load_documents()

    # 2. Create vector store
    vector_db = create_vector_store(docs)

    # 3. Retrieve relevant regulatory text
    relevant_docs = vector_db.similarity_search(question, k=5)
    context = " ".join([d.page_content for d in relevant_docs])

    # 4. Call LLM
    llm_response = generate_corep_output(context, scenario)

    # 5. Parse LLM JSON output
    try:
        data = json.loads(llm_response)
    except json.JSONDecodeError:
        st.error("LLM did not return valid JSON")
        st.text(llm_response)
        st.stop()

    # 6. Show COREP template
    st.subheader("COREP Template Output")
    st.text(map_to_template(data))

    # 7. Validation
    st.subheader("Validation Results")
    errors = validate(data)
    if errors:
        st.error(errors)
    else:
        st.success("No validation errors found")

    # 8. Audit log
    st.subheader("Audit Log")
    st.json(data.get("audit_log", {}))
