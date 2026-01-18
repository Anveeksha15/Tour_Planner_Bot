import React from "react";

export default function RightPanel() {
  return (
    <div className="bg-cardBg rounded-2xl px-12 py-10 w-[400px] shadow-xl">
      <div className="flex items-center mb-6">
        {/* Logo Icon */}
        <svg className="w-7 h-7 mr-2 text-orange" fill="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
        <span className="text-white font-bold text-lg">PitchDeck AI<br /><span className="font-normal">Flow</span></span>
      </div>
      <h2 className="text-white text-2xl font-bold mb-1">Create your account</h2>
      <p className="text-gray-400 text-sm mb-8">
        Join thousands of professionals improving their pitch skills
      </p>
      <form className="space-y-5">
        <div>
          <label className="block text-gray-300 text-sm mb-1">Full Name</label>
          <input type="text" className="w-full p-3 rounded bg-inputBg text-white focus:outline-none" placeholder="Enter your full name" />
        </div>
        <div>
          <label className="block text-gray-300 text-sm mb-1">Email Address</label>
          <input type="email" className="w-full p-3 rounded bg-inputBg text-white focus:outline-none" placeholder="Enter your email" />
        </div>
        <div>
          <label className="block text-gray-300 text-sm mb-1">Password</label>
          <input type="password" className="w-full p-3 rounded bg-inputBg text-white focus:outline-none" placeholder="Create a password" />
          <span className="text-xs text-gray-500 ml-1">
            Must be at least 8 characters with 1 number and 1 special character
          </span>
        </div>
        <div className="flex items-center text-xs mt-2">
          <input type="checkbox" className="mr-2 bg-inputBg accent-orange" />
          <span className="text-gray-400">
            I agree to the <span className="text-orange underline cursor-pointer">Terms of Service</span> — <span className="text-orange underline cursor-pointer">Privacy Policy</span>
          </span>
        </div>
        <button type="submit" className="w-full py-3 mt-2 rounded bg-orange text-white font-bold text-lg hover:opacity-90 transition">Create Account</button>
      </form>
      <div className="flex items-center justify-center my-5">
        <hr className="w-10 border-gray-700" />
        <span className="mx-2 text-gray-500 text-sm">or continue with</span>
        <hr className="w-10 border-gray-700" />
      </div>
      <div className="flex gap-4 mb-2">
        <button className="flex-1 flex items-center justify-center gap-2 bg-darkBg border border-orange rounded py-2 text-white font-bold hover:bg-orange hover:text-darkBg transition">
          {/* Google Icon */}
          <svg className="w-5 h-5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#222326"/><text x="6" y="17" fontSize="10" fill="#ff9900">G</text></svg>
          Google
        </button>
        <button className="flex-1 flex items-center justify-center gap-2 bg-darkBg border border-orange rounded py-2 text-white font-bold hover:bg-orange hover:text-darkBg transition">
          {/* LinkedIn Icon */}
          <svg className="w-5 h-5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#222326"/><text x="4" y="17" fontSize="10" fill="#ff9900">in</text></svg>
          LinkedIn
        </button>
      </div>
      <div className="mt-6 text-center">
        <span className="text-gray-500 text-sm">
          Already have an account? <a className="text-orange underline cursor-pointer" href="#">Sign in</a>
        </span>
      </div>
    </div>
  );
}
