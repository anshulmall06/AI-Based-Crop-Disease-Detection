"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import api from "../../lib/api";
import Link from "next/link";

const API = const API = process.env.NEXT_PUBLIC_API_URL;

export default function History() {

  const router = useRouter();

  const [predictions, setPredictions] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const [message, setMessage] = useState("");

  const [editingId, setEditingId] = useState(null);

  const [saving, setSaving] = useState(false);

  const [deletingId, setDeletingId] = useState(null);

  const [editForm, setEditForm] = useState({

    disease: "",

    confidence: "",

  });

  useEffect(() => {

    const token = localStorage.getItem("token");

    if (!token) {

      router.push("/login");

      return;

    }

    loadPredictions();

  }, []);

  const loadPredictions = async () => {

    try {

      setLoading(true);

      setError("");

      const token = localStorage.getItem("token");

      const res = await api.get(

        `${API}/predictions`,

        {

          headers: {

            Authorization: `Bearer ${token}`,

          },

        }

      );

      setPredictions(res.data);

    } catch (err) {

      console.log(err);

      setError("Unable to load prediction history.");

    } finally {

      setLoading(false);

    }

  };

  const startEdit = (item) => {

    setEditingId(item._id);

    setEditForm({

      disease: item.disease,

      confidence: item.confidence,

    });

  };

  const cancelEdit = () => {

    setEditingId(null);

    setEditForm({

      disease: "",

      confidence: "",

    });

  };

  const savePrediction = async (id) => {

    try {

      setSaving(true);

      const token = localStorage.getItem("token");

      await api.put(

        `${API}/predictions/${id}`,

        {

          disease: editForm.disease,

          confidence: Number(editForm.confidence),

        },

        {

          headers: {

            Authorization: `Bearer ${token}`,

          },

        }

      );

      setMessage("Prediction updated successfully.");

      setEditingId(null);

      loadPredictions();

    } catch (err) {

      console.log(err);

      setError("Update failed.");

    } finally {

      setSaving(false);

    }

  };

  const deletePrediction = async (id) => {

    if (!confirm("Delete this prediction?")) return;

    try {

      setDeletingId(id);

      const token = localStorage.getItem("token");

      await api.delete(

        `${API}/predictions/${id}`,

        {

          headers: {

            Authorization: `Bearer ${token}`,

          },

        }

      );

      setPredictions(

        predictions.filter(

          (item) => item._id !== id

        )

      );

      setMessage("Prediction deleted.");

    } catch (err) {

      console.log(err);

      setError("Delete failed.");

    } finally {

      setDeletingId(null);

    }

  };

  if (loading) {

    return (

      <div className="min-h-screen flex justify-center items-center text-2xl font-bold">

        Loading Prediction History...

      </div>

    );

  }

  return (

    <div className="min-h-screen bg-gray-100">

      {/* Navbar */}

      <nav className="bg-green-700 text-white px-6 py-4 flex flex-col md:flex-row justify-between items-center">

        <h1 className="text-3xl font-bold">

          🌱 Crop Disease Detection

        </h1>

        <div className="flex gap-6 mt-4 md:mt-0">

          <Link href="/">Home</Link>

          <Link href="/dashboard">

            Dashboard

          </Link>

          <Link href="/login">

            Login

          </Link>

        </div>

      </nav>

      <div className="max-w-6xl mx-auto p-8">

        <h1 className="text-4xl font-bold">

          Prediction History

        </h1>

        <p className="text-gray-600 mt-2">

          Manage your saved AI predictions.

        </p>

        {message && (

          <div className="bg-green-100 text-green-700 p-3 rounded-lg mt-6">

            {message}

          </div>

        )}

        {error && (

          <div className="bg-red-100 text-red-700 p-3 rounded-lg mt-6">

            {error}

          </div>

        )}

        <div className="bg-white rounded-xl shadow-lg mt-8 p-6">
          <h2 className="text-2xl font-bold mb-6">
            Saved Predictions
          </h2>

          {predictions.length === 0 ? (

            <div className="text-center py-12">

              <h3 className="text-2xl font-bold">
                No Prediction History
              </h3>

              <p className="text-gray-500 mt-2">
                Upload a crop image to create your first prediction.
              </p>

              <Link
                href="/"
                className="inline-block mt-6 bg-green-700 text-white px-6 py-3 rounded-lg hover:bg-green-800"
              >
                Predict Disease
              </Link>

            </div>

          ) : (

            <div className="overflow-x-auto">

              <table className="min-w-full border">

                <thead>

                  <tr className="bg-gray-200">

                    <th className="border p-3">
                      Disease
                    </th>

                    <th className="border p-3">
                      Confidence
                    </th>

                    <th className="border p-3">
                      File
                    </th>

                    <th className="border p-3">
                      Actions
                    </th>

                  </tr>

                </thead>

                <tbody>

                  {predictions.map((item) => (

                    <tr
                      key={item._id}
                      className="hover:bg-gray-50"
                    >

                      {editingId === item._id ? (

                        <>

                          <td className="border p-3">

                            <input
                              type="text"
                              value={editForm.disease}
                              onChange={(e) =>
                                setEditForm({
                                  ...editForm,
                                  disease: e.target.value,
                                })
                              }
                              className="border rounded-lg p-2 w-full"
                            />

                          </td>

                          <td className="border p-3">

                            <input
                              type="number"
                              value={editForm.confidence}
                              onChange={(e) =>
                                setEditForm({
                                  ...editForm,
                                  confidence: e.target.value,
                                })
                              }
                              className="border rounded-lg p-2 w-full"
                            />

                          </td>

                          <td className="border p-3">
                            {item.filename}
                          </td>

                          <td className="border p-3">

                            <div className="flex gap-2 flex-wrap">

                              <button
                                onClick={() =>
                                  savePrediction(item._id)
                                }
                                disabled={saving}
                                className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-lg"
                              >
                                {saving ? "Saving..." : "Save"}
                              </button>

                              <button
                                onClick={cancelEdit}
                                className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-lg"
                              >
                                Cancel
                              </button>

                            </div>

                          </td>

                        </>

                      ) : (

                        <>

                          <td className="border p-3">
                            {item.disease}
                          </td>

                          <td className="border p-3">
                            {item.confidence}%
                          </td>

                          <td className="border p-3">
                            {item.filename}
                          </td>

                          <td className="border p-3">

                            <div className="flex gap-2 flex-wrap">

                              <button
                                onClick={() =>
                                  startEdit(item)
                                }
                                className="bg-yellow-500 hover:bg-yellow-600 text-white px-4 py-2 rounded-lg"
                              >
                                Edit
                              </button>

                              <button
                                onClick={() =>
                                  deletePrediction(item._id)
                                }
                                disabled={
                                  deletingId === item._id
                                }
                                className="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-lg"
                              >
                                {deletingId === item._id
                                  ? "Deleting..."
                                  : "Delete"}
                              </button>

                            </div>

                          </td>

                        </>

                      )}

                    </tr>

                  ))}

                </tbody>

              </table>

            </div>

          )}
        </div>

      </div>

      {/* Footer */}

      <footer className="bg-green-700 text-white text-center py-4 mt-10">

        © 2026 AI Crop Disease Detection System

      </footer>

    </div>

  );

}