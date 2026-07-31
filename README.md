# 🌱 AI Based Crop Disease Detection System

An AI-powered web application that helps farmers identify crop diseases by uploading images of plant leaves. The system predicts crop diseases, displays confidence scores, stores prediction history, and generates treatment and prevention recommendations using **Google Gemini AI**.

---

# 🚀 Live Demo

## 🌐 Frontend (Vercel)

https://ai-based-crop-disease-detection-drab.vercel.app/

## ⚙️ Backend API (Render)

https://ai-based-crop-disease-detection-3.onrender.com

## 📖 API Documentation (Swagger)

https://ai-based-crop-disease-detection-3.onrender.com/docs

---

# 📸 Features

- 🌿 Upload crop leaf images
- 🤖 AI-powered crop disease prediction
- 📊 Confidence score display
- 🧠 Google Gemini AI crop advisor
- 💊 Disease description
- 🌱 Treatment recommendations
- 🛡 Prevention methods
- 👨‍🌾 Farmer tips
- 🔐 JWT Authentication
- 👤 User Registration & Login
- 📜 Prediction History (CRUD)
- 📈 Dashboard
- 💾 MongoDB Atlas integration
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
- Uvicorn
- JWT Authentication
- Pydantic

## Database

- MongoDB Atlas

## Artificial Intelligence

- Google Gemini AI
- Machine Learning Disease Prediction

---

# 📁 Project Structure

```text
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

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn app:app --reload
```

Backend runs at:

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

Frontend runs at:

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
|---------|----------|-------------|
| POST | `/auth/register` | Register User |
| POST | `/auth/login` | Login User |

---

## Disease Prediction

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/predict` | Predict Crop Disease |

---

## AI Crop Advisor

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/ai/explain` | Generate AI Advice using Gemini |

---

## Prediction History

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/predictions` | Get All Predictions |
| GET | `/predictions/{id}` | Get Prediction by ID |
| PUT | `/predictions/{id}` | Update Prediction |
| DELETE | `/predictions/{id}` | Delete Prediction |

---

# Application Workflow

1. Register a new account.
2. Login securely using JWT Authentication.
3. Upload a crop leaf image.
4. AI predicts the crop disease.
5. Confidence score is displayed.
6. Click **Get AI Advice**.
7. Google Gemini AI generates:
   - Disease Description
   - Causes
   - Treatment
   - Prevention
   - Farmer Tips
8. Prediction is saved to MongoDB.
9. View previous predictions in History and Dashboard.

---

# 🌐 Deployment

## Live Frontend

**Platform:** Vercel

https://ai-based-crop-disease-detection-drab.vercel.app/

---

## Live Backend

**Platform:** Render

https://ai-based-crop-disease-detection-3.onrender.com

---

## API Documentation

https://ai-based-crop-disease-detection-3.onrender.com/docs

---

# 📋 Deployment Summary

## Frontend

- Vercel
- Next.js
- React
- JavaScript

## Backend

- Render
- FastAPI
- Python

## Database

- MongoDB Atlas

## AI Service

- Google Gemini AI

---

# ⚠️ Known Limitations (Free Tier)

- The backend is deployed on the **Render Free Tier**.
- After approximately **15 minutes of inactivity**, Render may automatically put the backend service to sleep.
- The **first request after inactivity** may take **30–60 seconds** while the server wakes up.
- Once the backend is active, all application features work normally.
- AI advice requires an active internet connection to communicate with Google Gemini AI.

---

# 🚀 Future Enhancements

- 📱 Mobile Application
- 🌍 Multi-language Support
- 📷 Live Camera Disease Detection
- 📈 Analytics Dashboard
- 🌾 Support for More Crop Species
- ☁ Cloud Storage Integration
- 🔔 Disease Alert Notifications

---

# 📷 Screenshots

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

# 👨‍💻 Author

**Anshul**

MCA Student

Graphic Era University

GitHub:

https://github.com/anshulmall06

---

# 📄 License

This project was developed for educational and internship purposes.

---

# 🙏 Acknowledgements

- FastAPI
- Next.js
- MongoDB Atlas
- Google Gemini AI
- Render
- Vercel
- Axios
