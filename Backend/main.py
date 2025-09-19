from fastapi import FastAPI
import requests
import os

app = FastAPI()

# Environment variables (set these after signup)
CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

@app.get("/ping")
def ping():
    return {"message": "AI DevOps Assistant is running"}

@app.post("/analyze-log/")
def analyze_log(log: dict):
    """
    log: {"content": "Error: connection refused at port 5432"}
    """

    # Step 1: Summarize log with LLaMA
    llama_summary = f"LLaMA would summarize this log: {log['content']}"

    # Step 2: Troubleshoot with Cerebras
    cerebras_fix = f"Cerebras suggests steps to fix: check DB, network, and retries"

    return {
        "summary": llama_summary,
        "resolution": cerebras_fix
    }
