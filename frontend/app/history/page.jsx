"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import api from "../../lib/api";

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

      const res = await api.get("/predictions");

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

      await api.put(`/predictions/${id}`, {
        disease: editForm.disease,
        confidence: Number(editForm.confidence),
      });

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

      await api.delete(`/predictions/${id}`);

      setPredictions(
        predictions.filter((item) => item._id !== id)
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

      <nav className="bg-green-700 text-white px-6 py-4 flex justify-between items-center">

        <h1 className="text-3xl font-bold">
          🌱 Crop Disease Detection
        </h1>

        <div className="flex gap-6">
          <Link href="/">Home</Link>
          <Link href="/dashboard">Dashboard</Link>
          <Link href="/login">Login</Link>
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

          {predictions.length === 0 ? (

            <div className="text-center py-10">
              <h2 className="text-2xl font-bold">
                No Prediction History
              </h2>

              <p className="text-gray-500 mt-2">
                Upload a crop image to create your first prediction.
              </p>

              <Link
                href="/"
                className="inline-block mt-6 bg-green-700 text-white px-6 py-3 rounded-lg"
              >
                Predict Disease
              </Link>

            </div>

          ) : (

            <table className="w-full">

              <thead>

                <tr className="bg-green-700 text-white">

                  <th className="p-3">Disease</th>
                  <th className="p-3">Confidence</th>
                  <th className="p-3">File</th>
                  <th className="p-3">Actions</th>

                </tr>

              </thead>

              <tbody>

                {predictions.map((item) => (

                  <tr key={item._id} className="border-b">

                    {editingId === item._id ? (

                      <>

                        <td className="p-3">

                          <input
                            value={editForm.disease}
                            onChange={(e) =>
                              setEditForm({
                                ...editForm,
                                disease: e.target.value,
                              })
                            }
                            className="border p-2 rounded w-full"
                          />

                        </td>

                        <td className="p-3">

                          <input
                            type="number"
                            value={editForm.confidence}
                            onChange={(e) =>
                              setEditForm({
                                ...editForm,
                                confidence: e.target.value,
                              })
                            }
                            className="border p-2 rounded w-full"
                          />

                        </td>

                        <td className="p-3">
                          {item.filename}
                        </td>

                        <td className="p-3">

                          <button
                            onClick={() => savePrediction(item._id)}
                            className="bg-green-600 text-white px-4 py-2 rounded mr-2"
                          >
                            {saving ? "Saving..." : "Save"}
                          </button>

                          <button
                            onClick={cancelEdit}
                            className="bg-gray-500 text-white px-4 py-2 rounded"
                          >
                            Cancel
                          </button>

                        </td>

                      </>

                    ) : (

                      <>

                        <td className="p-3">{item.disease}</td>

                        <td className="p-3">
                          {item.confidence}%
                        </td>

                        <td className="p-3">
                          {item.filename}
                        </td>

                        <td className="p-3">

                          <button
                            onClick={() => startEdit(item)}
                            className="bg-blue-600 text-white px-4 py-2 rounded mr-2"
                          >
                            Edit
                          </button>

                          <button
                            onClick={() => deletePrediction(item._id)}
                            className="bg-red-600 text-white px-4 py-2 rounded"
                          >
                            {deletingId === item._id
                              ? "Deleting..."
                              : "Delete"}
                          </button>

                        </td>

                      </>

                    )}

                  </tr>

                ))}

              </tbody>

            </table>

          )}

        </div>

      </div>

    </div>
  );
}