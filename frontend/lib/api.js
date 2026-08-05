import axios from "axios";

const api = axios.create({
  baseURL: "https://ai-based-crop-disease-detection-3.onrender.com",
});


api.interceptors.request.use((config) => {

  if (typeof window !== "undefined") {

    const token = localStorage.getItem("token");

    console.log("TOKEN SENT:", token);

    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

  }

  return config;

});


export default api;