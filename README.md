# 🏦 LLM PRA COREP Reporting Assistant

## 🎯 Project Purpose

The purpose of this project is to build a **prototype reporting assistant for PRA COREP regulatory reporting**.  
It is designed to help structure, validate, and process regulatory reporting data by combining **schema-driven validation**, **document loading**, **mapping logic**, and **LLM-based assistance** within a clean Python architecture.

This project focuses on **understanding the reporting workflow**, not on UI complexity or production deployment.

---

## 🧠 Problem Context

PRA COREP reporting involves:
- Strict regulatory schemas  
- Large and complex reporting documents  
- Validation rules that must be consistently applied  
- Mapping raw data into regulator-defined structures  

Manual handling of these steps is time-consuming and error-prone.  
This project explores how a **modular Python system** can assist in automating and validating parts of this workflow.

---

## ✅ What This Project Demonstrates

- Regulatory reporting **schema handling**
- Document ingestion and preprocessing
- Data mapping and transformation logic
- Validation of COREP structures
- Separation of concerns using modular Python files
- A prototype **LLM-driven reporting assistant**
- Clean Git-based project organization

---

## 🛠️ Technologies Used

- **Python** – core implementation language  
- **LLM-based logic** – for reporting assistance (prototype level)  
- **Git & GitHub** – version control and collaboration  

---

## 📁 Repository Structure

```
llm-pra-corep-reporting-assistant/
│
│── app.py                # Entry point for running the reporting assistant
│── llm_engine.py         # Core logic for LLM-driven assistance
│── document_loader.py    # Loads and preprocesses reporting documents
│── corep_schema.py       # Defines PRA COREP schema structures
│── validator.py          # Validates data against COREP rules
│── mapper.py             # Maps raw data into COREP-compliant format
│── vector_store.py       # Handles vector storage for document retrieval
│── requirements.txt      # Project dependencies
│
│── data/                 # Sample or working data files
│── __pycache__/          # Python cache files (not relevant to logic)
│── README.md             # Project documentation
```

---

## ⚙️ How the System Works (High-Level)

1. **Document Loading**  
   Reporting documents or data sources are loaded using `document_loader.py`.

2. **Schema Definition**  
   COREP structures and rules are defined in `corep_schema.py`.

3. **Data Mapping**  
   Raw inputs are transformed into COREP-aligned formats using `mapper.py`.

4. **Validation**  
   The transformed data is validated against regulatory rules via `validator.py`.

5. **LLM Assistance**  
   `llm_engine.py` provides intelligent assistance for understanding, structuring, or querying reporting data.

6. **Execution**  
   `app.py` ties all components together into a runnable prototype.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AnilPal-Analytics/llm-pra-corep-reporting-assistant.git
cd llm-pra-corep-reporting-assistant
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
python app.py
```

---

## 🔁 Version Control Practice

This repository follows a clean Git workflow:
- Initial prototype committed clearly
- Modular files tracked independently
- Ready for iterative enhancements

---

## 🎯 Intended Use

- Regulatory reporting research & learning
- Proof-of-concept for PRA COREP automation
- Interview discussion project (regulatory + LLM)
- Foundation for future production-grade tooling

---

## 🚀 Future Enhancements

- Improved validation rule coverage
- Enhanced COREP taxonomy support
- UI layer (Streamlit or web-based)
- Better explainability for validation failures
- Integration with real reporting datasets

---

## 🔗 Project Links

- **GitHub Repository:**  
  https://github.com/AnilPal-Analytics/llm-pra-corep-reporting-assistant

- **LinkedIn:**  
  https://www.linkedin.com/in/anil-pal555

---

## 👤 Author

**Anil Pal**    

This project is a prototype developed to explore automation and assistance in PRA COREP regulatory reporting.
