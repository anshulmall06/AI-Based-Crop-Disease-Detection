"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import api from "../../lib/api";

export default function Login() {
  const router = useRouter();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const login = async () => {
    if (!email || !password) {
      setError("Please enter email and password.");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const res = await api.post("/auth/login", {
        email,
        password,
      });

      localStorage.setItem(
        "token",
        res.data.access_token
      );

      alert("Login Successful");

      router.push("/dashboard");
    } catch (err) {
      console.error(err);

      setError(
        err?.response?.data?.detail ||
          "Invalid email or password."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-green-200 to-green-500 flex items-center justify-center p-6">

      <div className="bg-white w-full max-w-md rounded-xl shadow-xl p-8">

        <h1 className="text-4xl font-bold text-center text-green-700">

          Login

        </h1>

        <p className="text-center text-gray-500 mt-2">

          Sign in to your Crop Disease Detection account

        </p>

        {error && (

          <div className="bg-red-100 text-red-700 mt-6 p-3 rounded-lg">

            {error}

          </div>

        )}

        <div className="mt-6">

          <label className="block font-semibold mb-2">

            Email

          </label>

          <input
            type="email"
            placeholder="Enter email"
            value={email}
            onChange={(e) =>
              setEmail(e.target.value)
            }
            className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-green-600"
          />

        </div>

        <div className="mt-5">

          <label className="block font-semibold mb-2">

            Password

          </label>

          <input
            type="password"
            placeholder="Enter password"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
            className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-green-600"
          />

        </div>

        <button
          onClick={login}
          disabled={loading}
          className="w-full mt-8 bg-green-700 hover:bg-green-800 text-white py-3 rounded-lg font-semibold transition"
        >
          {loading ? "Logging in..." : "Login"}
        </button>

        <button
          onClick={() => router.push("/register")}
          className="w-full mt-4 border border-green-700 text-green-700 py-3 rounded-lg hover:bg-green-50"
        >
          Create New Account
        </button>

      </div>

    </div>
  );
}