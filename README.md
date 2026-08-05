# 🌱 AI Based Crop Disease Detection System

An AI-powered full-stack web application that helps farmers identify crop diseases by uploading plant leaf images.

The system uses a **Deep Learning image classification model with ONNX Runtime** to detect crop diseases, provides confidence scores, stores prediction history, and generates disease explanation, treatment recommendations, and prevention methods using **Google Gemini AI**.

---

# 🚀 Live Demo

## 🌐 Frontend (Vercel)

https://ai-based-crop-disease-detection-1okxdgbje-tbi4.vercel.app/

## ⚙️ Backend API (Render)

https://ai-based-crop-disease-detection-3.onrender.com/

## 📖 Swagger API Documentation

https://ai-based-crop-disease-detection-3.onrender.com/docs

---

# 📸 Application Screenshots


## 🔐 Login Page

![Login Screenshot](screenshots/login.png)


## 🌿 Disease Prediction

![Prediction Screenshot](screenshots/prediction.png)


## 📊 Dashboard

![Dashboard Screenshot](screenshots/dashboard.png)


---

# ✨ Features

## 🌿 AI Crop Disease Detection

- Upload crop leaf images
- Detect plant diseases using Deep Learning
- ONNX Runtime based inference
- Display predicted disease name
- Display confidence percentage


---

## 🤖 AI Crop Advisor

Integrated with Google Gemini AI:

- Disease explanation
- Disease causes
- Treatment recommendations
- Prevention methods
- Farmer guidance


---

## 🔐 Authentication System

- User registration
- Secure login
- JWT authentication
- Protected API routes
- Token-based authorization


---

## 📊 Dashboard

- Total prediction count
- Average confidence score
- Latest prediction
- Prediction management


---

## 📜 Prediction History

Users can:

- View previous predictions
- Update prediction records
- Delete prediction records


---

## 💾 Database Integration

Using MongoDB Atlas:

- User information storage
- Prediction history storage
- Cloud database integration


---

## 🌍 User Experience

- Responsive UI
- English/Hindi language support
- Modern dashboard interface
- Mobile-friendly design


---

# 🛠 Tech Stack


## Frontend

- Next.js
- React.js
- JavaScript
- HTML5
- CSS3
- Tailwind CSS
- Axios


## Backend

- FastAPI
- Python
- Uvicorn
- Pydantic
- JWT Authentication


## Machine Learning / AI

- ONNX Runtime
- Deep Learning Image Classification Model
- OpenCV
- NumPy
- Google Gemini AI


## Database

- MongoDB Atlas


## Deployment

- Frontend: Vercel
- Backend: Render
- Database: MongoDB Atlas


---

# 📁 Project Structure

```text
AI-Based-Crop-Disease-Detection/

│
├── backend/
│
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
│   ├── login.png
│   ├── prediction.png
│   └── dashboard.png
│
├── README.md
└── .gitignore
```

---

# ⚙️ Installation Guide


## Clone Repository

```bash
git clone https://github.com/anshulmall06/AI-Based-Crop-Disease-Detection.git
```

```bash
cd AI-Based-Crop-Disease-Detection
```

---

# Backend Setup

Navigate to backend:

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


Backend runs:

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


Start frontend:

```bash
npm run dev
```


Frontend runs:

```
http://localhost:3000
```

---

# 🔑 Environment Variables


Create `.env` inside backend folder.


```env
MONGO_URI=your_mongodb_connection_string

JWT_SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_google_gemini_api_key
```

---

# 🔌 API Endpoints


## Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register user |
| POST | `/auth/login` | Login user |


---

## Disease Prediction

| Method | Endpoint | Description |
|---|---|---|
| POST | `/predict` | Upload image and predict disease |


---

## AI Advisor

| Method | Endpoint | Description |
|---|---|---|
| POST | `/ai/explain` | Generate AI disease advice |


---

## Prediction History

| Method | Endpoint | Description |
|---|---|---|
| GET | `/predictions` | Get predictions |
| GET | `/predictions/{id}` | Get prediction details |
| PUT | `/predictions/{id}` | Update prediction |
| DELETE | `/predictions/{id}` | Delete prediction |

---

# 🔐 JWT Protected Routes


Protected APIs:

```
POST /predict

GET /predictions

PUT /predictions/{id}

DELETE /predictions/{id}
```


Authorization Header:

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
Next.js Frontend
(Vercel)
 |
 |
Axios REST API
 |
 |
V
FastAPI Backend
(Render)
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

# 🌐 Deployment Details


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


Backend supports:


Local Development:

```
http://localhost:3000
```


Vercel Deployment:

```
https://*.vercel.app
```


---

# ⚠️ Known Limitations


- Backend is deployed on Render Free Tier.
- Server may sleep after inactivity.
- First request after sleep may take extra time.
- Gemini AI requires internet connection.
- Prediction accuracy depends on uploaded image quality.


---

# 🚀 Future Enhancements


- Mobile application
- Live camera disease detection
- More crop categories
- Cloud image storage
- Disease alert notifications
- Advanced analytics dashboard
- Smart farming recommendations


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
- ONNX Runtime
- OpenCV
- Render
- Vercel
- Axios
