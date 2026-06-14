# OCR API with FastAPI

## Overview

This project is an OCR (Optical Character Recognition) API built using FastAPI. It allows users to upload images, extract text using Tesseract OCR, and store OCR results in a SQLite database.

## Features

* Upload image files through REST API
* Extract text using Tesseract OCR
* Image preprocessing using OpenCV
* Store OCR results in SQLite
* Retrieve OCR history
* FastAPI Swagger documentation
* Docker support

## Tech Stack

* Python
* FastAPI
* OpenCV
* Tesseract OCR
* SQLite
* SQLAlchemy
* Uvicorn

## Project Structure

```text
ocr-project/
│
├── app/
│   ├── main.py
│   ├── ocr.py
│   ├── database.py
│   └── models.py
│
├── uploads/
├── requirements.txt
├── Dockerfile
└── .gitignore
```

## API Endpoints

### Upload Image
<img width="890" height="436" alt="image" src="https://github.com/user-attachments/assets/e08229aa-6a74-4f3c-927b-7ac52d0749cd" />


```http
POST /upload
```

Uploads an image and extracts text.

### OCR History

```http
GET /history
```

Returns all OCR records stored in the database.

## Installation

```bash
git clone <repository-url>
cd ocr-project

python -m venv venv
source venv/Scripts/activate

pip install -r requirements.txt
```

## Run Application

```bash
uvicorn app.main:app --reload
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Note

Install Tesseract OCR separately and update the Tesseract executable path in `ocr.py` according to your operating system.
