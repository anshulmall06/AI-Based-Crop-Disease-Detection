"use client";

import { useState } from "react";
import api from "../lib/api";
import AIAdvice from "../components/AIAdvice";
import Link from "next/link";

const API = "http://127.0.0.1:8000";

export default function Home() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handlePredict = async () => {
    if (!file) {
      setError("Please select an image.");
      return;
    }

    setError("");
    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await api.post("/predict", formData, {
  headers: {
    "Content-Type": "multipart/form-data",
  },
});

      setResult(res.data);
    } catch (err) {
      console.error(err);
      setError("Prediction failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">

      {/* Navbar */}
      <nav className="bg-green-700 text-white px-6 py-4 flex flex-col md:flex-row justify-between items-center">

        <h1 className="text-3xl font-bold">
          🌱 Crop Disease Detection
        </h1>

        <div className="flex gap-6 mt-4 md:mt-0">
          <Link href="/">Home</Link>
          <Link href="/history">History</Link>
          <Link href="/dashboard">Dashboard</Link>
          <Link href="/login">Login</Link>
        </div>

      </nav>

      {/* Upload Card */}
      <div className="max-w-4xl mx-auto mt-10 bg-white rounded-xl shadow-lg p-8">

        <h2 className="text-3xl font-bold mb-6">
          Upload Crop Leaf Image
        </h2>

        <input
          type="file"
          accept="image/*"
          className="w-full border rounded-lg p-3"
          onChange={(e) => setFile(e.target.files[0])}
        />

        {error && (
          <div className="bg-red-100 text-red-700 mt-4 p-3 rounded-lg">
            {error}
          </div>
        )}

        <button
          onClick={handlePredict}
          disabled={loading}
          className="mt-6 bg-green-700 hover:bg-green-800 text-white px-6 py-3 rounded-lg"
        >
          {loading ? "Predicting..." : "Predict Disease"}
        </button>

      </div>

      {/* Loading */}
      {loading && (
        <div className="max-w-4xl mx-auto mt-8 bg-yellow-100 rounded-xl p-6 shadow">

          <h2 className="text-2xl font-bold">
            Analysing Image...
          </h2>

          <p className="mt-2">
            Please wait while the AI analyses your crop leaf.
          </p>

        </div>
      )}

      {/* Prediction Result */}
      {!loading && result && (

        <div className="max-w-4xl mx-auto mt-8 bg-white rounded-xl shadow-lg p-8">

          <h2 className="text-3xl font-bold mb-6">
            Prediction Result
          </h2>

          <div className="space-y-4">

            <p>
              <strong>Disease:</strong> {result.disease}
            </p>

            <p>
              <strong>Confidence:</strong> {result.confidence}%
            </p>

            <p>
              <strong>Description:</strong>
              {" "}
              Detected disease in uploaded crop leaf.
            </p>

            <p>
              <strong>Treatment:</strong>
              {" "}
              Apply recommended fungicide and remove infected leaves.
            </p>

            <p>
              <strong>Prevention:</strong>
              {" "}
              Maintain field hygiene and inspect crops regularly.
            </p>

          </div>

          <div className="mt-8">

            <AIAdvice
              disease={result.disease}
              confidence={result.confidence}
            />

          </div>

        </div>

      )}

      {/* Empty State */}
      {!loading && !result && (

        <div className="max-w-4xl mx-auto mt-8 bg-white rounded-xl shadow-lg p-8 text-center">

          <h2 className="text-2xl font-bold">
            No Prediction Yet
          </h2>

          <p className="text-gray-500 mt-2">
            Upload a crop image and click Predict Disease.
          </p>

        </div>

      )}

      {/* Footer */}
      <footer className="bg-green-700 text-white text-center py-5 mt-12">

        © 2026 AI Crop Disease Detection

      </footer>

    </div>
  );
}