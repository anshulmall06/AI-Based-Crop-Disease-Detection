# 🌱 AI Based Crop Disease Detection System

An AI-powered web application that helps farmers identify crop diseases by uploading images of plant leaves. The system predicts the disease, provides confidence scores, and provides AI-assisted treatment and prevention recommendations.

---

# 🌐 Live Deployment

### Frontend (Vercel)

**Live URL:**
https://ai-based-crop-disease-detection-drab.vercel.app/

### Backend (Render)

**Live API URL:**
https://ai-based-crop-disease-detection-3.onrender.com/

---

# 🚀 Features

* 🌿 Upload crop leaf images
* 🤖 AI-powered crop disease prediction
* 📊 Confidence score for predictions
* 💊 Disease description, treatment, and prevention recommendations
* 🧠 AI Crop Advisor powered by Google Gemini
* 🔐 User Authentication (JWT)
* 📜 Prediction history
* 📈 Dashboard with prediction records
* ⚡ FastAPI REST APIs
* 💾 MongoDB Atlas integration
* 📱 Responsive UI

---

# 🛠️ Tech Stack Summary

## Frontend

* Next.js
* React
* JavaScript
* HTML
* CSS
* Axios

## Backend

* FastAPI
* Python
* JWT Authentication
* Pydantic

## Database

* MongoDB Atlas

## AI / Machine Learning

* Google Gemini API
* OpenCV
* NumPy
* Scikit-learn

## Deployment

* Vercel (Frontend)
* Render (Backend)

---

# 📁 Project Structure

```text
AI-Based-Crop-Disease-Detection/
│
├── backend/
│   ├── auth/
│   ├── controllers/
│   ├── database/
│   ├── middleware/
│   ├── ml/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── static/
│   ├── uploads/
│   ├── utils/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── dataset/
├── notebooks/
└── README.md
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
python -m uvicorn app:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```text
http://localhost:3000
```

---

# Environment Variables

Create a `.env` file inside the **backend** directory.

Example:

```env
MONGO_URI=your_mongodb_connection_string

JWT_SECRET_KEY=your_secret_key

GOOGLE_API_KEY=your_google_api_key
```

---

# API Endpoints

## Authentication

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| POST   | `/auth/register` | Register a new user |
| POST   | `/auth/login`    | User login          |

## Prediction

| Method | Endpoint            | Description          |
| ------ | ------------------- | -------------------- |
| POST   | `/predict`          | Predict crop disease |
| GET    | `/predictions`      | Get all predictions  |
| GET    | `/predictions/{id}` | Get prediction by ID |
| PUT    | `/predictions/{id}` | Update prediction    |
| DELETE | `/predictions/{id}` | Delete prediction    |

---

# Application Workflow

1. User registers or logs into the system.
2. User uploads a crop leaf image.
3. The backend processes the image.
4. The AI model predicts the disease.
5. Confidence score is generated.
6. Disease information is displayed.
7. AI Crop Advisor provides treatment and prevention suggestions.
8. Prediction is stored in MongoDB.
9. Users can view prediction history and dashboard statistics.

---

# Deployment Summary

## Frontend

* Platform: Vercel
* Framework: Next.js
* Automatic deployment through GitHub

## Backend

* Platform: Render
* Framework: FastAPI
* MongoDB Atlas database
* Automatic deployment through GitHub

---

# Known Limitations (Free Tier)

* The backend is deployed on Render's free tier.
* Render may spin down the service after approximately 15 minutes of inactivity.
* The first request after inactivity can take around 30–60 seconds while the service wakes up.
* AI prediction speed depends on internet connectivity and server response time.

---

# Future Enhancements

* 📱 Android Application
* 🌐 Multi-language Support
* 📷 Real-time Camera Detection
* 📊 Advanced Analytics Dashboard
* 🌾 Support for More Crop Species
* 🔔 Disease Alert Notifications

---

# Contributors

**Anshul Mall**

GitHub: https://github.com/anshulmall06

---

# License

This project was developed for educational and internship purposes.
