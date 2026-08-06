"use client";

import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 bg-green-700 shadow-lg">
      <div className="max-w-7xl mx-auto px-6 py-4 flex flex-col md:flex-row justify-between items-center">
        <h1 className="text-3xl font-bold text-white">
          🌱 AI Crop Disease Detection
        </h1>

        <div className="flex gap-6 text-white font-medium mt-4 md:mt-0">
          <Link href="/" className="hover:text-green-200 transition">
            Home
          </Link>

          <Link href="/history" className="hover:text-green-200 transition">
            History
          </Link>

          <Link href="/dashboard" className="hover:text-green-200 transition">
            Dashboard
          </Link>

          <Link href="/login" className="hover:text-green-200 transition">
            Login
          </Link>
        </div>
      </div>
    </nav>
  );
}