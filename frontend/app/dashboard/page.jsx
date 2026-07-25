"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import api from "../../lib/api";

export default function Dashboard() {
  const router = useRouter();

  const [user, setUser] = useState(null);
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [editingId, setEditingId] = useState(null);

  const [editForm, setEditForm] = useState({
    disease: "",
    confidence: "",
  });

  useEffect(() => {
    checkLogin();
  }, []);

  const checkLogin = async () => {
    try {
      const profile = await api.get("/auth/profile");

      setUser(profile.data.user);

      loadPredictions();
    } catch (err) {
      localStorage.removeItem("token");
      router.push("/login");
    }
  };

  const loadPredictions = async () => {
    try {
      setLoading(true);

      const res = await api.get("/predictions");

      setPredictions(res.data);

      setError("");
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

  const saveEdit = async (id) => {
    try {
      await api.put(`/predictions/${id}`, {
        disease: editForm.disease,
        confidence: Number(editForm.confidence),
      });

      await loadPredictions();

      setEditingId(null);
    } catch (err) {
      alert("Failed to update prediction.");
    }
  };

  const deletePrediction = async (id) => {
    if (!confirm("Delete this prediction?")) return;

    try {
      await api.delete(`/predictions/${id}`);

      loadPredictions();
    } catch (err) {
      alert("Unable to delete prediction.");
    }
  };

  const logout = () => {
    localStorage.removeItem("token");

    router.push("/login");
  };

  const totalPredictions = predictions.length;

  const averageConfidence =
    predictions.length > 0
      ? (
          predictions.reduce(
            (sum, item) => sum + Number(item.confidence),
            0
          ) / predictions.length
        ).toFixed(2)
      : 0;

  const latestPrediction =
    predictions.length > 0
      ? predictions[0].disease
      : "No Prediction";

  return (
    <div className="min-h-screen bg-gray-100">

      <nav className="bg-green-700 text-white px-8 py-4 flex justify-between items-center">

        <h1 className="text-3xl font-bold">
          🌱 Crop Disease Detection
        </h1>

        <div className="flex gap-6 items-center">

          <Link href="/">Home</Link>

          <Link href="/history">History</Link>

          <button
            onClick={logout}
            className="bg-red-600 px-4 py-2 rounded-lg hover:bg-red-700"
          >
            Logout
          </button>

        </div>

      </nav>

      <div className="max-w-7xl mx-auto p-8">

        <h2 className="text-4xl font-bold mb-2">
          Dashboard
        </h2>

        <p className="text-gray-600 mb-8">
          Welcome {user?.sub}
        </p>

        <div className="grid md:grid-cols-3 gap-6 mb-8">

          <div className="bg-green-600 text-white rounded-xl p-6 shadow">

            <h3 className="text-xl font-semibold">
              Total Predictions
            </h3>

            <p className="text-5xl font-bold mt-4">
              {totalPredictions}
            </p>

          </div>

          <div className="bg-blue-600 text-white rounded-xl p-6 shadow">

            <h3 className="text-xl font-semibold">
              Latest Prediction
            </h3>

            <p className="text-2xl mt-4">
              {latestPrediction}
            </p>

          </div>

          <div className="bg-orange-500 text-white rounded-xl p-6 shadow">

            <h3 className="text-xl font-semibold">
              Average Confidence
            </h3>

            <p className="text-5xl font-bold mt-4">
              {averageConfidence}%
            </p>

          </div>

        </div>
                {error && (
          <div className="bg-red-100 text-red-700 p-4 rounded-lg mb-6">
            {error}
          </div>
        )}

        {loading ? (

          <div className="bg-white rounded-xl shadow p-8 text-center">
            Loading prediction history...
          </div>

        ) : predictions.length === 0 ? (

          <div className="bg-white rounded-xl shadow p-8 text-center">

            <h2 className="text-2xl font-bold mb-3">
              No Predictions Yet
            </h2>

            <p className="text-gray-600">
              Upload a crop image to generate your first prediction.
            </p>

          </div>

        ) : (

          <div className="bg-white rounded-xl shadow-lg overflow-x-auto">

            <table className="w-full">

              <thead>

                <tr className="bg-green-700 text-white">

                  <th className="p-4 text-left">Disease</th>

                  <th className="p-4 text-left">Confidence</th>

                  <th className="p-4 text-left">File</th>

                  <th className="p-4 text-center">Actions</th>

                </tr>

              </thead>

              <tbody>

                {predictions.map((item) => (

                  <tr
                    key={item._id}
                    className="border-b hover:bg-gray-50"
                  >

                    {editingId === item._id ? (

                      <>
                        <td className="p-4">

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

                        <td className="p-4">

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

                        <td className="p-4">
                          {item.filename}
                        </td>

                        <td className="p-4 text-center space-x-2">

                          <button
                            onClick={() => saveEdit(item._id)}
                            className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700"
                          >
                            Save
                          </button>

                          <button
                            onClick={cancelEdit}
                            className="bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-600"
                          >
                            Cancel
                          </button>

                        </td>

                      </>
                                          ) : (

                      <>

                        <td className="p-4">
                          {item.disease}
                        </td>

                        <td className="p-4">
                          {item.confidence}%
                        </td>

                        <td className="p-4">
                          {item.filename}
                        </td>

                        <td className="p-4 text-center space-x-2">

                          <button
                            onClick={() => startEdit(item)}
                            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
                          >
                            Edit
                          </button>

                          <button
                            onClick={() => deletePrediction(item._id)}
                            className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700"
                          >
                            Delete
                          </button>

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

      <footer className="bg-green-700 text-white text-center py-4 mt-10">
        © 2026 AI Crop Disease Detection System
      </footer>

    </div>
  );
}