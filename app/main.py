from fastapi import FastAPI, UploadFile, File
from app.ocr import extract_text

from app.database import SessionLocal, engine
from app.models import OCRHistory
from app.database import Base

import os

app = FastAPI()

Base.metadata.create_all(bind=engine)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/history")
def get_history():

    db = SessionLocal()

    records = db.query(OCRHistory).all()

    db.close()

    return records
@app.get("/")
def home():
    return {
        "message": "OCR API is running"
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text(file_path)

    db = SessionLocal()

    record = OCRHistory(
        filename=file.filename,
        extracted_text=text
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    db.close()

    return {
        "filename": file.filename,
        "extracted_text": text
    }
