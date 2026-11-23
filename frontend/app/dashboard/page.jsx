
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import api from "../../lib/api";

export default function Dashboard() {
  const router = useRouter();

  const [user, setUser] = useState<any>(null);
  const [predictions, setPredictions] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [editingId, setEditingId] = useState<string | null>(null);

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

      await loadPredictions();
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
      console.error(err);
      setError("Unable to load prediction history.");
    } finally {
      setLoading(false);
    }
  };

  const startEdit = (item: any) => {
    setEditingId(item._id);

    setEditForm({
      disease: item.disease,
      confidence: String(item.confidence),
    });
  };

  const cancelEdit = () => {
    setEditingId(null);

    setEditForm({
      disease: "",
      confidence: "",
    });
  };

  const saveEdit = async (id: string) => {
    try {
      await api.put(`/predictions/${id}`, {
        disease: editForm.disease,
        confidence: Number(editForm.confidence),
      });

      await loadPredictions();
      setEditingId(null);
    } catch (err) {
      console.error(err);
      alert("Failed to update prediction.");
    }
  };

  const deletePrediction = async (id: string) => {
    if (!confirm("Delete this prediction?")) return;

    try {
      await api.delete(`/predictions/${id}`);
      await loadPredictions();
    } catch (err) {
      console.error(err);
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
            (sum: number, item: any) =>
              sum + Number(item.confidence),
            0
          ) / predictions.length
        ).toFixed(2)
      : "0.00";

  const latestPrediction =
    predictions.length > 0
      ? predictions[0].disease
      : "No Prediction";

  return (
    <div className="min-h-screen bg-gray-100 text-gray-900">

      {/* Navigation Bar */}
      <nav className="bg-green-700 text-white px-8 py-4 flex flex-wrap justify-between items-center gap-4">
        <h1 className="text-2xl md:text-3xl font-bold text-white">
          🌱 Crop Disease Detection
        </h1>

        <div className="flex gap-6 items-center text-white">
          <Link
            href="/"
            className="text-white hover:text-green-200"
          >
            Home
          </Link>

          <Link
            href="/history"
            className="text-white hover:text-green-200"
          >
            History
          </Link>

          <button
            onClick={logout}
            className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700"
          >
            Logout
          </button>
        </div>
      </nav>

      {/* Dashboard Content */}
      <main className="max-w-7xl mx-auto p-6 md:p-8">

        <h2 className="text-4xl font-bold mb-2 text-gray-900">
          Dashboard
        </h2>

        <p className="text-gray-700 mb-8">
          Welcome {user?.sub}
        </p>

        {/* Statistics Cards */}
        <div className="grid md:grid-cols-3 gap-6 mb-8">

          <div className="bg-green-600 text-white rounded-xl p-6 shadow">
            <h3 className="text-xl font-semibold text-white">
              Total Predictions
            </h3>

            <p className="text-5xl font-bold mt-4 text-white">
              {totalPredictions}
            </p>
          </div>

          <div className="bg-blue-600 text-white rounded-xl p-6 shadow">
            <h3 className="text-xl font-semibold text-white">
              Latest Prediction
            </h3>

            <p className="text-2xl mt-4 text-white break-words">
              {latestPrediction}
            </p>
          </div>

          <div className="bg-orange-500 text-white rounded-xl p-6 shadow">
            <h3 className="text-xl font-semibold text-white">
              Average Confidence
            </h3>

            <p className="text-5xl font-bold mt-4 text-white">
              {averageConfidence}%
            </p>
          </div>

        </div>

        {/* Error Message */}
        {error && (
          <div className="bg-red-100 text-red-800 border border-red-300 p-4 rounded-lg mb-6">
            {error}
          </div>
        )}

        {/* Loading State */}
        {loading ? (

          <div className="bg-white text-gray-800 rounded-xl shadow p-8 text-center">
            Loading prediction history...
          </div>

        ) : predictions.length === 0 ? (

          /* Empty State */
          <div className="bg-white rounded-xl shadow p-8 text-center">

            <h2 className="text-2xl font-bold mb-3 text-gray-900">
              No Predictions Yet
            </h2>

            <p className="text-gray-700">
              Upload a crop image to generate your first prediction.
            </p>

          </div>

        ) : (

          /* Prediction History Table */
          <div className="bg-white rounded-xl shadow-lg overflow-x-auto">

            <table className="w-full text-left">

              <thead>
                <tr className="bg-green-700 text-white">

                  <th className="p-4 text-white font-semibold">
                    Disease
                  </th>

                  <th className="p-4 text-white font-semibold">
                    Confidence
                  </th>

                  <th className="p-4 text-white font-semibold">
                    File
                  </th>

                  <th className="p-4 text-center text-white font-semibold">
                    Actions
                  </th>

                </tr>
              </thead>

              <tbody className="text-gray-800">

                {predictions.map((item: any) => (

                  <tr
                    key={item._id}
                    className="border-b border-gray-200 text-gray-800 hover:bg-gray-50"
                  >

                    {editingId === item._id ? (

                      <>
                        {/* Edit Disease */}
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
                            className="border border-gray-300 rounded-lg p-2 w-full bg-white text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-500"
                          />
                        </td>

                        {/* Edit Confidence */}
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
                            className="border border-gray-300 rounded-lg p-2 w-full bg-white text-gray-900 focus:outline-none focus:ring-2 focus:ring-green-500"
                          />
                        </td>

                        <td className="p-4 text-gray-800">
                          {item.filename}
                        </td>

                        <td className="p-4 text-center">
                          <div className="flex flex-wrap justify-center gap-2">

                            <button
                              onClick={() => saveEdit(item._id)}
                              className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700"
                            >
                              Save
                            </button>

                            <button
                              onClick={cancelEdit}
                              className="bg-gray-600 text-white px-4 py-2 rounded-lg hover:bg-gray-700"
                            >
                              Cancel
                            </button>

                          </div>
                        </td>
                      </>

                    ) : (

                      <>
                        <td className="p-4 text-gray-800 font-medium">
                          {item.disease}
                        </td>

                        <td className="p-4 text-gray-800 font-medium">
                          {item.confidence}%
                        </td>

                        <td className="p-4 text-gray-800">
                          {item.filename}
                        </td>

                        <td className="p-4 text-center">
                          <div className="flex flex-wrap justify-center gap-2">

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

      </main>

      {/* Footer */}
      <footer className="bg-green-700 text-white text-center py-4 mt-10">
        © 2026 AI Crop Disease Detection System
      </footer>

    </div>
  );
}
