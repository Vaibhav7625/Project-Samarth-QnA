import os
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import traceback
from dotenv import load_dotenv

load_dotenv()

# Fetch API keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

df = pd.read_csv("final_dataset.csv")

app = FastAPI(title="Project Samarth - Intelligent Q&A System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conversation_history = []

def ask_gemini(prompt: str):
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    response = model.generate_content(prompt)
    return response.text.strip()

def safe_execute(code: str, df: pd.DataFrame):
    local_vars = {"df": df.copy()}
    try:
        exec(code, {}, local_vars)
        result = local_vars.get("result", None)
        return result
    except Exception as e:
        traceback.print_exc()
        return f"Error executing code: {e}"

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    user_query = data.get("query", "")

    conversation_history.append({"role": "user", "content": user_query})
    last_context = "\n".join([f"{m['role']}: {m['content']}" for m in conversation_history[-4:]])

    # --- Step 1: Gemini generates Pandas code ---
    system_prompt = f"""
    You are a data analyst AI for Indian Agriculture.
    You have a dataframe df with columns:
    state_name, crop_year, season, crop, area_, production_, yield_, rainfall_mm.

    Generate **only executable Python code** using df to answer the user's question.
    Assign your final output to a variable called 'result'.
    Do not print or explain.
    Example:
        result = df.groupby('state_name')['rainfall_mm'].mean()
    """

    code_prompt = f"{system_prompt}\nUser question: {user_query}\nChat history: {last_context}"
    code = ask_gemini(code_prompt)

    # --- Step 2: Execute Pandas code ---
    exec_result = safe_execute(code, df)

    explanation_prompt = f"""
    You are a data analyst. 

    The user asked: "{user_query}".
    The executed Pandas result is: {str(exec_result)}.

    Provide a clear, concise explanation in **3–5 points**. Each point should:
    - Summarize a key insight, trend, or pattern from the data
    - Be informative but brief
    - Highlight the relevance to agriculture or rainfall patterns

    Mention data sources:
    1. Crop data: Ministry of Agriculture & Farmers Welfare
    2. Rainfall data: India Meteorological Department (data.gov.in)
    """

    detailed_answer = ask_gemini(explanation_prompt)

    conversation_history.append({"role": "assistant", "content": detailed_answer})

    return {
        "query": user_query,
        "generated_code": code,
        "result_preview": str(exec_result),
        "answer": detailed_answer,
        "source": "data.gov.in"
    }