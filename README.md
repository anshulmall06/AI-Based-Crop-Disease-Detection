# 🌱 AI Based Crop Disease Detection System

An AI-powered full-stack web application that helps farmers identify crop diseases by uploading images of plant leaves.

The system uses a Deep Learning image classification model with **ONNX Runtime** to predict crop diseases, provides confidence scores, stores prediction history, and generates disease explanation and treatment recommendations using **Google Gemini AI**.

---

# 🚀 Live Demo

## 🌐 Frontend (Vercel)

https://ai-based-crop-disease-detection-1okxdgbje-tbi4.vercel.app/

## ⚙️ Backend API (Render)

https://ai-based-crop-disease-detection-3.onrender.com/

## 📖 API Documentation (Swagger)

https://ai-based-crop-disease-detection-3.onrender.com/docs

---

# 📸 Features

## 🌿 Crop Disease Detection

* Upload crop leaf images
* AI-based disease prediction
* Confidence score calculation
* Plant disease classification using Deep Learning model

## 🤖 AI Crop Advisor

* Disease explanation
* Causes of disease
* Treatment recommendations
* Prevention methods
* Farmer tips using Google Gemini AI

## 🔐 Authentication System

* User registration
* Secure login
* JWT authentication
* Protected API routes

## 📊 Dashboard

* Total predictions count
* Average confidence score
* Latest prediction
* Prediction history management

## 📜 Prediction History

* View previous predictions
* Update prediction records
* Delete prediction records

## 💾 Database

* MongoDB Atlas integration
* User data storage
* Prediction history storage

## 🌍 User Experience

* Responsive UI
* English/Hindi language support
* Modern dashboard interface

---

# 🛠 Tech Stack

## Frontend

* Next.js
* React.js
* JavaScript
* HTML5
* CSS3
* Tailwind CSS
* Axios

## Backend

* FastAPI
* Python
* Uvicorn
* Pydantic
* JWT Authentication

## Database

* MongoDB Atlas

## Artificial Intelligence

* ONNX Runtime
* Deep Learning Image Classification Model
* OpenCV
* NumPy
* Google Gemini AI

## Deployment

* Frontend: Vercel
* Backend: Render
* Database: MongoDB Atlas

---

# 📁 Project Structure

```
AI-Based-Crop-Disease-Detection/

│
├── backend/
│
│   ├── controllers/
│   ├── database/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   │
│   ├── ml/
│   │   ├── model.onnx
│   │   ├── model.onnx.data
│   │   ├── classes.json
│   │   └── predictor.py
│   │
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
│
├── frontend/
│
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── package.json
│   └── next.config.ts
│
│
├── screenshots/
│
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/anshulmall06/AI-Based-Crop-Disease-Detection.git
```

```bash
cd AI-Based-Crop-Disease-Detection
```

---

# Backend Setup

Move into backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

# Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend runs on:

```
http://localhost:3000
```

---

# 🔑 Environment Variables

Create `.env` file inside backend folder.

```env
MONGO_URI=your_mongodb_connection_string

JWT_SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_google_gemini_api_key
```

---

# 🔌 API Endpoints

## Authentication

| Method | Endpoint         | Description   |
| ------ | ---------------- | ------------- |
| POST   | `/auth/register` | Register user |
| POST   | `/auth/login`    | Login user    |

---

## Disease Prediction

| Method | Endpoint   | Description                      |
| ------ | ---------- | -------------------------------- |
| POST   | `/predict` | Upload image and predict disease |

---

## AI Advisor

| Method | Endpoint      | Description                |
| ------ | ------------- | -------------------------- |
| POST   | `/ai/explain` | Generate AI disease advice |

---

## Prediction History

| Method | Endpoint            | Description            |
| ------ | ------------------- | ---------------------- |
| GET    | `/predictions`      | Get all predictions    |
| GET    | `/predictions/{id}` | Get prediction details |
| PUT    | `/predictions/{id}` | Update prediction      |
| DELETE | `/predictions/{id}` | Delete prediction      |

---

# 🔐 Protected APIs

JWT authentication is required for:

```
POST /predict

GET /predictions

PUT /predictions/{id}

DELETE /predictions/{id}
```

Authorization header:

```
Authorization: Bearer <JWT_TOKEN>
```

---

# 🏗 Application Workflow

```
User
 |
 |
V
Next.js Frontend (Vercel)
 |
 |
Axios REST API
 |
 |
V
FastAPI Backend (Render)
 |
 |
 +----------------+
 |                |
 V                V
ONNX Model     MongoDB Atlas
Prediction     Database
 |
 |
V
Google Gemini AI
 |
 |
V
Treatment & Prevention Advice
```

---

# 🌐 Deployment

## Frontend

Platform:

```
Vercel
```

Technology:

```
Next.js + React
```

URL:

```
https://ai-based-crop-disease-detection-1okxdgbje-tbi4.vercel.app/
```

---

## Backend

Platform:

```
Render
```

Technology:

```
FastAPI + Python
```

URL:

```
https://ai-based-crop-disease-detection-3.onrender.com/
```

---

## Database

Platform:

```
MongoDB Atlas
```

---

# 🌍 CORS Configuration

The backend supports:

* Local development

```
http://localhost:3000
```

* Vercel deployments

```
https://*.vercel.app
```

---

# 📸 Screenshots

Add application screenshots here:

```
screenshots/

├── home.png
├── prediction.png
└── dashboard.png
```

---

# ⚠️ Known Limitations

* Backend uses Render Free Tier.
* Service may sleep after inactivity.
* First request after inactivity may take additional time.
* Gemini AI requires internet connectivity.
* Disease prediction accuracy depends on image quality.

---

# 🚀 Future Enhancements

* Mobile application
* Live camera disease detection
* More crop categories
* Cloud image storage
* Disease alert notifications
* Advanced analytics dashboard
* Farmer recommendation system

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

* FastAPI
* Next.js
* MongoDB Atlas
* Google Gemini AI
* ONNX Runtime
* OpenCV
* Render
* Vercel
* Axios
