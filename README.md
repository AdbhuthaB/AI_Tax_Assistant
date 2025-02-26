# AI_Tax_Assistant


## Overview
An AI-powered tax assistant that automates tax filing using OCR, NLP, and machine learning.

## Technologies Used
- **Backend:** FastAPI (Python)
- **Frontend:** React (JavaScript)
- **AI & ML:** OpenAI API, Tesseract OCR
- **Database:** PostgreSQL
- **Authentication & Security:** OAuth 2.0, AES encryption
- **Containerization:** Docker & Docker Compose

---

## Setup Instructions

### Running with Docker (Recommended)
1. **Ensure Docker is installed** on your machine.
2. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd tax-assistant
   ```
3. **Create a `.env` file** and add your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your_api_key" > .env
   ```
4. **Start the services**:
   ```bash
   docker-compose up --build
   ```
5. **Access the application**:
   - **Frontend:** `http://localhost:3000`
   - **Backend API Docs:** `http://localhost:8000/docs`

### Running Without Docker
1. **Backend Setup**:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
2. **Database Setup (PostgreSQL)**:
   ```sql
   CREATE DATABASE tax_db;
   ```
3. **Frontend Setup**:
   ```bash
   cd frontend
   npm install
   npm start
   ```

---

## API Endpoints
- `POST /extract-text/` → Extracts text from uploaded tax documents.
- `POST /predict-deductions/` → Predicts possible tax deductions.

---

## Deployment
- **Production Deployment:** Use cloud platforms like AWS/GCP with Docker containers.
- **Security:** Store API keys securely using environment variables.

---

## Troubleshooting
- **Docker issues?** Restart Docker and run `docker-compose up --build`.
- **WSL errors (Windows)?** Ensure WSL2 is set up correctly (`wsl --set-default-version 2`).
- **Database connection issues?** Ensure PostgreSQL is running and accessible.

---

This project simplifies tax filing, ensuring accuracy and maximizing deductions using AI. 🚀
