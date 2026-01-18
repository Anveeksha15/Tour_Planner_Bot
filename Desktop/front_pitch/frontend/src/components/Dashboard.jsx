import React from "react";

const navItems = [
  { label: "Sign Up", icon: "👤" },
  { label: "Pitch Session", icon: "🎤" },
  { label: "Analytics", icon: "📊" },
  { label: "My Decks", icon: "📁" },
  { label: "VC Network", icon: "🌐" },
  { label: "Company Profile", icon: "🏢" },
  { label: "Settings", icon: "⚙️" },
];

const recentUploads = [
  { name: "Test1_Pitch_v2.pdf", date: "Uploaded 1 min ago" },
  { name: "Investor_Deck_2023.ppt", date: "Uploaded 3 min ago" },
  { name: "Seed_Round_Pitch.ppt", date: "Uploaded 5 min ago" },
];

const features = [
  {
    title: "AI Investor Simulation",
    desc: "Our AI simulates real investor questions based on your pitch deck content and delivery.",
    cta: "Try voice Q&A →",
    icon: (
      <svg className="w-7 h-7 text-orange" fill="none" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="currentColor" /></svg>
    ),
  },
  {
    title: "Performance Analytics",
    desc: "Get detailed feedback on your pitch delivery, including pacing, clarity, and persuasiveness.",
    cta: "View analytics →",
    icon: (
      <svg className="w-7 h-7 text-orange" fill="none" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="currentColor" /></svg>
    ),
  },
  {
    title: "VC Personas",
    desc: "Practice with different investor personas, from angel investors to VCs.",
    cta: "Explore personas →",
    icon: (
      <svg className="w-7 h-7 text-orange" fill="none" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="currentColor" /></svg>
    ),
  },
];

export default function Dashboard() {
  return (
    <div className="flex min-h-screen bg-darkBg text-white">
      {/* Sidebar */}
      <aside className="w-64 bg-cardBg flex flex-col py-6 px-4 min-h-screen border-r border-[#232323]">
        <div className="flex items-center mb-10">
          <svg className="w-8 h-8 text-orange mr-2" fill="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
          <span className="font-bold text-lg leading-tight">PitchDeck AI<br /><span className="font-normal">Flow</span></span>
        </div>
        <nav className="flex-1">
          <ul className="space-y-2">
            {navItems.map((item, i) => (
              <li key={item.label} className="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-[#232323] cursor-pointer text-sm font-medium">
                <span className="text-orange text-lg">{item.icon}</span>
                <span>{item.label}</span>
              </li>
            ))}
          </ul>
        </nav>
        <div className="mt-8 bg-[#232323] rounded-lg p-4">
          <div className="text-xs text-gray-300 mb-2">Upcoming</div>
          <div className="text-sm mb-3">Your scheduled pitch practice with 'NextGen VC' is in 2 hours.</div>
          <button className="w-full py-2 rounded bg-orange text-black font-bold text-sm hover:opacity-90 transition">Prepare Now</button>
        </div>
      </aside>
      {/* Main Content */}
      <main className="flex-1 flex flex-col min-h-screen bg-darkBg">
        {/* Top Bar */}
        <header className="flex items-center justify-between px-10 py-5 border-b border-[#232323] bg-darkBg">
          <div className="flex items-center gap-2">
            <button className="bg-cardBg px-4 py-2 rounded text-sm text-white border border-[#232323] mr-2">New Session</button>
            <button className="bg-orange px-4 py-2 rounded text-sm text-black font-bold">Start Pitch</button>
          </div>
          <div className="flex items-center gap-4">
            <span className="text-sm">Alex</span>
            <div className="w-8 h-8 rounded-full bg-gray-500 flex items-center justify-center text-white font-bold">A</div>
          </div>
        </header>
        {/* Content Area */}
        <section className="flex-1 px-10 py-8 bg-darkBg">
          <h1 className="text-3xl font-bold mb-2">Start Your <span className="text-orange">AI-Powered Pitch Session</span></h1>
          <p className="text-gray-300 mb-8">Upload your pitch deck and practice with our AI investor simulation</p>
          {/* Upload & Simulation */}
          <div className="flex gap-8 mb-8">
            <div className="flex-1 bg-cardBg rounded-xl p-6 flex flex-col items-center">
              <h2 className="text-lg font-bold mb-2">Upload Your Pitch Deck</h2>
              <p className="text-gray-400 text-xs mb-4">Supported formats: PDF, PPT, PPTX (Max: 50MB)</p>
              <button className="bg-[#232323] border border-orange text-orange px-6 py-2 rounded font-bold hover:bg-orange hover:text-black transition">Choose File</button>
            </div>
            <div className="flex-1 bg-cardBg rounded-xl p-6 flex flex-col items-center">
              <h2 className="text-lg font-bold mb-2">Start Pitch Simulation</h2>
              <p className="text-gray-400 text-xs mb-4">Practice your pitch with AI-simulated investor questions</p>
              <button className="bg-orange text-black px-6 py-2 rounded font-bold hover:opacity-90 transition">Start Session</button>
            </div>
          </div>
          {/* Recent Uploads */}
          <div className="bg-cardBg rounded-xl p-6 mb-8">
            <h3 className="text-lg font-bold mb-4">Your recent uploads will appear here</h3>
            <div className="flex gap-6">
              {recentUploads.map((file, i) => (
                <div key={file.name} className="flex flex-col items-center bg-[#232323] rounded-lg p-4 w-48">
                  <svg className="w-10 h-10 text-orange mb-2" fill="currentColor" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="3" fill="currentColor" /></svg>
                  <span className="text-sm font-bold mb-1 text-white truncate w-full text-center">{file.name}</span>
                  <span className="text-xs text-gray-400">{file.date}</span>
                </div>
              ))}
            </div>
          </div>
          {/* Features */}
          <div className="flex gap-8 mb-8">
            {features.map((f, i) => (
              <div key={f.title} className="flex-1 bg-cardBg rounded-xl p-6 flex flex-col items-start">
                <div className="mb-3">{f.icon}</div>
                <h4 className="font-bold text-lg mb-1">{f.title}</h4>
                <p className="text-gray-400 text-sm mb-4">{f.desc}</p>
                <button className="text-orange text-sm font-bold hover:underline p-0 m-0 bg-transparent">{f.cta}</button>
              </div>
            ))}
          </div>
          {/* Pro Tip */}
          <div className="bg-[#232323] rounded-xl p-6 border-l-4 border-orange">
            <h5 className="font-bold text-white mb-1">Pro Tip: Prepare for Success</h5>
            <p className="text-gray-300 text-sm mb-2">For the best results, ensure your pitch deck clearly outlines your value proposition, market opportunity, business model, and financials. AI will focus questions on these key areas.</p>
            <span className="text-orange text-xs font-bold cursor-pointer hover:underline">Upgrade to Pro for advanced features →</span>
          </div>
        </section>
      </main>
    </div>
  );
} 