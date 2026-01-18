import React from "react";

export default function LeftPanel() {
  return (
    <div className="p-12 flex flex-col justify-center h-full bg-darkBg">
      <div className="max-w-md">
        <h1 className="text-4xl font-bold text-white mb-4">
          Elevate Your <span className="text-white">Pitch</span>
        </h1>
        <p className="text-gray-300 text-lg mb-8">
          Create compelling presentations with real-time AI feedback and coaching
        </p>
        <ul className="space-y-6 text-base">
          <li className="flex items-center">
            <span className="mr-4">
              {/* Play Icon */}
              <svg width="24" height="24" fill="none" viewBox="0 0 24 24" className="text-orange"><circle cx="12" cy="12" r="12" fill="currentColor"/><polygon points="10,8 16,12 10,16" fill="#222326"/></svg>
            </span>
            <span className="text-white">AI-powered presentation analysis</span>
          </li>
          <li className="flex items-center">
            <span className="mr-4">
              {/* Bar Chart Icon */}
              <svg width="24" height="24" fill="none" viewBox="0 0 24 24" className="text-orange"><circle cx="12" cy="12" r="12" fill="currentColor"/><rect x="8" y="12" width="2" height="4" fill="#222326"/><rect x="12" y="10" width="2" height="6" fill="#222326"/><rect x="16" y="8" width="2" height="8" fill="#222326"/></svg>
            </span>
            <span className="text-white">Data-driven improvement suggestions</span>
          </li>
          <li className="flex items-center">
            <span className="mr-4">
              {/* Feedback Icon */}
              <svg width="24" height="24" fill="none" viewBox="0 0 24 24" className="text-orange"><circle cx="12" cy="12" r="12" fill="currentColor"/><path d="M8 12h8M8 16h5" stroke="#222326" strokeWidth="2" strokeLinecap="round"/></svg>
            </span>
            <span className="text-white">Real-time delivery feedback</span>
          </li>
        </ul>
      </div>
    </div>
  );
}
