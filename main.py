# File: backend/main.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import uvicorn
import pytesseract
from PIL import Image
import openai
import psycopg2
import os

app = FastAPI()

# Database connection
conn = psycopg2.connect(
    dbname="tax_db", user="admin", password="password", host="db", port="5432"
)
cursor = conn.cursor()

# OpenAI API Key (ensure this is securely stored)
openai.api_key = os.getenv("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")

class TaxData(BaseModel):
    user_id: int
    income: float
    expenses: float

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file)
        text = pytesseract.image_to_string(image)
        return {"extracted_text": text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/predict-deductions/")
async def predict_deductions(data: TaxData):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Based on income {data.income} and expenses {data.expenses}, predict deductions:",
        max_tokens=100
    )
    return {"deductions": response.choices[0].text.strip()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
