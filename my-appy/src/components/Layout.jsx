// components/Layout.jsx

import Navbar from "./navbar";          // 1️⃣  top-level import
                                         // same directory -> “./”

export default function Layout({ children }) {
  return (
    <div className="min-h-screen bg-[#f6f5ff] text-gray-800 font-sans">

      <Navbar />                         {/* 2️⃣  just use the component */}
      {children}
    </div>
  );
}
