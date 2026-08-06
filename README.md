# 🌱 AI Based Crop Disease Detection System

An AI-powered full-stack web application that helps farmers identify crop diseases by uploading plant leaf images.

The system uses a **Deep Learning image classification model with ONNX Runtime** for disease prediction, provides confidence scores, stores prediction history, and uses **Google Gemini AI** to generate disease explanations, treatment recommendations, and prevention methods.

This project combines **Artificial Intelligence, Machine Learning, Full Stack Development, and Cloud Deployment** to provide a smart farming assistance solution.

---

# 🚀 Live Demo

## 🌐 Frontend Application (Vercel)

https://ai-based-crop-disease-detection-drab.vercel.app/


## ⚙️ Backend API (Render)

https://ai-based-crop-disease-detection-3.onrender.com/


## 📖 API Documentation (Swagger)

https://ai-based-crop-disease-detection-3.onrender.com/docs

---

# 📸 Application Screenshots


## 🔐 Login Page

![Login](screenshots/login.png)


## 🌿 Disease Prediction

![Prediction](screenshots/prediction.png)


## 📊 Dashboard

![Dashboard](screenshots/dashboard.png)


---

# ✨ Key Features


## 🌿 AI Crop Disease Detection

- Upload plant leaf images
- Detect crop diseases using Deep Learning
- ONNX Runtime based model inference
- Display predicted disease name
- Display prediction confidence percentage


---

## 🤖 AI Crop Advisor

Integrated with Google Gemini AI to provide:

- Disease explanation
- Possible causes
- Treatment recommendations
- Prevention methods
- Farmer-friendly guidance


---

## 🔐 Secure Authentication

- User registration
- User login
- JWT based authentication
- Protected API routes
- Secure token authorization


---

## 📊 User Dashboard

Dashboard provides:

- Total prediction count
- Average confidence score
- Recent predictions
- Prediction management


---

## 📜 Prediction History Management

Users can:

- View previous predictions
- View prediction details
- Update records
- Delete prediction history


---

## 🌍 Multi Language Support

- English language support
- Hindi language support
- Responsive user interface
- Mobile-friendly design


---

# 🛠 Technology Stack


## Frontend

- Next.js
- React.js
- JavaScript
- HTML5
- CSS3
- Tailwind CSS
- Axios


## Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- JWT Authentication


## Machine Learning / AI

- Deep Learning Image Classification
- ONNX Runtime
- OpenCV
- NumPy
- Google Gemini AI


## Database

- MongoDB Atlas


## Deployment

- Vercel (Frontend)
- Render (Backend)
- MongoDB Atlas (Database)

---

# 🏗 System Architecture


```
                 User
                  |
                  |
                  V

          Next.js Frontend
              (Vercel)

                  |
                  |
             Axios API

                  |
                  |

          FastAPI Backend
              (Render)

          /             \

         /               \

 ONNX Deep Learning     MongoDB Atlas
     Model              Database

         |
         |

   Google Gemini AI

         |
         |

 Disease Explanation
 Treatment & Prevention
 Recommendations

```

---

# 📁 Project Structure


```
AI-Based-Crop-Disease-Detection

│
├── backend
│
│   ├── database
│   ├── middleware
│   ├── models
│   ├── routes
│   ├── schemas
│   ├── services
│   │
│   ├── ml
│   │   ├── model.onnx
│   │   ├── model.onnx.data
│   │   ├── classes.json
│   │   └── predictor.py
│   │
│   ├── app.py
│   └── requirements.txt
│
│
├── frontend
│
│   ├── app
│   ├── components
│   ├── lib
│   ├── public
│   ├── package.json
│   └── next.config.ts
│
│
├── screenshots
│
│   ├── login.png
│   ├── prediction.png
│   └── dashboard.png
│
│
├── README.md
└── .gitignore

```

---

# ⚙️ Installation & Setup


## Clone Repository


```bash
git clone https://github.com/anshulmall06/AI-Based-Crop-Disease-Detection.git
```


Navigate into project:


```bash
cd AI-Based-Crop-Disease-Detection
```


---

# Backend Setup


Go to backend folder:


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


Backend will run on:


```
http://127.0.0.1:8000
```


---

# Frontend Setup


Open another terminal:


```bash
cd frontend
```


Install dependencies:


```bash
npm install
```


Start application:


```bash
npm run dev
```


Frontend will run on:


```
http://localhost:3000
```

---

# 🔑 Environment Variables


Create `.env` file inside backend folder:


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
| POST | `/auth/register` | Create new user |
| POST | `/auth/login` | User login |


---

## Disease Prediction


| Method | Endpoint | Description |
|---|---|---|
| POST | `/predict` | Predict crop disease |


---

## AI Advisor


| Method | Endpoint | Description |
|---|---|---|
| POST | `/ai/explain` | Generate AI recommendations |


---

## Prediction History


| Method | Endpoint | Description |
|---|---|---|
| GET | `/predictions` | Get all predictions |
| GET | `/predictions/{id}` | Get prediction details |
| PUT | `/predictions/{id}` | Update prediction |
| DELETE | `/predictions/{id}` | Delete prediction |


---

# 🔐 Authentication Flow


1. User registers an account
2. User logs in
3. Backend generates JWT token
4. Token is stored on client side
5. Protected APIs require:

```
Authorization: Bearer <JWT_TOKEN>
```

---

# 🌐 Deployment


## Frontend

Platform:

```
Vercel
```

Framework:

```
Next.js + React
```


URL:

```
https://ai-based-crop-disease-detection-drab.vercel.app/
```


---

## Backend


Platform:

```
Render
```


Framework:

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

# ⚠️ Limitations


- Prediction accuracy depends on image quality
- Render free tier may cause initial loading delay
- Gemini AI requires internet connectivity
- Currently supports limited crop disease categories


---

# 🚀 Future Enhancements


- Mobile application
- Real-time camera disease detection
- More crop categories
- Cloud image storage
- Weather-based disease prediction
- Smart farming analytics
- Disease alert notification system


---

# 👨‍💻 Developer


**Anshul**

MCA Student  
Graphic Era University


GitHub:

https://github.com/anshulmall06


---

# 📄 License


This project is developed for educational and internship purposes.

---

# 🙏 Acknowledgements


- FastAPI
- Next.js
- MongoDB Atlas
- Google Gemini AI
- ONNX Runtime
- OpenCV
- Vercel
- Render
- Axios
