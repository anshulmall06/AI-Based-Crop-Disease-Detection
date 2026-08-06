"use client";

import { useState } from "react";
import api from "../lib/api";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import AIAdvice from "../components/AIAdvice";

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
      <Navbar />

      {/* Hero Section */}
      <Hero />

      {/* Upload Card */}
      <div
        id="upload-section"
        className="max-w-5xl mx-auto -mt-16 relative z-20 bg-white rounded-2xl shadow-2xl p-8"
      >
        <h2 className="text-3xl font-bold mb-6 text-center text-green-700">
          🌿 Upload Crop Leaf Image
        </h2>

        <input
          type="file"
          accept="image/*"
          className="w-full border-2 border-dashed border-green-300 rounded-xl p-4 cursor-pointer hover:border-green-600 transition"
          onChange={(e) => setFile(e.target.files[0])}
        />

        {file && (
          <p className="mt-3 text-green-700 font-medium">
            📄 Selected File: {file.name}
          </p>
        )}

        {error && (
          <div className="bg-red-100 text-red-700 mt-4 p-3 rounded-lg">
            {error}
          </div>
        )}

        <button
          onClick={handlePredict}
          disabled={loading}
          className="mt-6 w-full bg-green-700 hover:bg-green-800 disabled:bg-gray-500 text-white px-6 py-4 rounded-xl text-lg font-semibold transition"
        >
          {loading ? "🔄 Predicting..." : "🌱 Predict Disease"}
        </button>
      </div>

      {/* Loading */}
      {loading && (
        <div className="max-w-5xl mx-auto mt-8 bg-yellow-50 border border-yellow-300 rounded-2xl p-6 shadow-lg">
          <div className="flex items-center gap-4">
            <div className="animate-spin rounded-full h-10 w-10 border-4 border-green-200 border-t-green-700"></div>

            <div>
              <h2 className="text-2xl font-bold text-green-700">
                🤖 AI is Analysing Your Crop...
              </h2>

              <p className="mt-2 text-gray-600">
                Please wait while the AI identifies the disease and prepares recommendations.
              </p>
            </div>
          </div>
        </div>
      )}

      {/* Prediction Result */}
      {!loading && result && (
        <div className="max-w-5xl mx-auto mt-8 bg-white rounded-2xl shadow-2xl p-8">
          <h2 className="text-3xl font-bold mb-8 text-green-700">
            🌾 Prediction Result
          </h2>

          <div className="grid md:grid-cols-2 gap-6">

            <div className="bg-green-50 rounded-xl p-5 shadow">
              <h3 className="font-bold text-green-700 mb-2">🌿 Disease</h3>
              <p>{result.disease}</p>
            </div>

            <div className="bg-green-50 rounded-xl p-5 shadow">
              <h3 className="font-bold text-green-700 mb-2">📈 Confidence</h3>
              <p>{result.confidence}%</p>
            </div>

            <div className="bg-green-50 rounded-xl p-5 shadow">
              <h3 className="font-bold text-green-700 mb-2">📝 Description</h3>
              <p>Detected disease in uploaded crop leaf.</p>
            </div>

            <div className="bg-green-50 rounded-xl p-5 shadow">
              <h3 className="font-bold text-green-700 mb-2">💊 Treatment</h3>
              <p>Apply recommended fungicide and remove infected leaves.</p>
            </div>

            <div className="bg-green-50 rounded-xl p-5 shadow md:col-span-2">
              <h3 className="font-bold text-green-700 mb-2">🛡 Prevention</h3>
              <p>
                Maintain field hygiene, inspect crops regularly, and follow proper crop management practices.
              </p>
            </div>

          </div>

          <div className="mt-10">
            <AIAdvice
              disease={result.disease}
              confidence={result.confidence}
            />
          </div>
        </div>
      )}

      {/* Empty State */}
      {!loading && !result && (
        <div className="max-w-5xl mx-auto mt-8 bg-white rounded-2xl shadow-xl p-10 text-center">
          <div className="text-6xl mb-4">🌱</div>

          <h2 className="text-3xl font-bold text-green-700">
            No Prediction Yet
          </h2>

          <p className="text-gray-500 mt-3">
            Upload a crop leaf image and click
            <strong> Predict Disease </strong>
            to begin AI analysis.
          </p>
        </div>
      )}

      {/* Footer */}
      <footer className="bg-green-700 text-white text-center py-6 mt-12">
        <h2 className="text-xl font-semibold">
          🌾 AI Crop Disease Detection
        </h2>

        <p className="mt-2">
          Powered by Next.js • FastAPI • MongoDB • ONNX Runtime • Google Gemini
        </p>

        <p className="mt-3 text-sm">
          © 2026 AI Crop Disease Detection. All Rights Reserved.
        </p>
      </footer>

    </div>
  );
}