# 🌾 Project Samarth – Intelligent Q&A System for Indian Agriculture & Climate Data

## 📖 Overview

**Project Samarth** is an intelligent Question-Answering (Q&A) system that enables users to ask **data-driven natural language questions** about **India’s agricultural economy and its relationship with climate patterns**.

It sources real government datasets from [data.gov.in](https://data.gov.in) and uses **Google Gemini AI**, **FastAPI**, and **Streamlit** to deliver accurate, interpretable, and traceable insights — with every answer citing the **Ministry of Agriculture & Farmers Welfare** and **India Meteorological Department (IMD)**.

---

## 🎯 Vision

Government datasets from portals like data.gov.in contain invaluable information, but are distributed across ministries in inconsistent formats. **Project Samarth** bridges this gap by:

* Integrating agricultural and climate datasets programmatically
* Allowing users to query data conversationally
* Generating Pandas-based reasoning dynamically
* Providing explainable, cited results

---

## ⚙️ System Architecture

### 🧠 Core Components

| Component              | Technology                         | Description                                                    |
| ---------------------- | ---------------------------------- | -------------------------------------------------------------- |
| **Backend API**        | FastAPI                            | Handles Q&A logic, dataset processing, and LLM communication   |
| **Frontend Interface** | Streamlit                          | Interactive chat interface for user queries                    |
| **LLM Integration**    | Google Gemini API                  | Interprets user questions and generates executable Pandas code |
| **Dataset Source**     | [data.gov.in](https://data.gov.in) | Real data from Ministry of Agriculture & IMD                   |

### 🗂️ Datasets Used

1. **[District-wise Season-wise Crop Production Statistics](https://www.data.gov.in/catalog/district-wise-season-wise-crop-production-statistics-0)**
   Source: Ministry of Agriculture & Farmers Welfare

2. **[Sub-Divisional Monthly Rainfall (1901–2017)](https://www.data.gov.in/resource/sub-divisional-monthly-rainfall-1901-2017)**
   Source: India Meteorological Department (IMD)

---

## 🧩 Directory Structure

```
Project_Samarth/
│
├── main.py                 # FastAPI backend
├── frontend.py             # Streamlit frontend
├── dataset_preprocessing.ipynb  # Preprocessing and merging datasets
├── final_dataset.csv       # Combined dataset (generated locally)
├── .env                    # Contains GEMINI_API_KEY
└── README.md               # This file
```

---

## 🧠 How It Works

1. **User asks a question** on the Streamlit interface (e.g., “Compare rainfall in Maharashtra and Karnataka over the last 5 years”).
2. **Frontend** sends the query to the **FastAPI backend** via `/ask`.
3. **Gemini API** generates executable **Pandas code** to analyze the dataset.
4. The backend **executes the code safely** on `final_dataset.csv`.
5. Gemini then summarizes results into a **human-readable explanation**, citing both sources.
6. The response and generated code are displayed interactively in the chat UI.

---

## 💻 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/project-samarth.git
cd project-samarth
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set up Environment Variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4️⃣ Run the Backend (FastAPI)

```bash
uvicorn main:app --reload
```

Server will start at:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 5️⃣ Run the Frontend (Streamlit)

```bash
streamlit run frontend.py
```

App will open at:
👉 [http://localhost:8501](http://localhost:8501)

---

## 🧮 Example Questions

| Example Query                                                                     | What It Does                                 |
| --------------------------------------------------------------------------------- | -------------------------------------------- |
| “Compare the average rainfall in Maharashtra and Karnataka for the last 5 years.” | Fetches rainfall stats from IMD data         |
| “List top 5 most produced crops in Tamil Nadu.”                                   | Aggregates crop data by production volume    |
| “Analyze the production trend of rice in West Bengal over the last decade.”       | Correlates crop yield with rainfall patterns |
| “Which district in Punjab had the highest wheat production last year?”            | Identifies top-performing districts          |

---

## 🧰 Technologies Used

* **Python 3.11+**
* **FastAPI**
* **Streamlit**
* **Pandas**
* **Google Gemini API**
* **dotenv**
* **CORS Middleware**

---

## 🔐 Core Values

| Principle                   | Implementation                                                                |
| --------------------------- | ----------------------------------------------------------------------------- |
| **Accuracy & Traceability** | Every insight is derived from official datasets and cites data.gov.in sources |
| **Data Sovereignty**        | Can run entirely on a local system without external data upload               |
| **Explainability**          | Shows generated code for transparency                                         |
| **Interactivity**           | Conversational Q&A via Streamlit chat interface                               |

---

## 🎥 Loom Submission

**Public Loom Link:**
👉 [Add your 2-minute video link here]

> In the video, demonstrate:
>
> 1. The working Q&A interface
> 2. How queries are processed end-to-end
> 3. Code generation and result explanation
> 4. The datasets and architecture decisions

---

## 🧾 Credits

* **Dataset Sources:**

  * Ministry of Agriculture & Farmers Welfare
  * India Meteorological Department (IMD)
  * [data.gov.in](https://data.gov.in)

* **Developed by:** Vaibhav Gupta

* **Project:** Samarth – Data-Driven Agriculture Intelligence Prototype
