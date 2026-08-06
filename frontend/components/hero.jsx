"use client";

export default function Hero() {
  return (
    <section
      className="relative h-[75vh] bg-cover bg-center flex items-center justify-center"
      style={{
        backgroundImage: "url('/images/farm-bg.jpg')",
      }}
    >
      {/* Dark Overlay */}
      <div className="absolute inset-0 bg-black/60"></div>

      {/* Hero Content */}
      <div className="relative z-10 text-center text-white px-6 max-w-4xl">
        <h1 className="text-5xl md:text-6xl font-extrabold leading-tight">
          🌱 AI Crop Disease Detection
        </h1>

        <p className="mt-6 text-lg md:text-xl text-gray-200">
          Detect crop diseases instantly using Artificial Intelligence.
          Upload a crop leaf image and receive disease predictions,
          treatment recommendations, and prevention tips in seconds.
        </p>

        <button
          onClick={() =>
            document
              .getElementById("upload-section")
              ?.scrollIntoView({ behavior: "smooth" })
          }
          className="mt-8 bg-green-600 hover:bg-green-700 px-8 py-4 rounded-xl font-semibold text-lg transition duration-300 shadow-lg hover:scale-105"
        >
          🌿 Upload & Predict
        </button>
      </div>
    </section>
  );
}