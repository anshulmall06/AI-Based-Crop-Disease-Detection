# 🌱 AI Based Crop Disease Detection System

An AI-powered web application that helps farmers identify crop diseases by uploading images of plant leaves. The system predicts the disease using AI, provides confidence scores, stores prediction history, and generates treatment and prevention recommendations using Google's Gemini AI.

---

# 🚀 Live Demo

### 🌐 Frontend (Vercel)
https://ai-based-crop-disease-detection-drab.vercel.app/

### ⚙️ Backend API (Render)
https://ai-based-crop-disease-detection-3.onrender.com

### 📖 API Documentation
https://ai-based-crop-disease-detection-3.onrender.com/docs

---

# 📸 Features

- 🌿 Upload crop leaf images
- 🤖 AI-powered crop disease prediction
- 📊 Confidence score display
- 🧠 Gemini AI crop advisor
- 💊 Disease description
- 🌱 Treatment recommendations
- 🛡 Prevention methods
- 👨‍🌾 Farmer tips
- 🔐 JWT Authentication
- 👤 User Registration & Login
- 📜 Prediction history
- 📈 Dashboard
- 💾 MongoDB database integration
- 🌍 Responsive UI
- ⚡ FastAPI REST APIs

---

# 🛠 Tech Stack

## Frontend

- Next.js
- React
- JavaScript
- HTML5
- CSS3
- Axios

## Backend

- FastAPI
- Python
- JWT Authentication
- Pydantic
- Uvicorn

## Database

- MongoDB Atlas

## Artificial Intelligence

- Google Gemini AI
- Machine Learning Disease Prediction

---

# 📁 Project Structure

```
AI-Based-Crop-Disease-Detection/
│
├── backend/
│   ├── controllers/
│   ├── database/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── package.json
│   └── next.config.ts
│
├── dataset/
├── notebooks/
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/anshulmall06/AI-Based-Crop-Disease-Detection.git

cd AI-Based-Crop-Disease-Detection
```

---

# Backend Setup

```bash
cd backend

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start Backend

```bash
uvicorn app:app --reload
```

Backend will run at

```
http://127.0.0.1:8000
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend will run at

```
http://localhost:3000
```

---

# Environment Variables

Create a `.env` file inside the **backend** folder.

```env
MONGO_URI=your_mongodb_connection_string

JWT_SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_google_gemini_api_key
```

---

# API Endpoints

## Authentication

| Method | Endpoint | Description |
|----------|----------------|----------------|
| POST | `/auth/register` | Register User |
| POST | `/auth/login` | Login User |

---

## Disease Prediction

| Method | Endpoint | Description |
|----------|----------------|----------------|
| POST | `/predict` | Predict Disease |

---

## AI Crop Advisor

| Method | Endpoint | Description |
|----------|----------------|----------------|
| POST | `/ai/explain` | Generate AI Advice |

---

## Prediction History

| Method | Endpoint | Description |
|----------|----------------|----------------|
| GET | `/predictions` | Get Prediction History |
| GET | `/predictions/{id}` | Get Prediction |
| PUT | `/predictions/{id}` | Update Prediction |
| DELETE | `/predictions/{id}` | Delete Prediction |

---

# Application Workflow

1. User registers an account.
2. User logs into the application.
3. User uploads a crop leaf image.
4. Backend predicts the disease.
5. Disease name and confidence score are displayed.
6. User clicks **Get AI Advice**.
7. Gemini AI generates:
   - Disease Description
   - Causes
   - Treatment
   - Prevention
   - Farmer Tips
8. Prediction is saved to MongoDB.
9. User can view prediction history and dashboard.

---

# Deployment

## Frontend

- Vercel

## Backend

- Render

## Database

- MongoDB Atlas

---

# Future Enhancements

- 📱 Mobile Application
- 🌍 Multi-language Support
- 📷 Live Camera Detection
- 📈 Analytics Dashboard
- 🌾 Support for More Crop Types
- ☁ Cloud Storage Integration
- 🔔 Disease Alert Notifications

---

# Screenshots

## Home Page

- Upload Crop Leaf Image
- Disease Prediction

## AI Crop Advisor

- Disease Description
- Treatment
- Prevention
- Farmer Tips

## Dashboard

- Prediction Statistics

## History

- Previous Predictions

---

# Author

**Anshul**

MCA Student

Graphic Era University

GitHub

https://github.com/anshulmall06

---

# License

This project was developed for educational and internship purposes.

---

# Acknowledgements

- FastAPI
- Next.js
- MongoDB Atlas
- Google Gemini AI
- Render
- Vercel
