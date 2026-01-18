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

export default function CompanyPitchPrep() {
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
            {navItems.map((item) => (
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
        <section className="flex-1 px-10 py-8 bg-darkBg flex flex-col gap-8">
          <h1 className="text-2xl font-bold mb-1">Company Pitch Preparation</h1>
          <p className="text-gray-300 mb-6 text-sm">Prepare company details below to generate an AI-powered pitch that will impress investors.</p>
          <div className="flex flex-col md:flex-row gap-8">
            {/* Company Details Form */}
            <form className="flex-1 bg-cardBg rounded-xl p-6 flex flex-col gap-4">
              <div className="font-bold mb-2">Company Details</div>
              <input className="bg-[#232323] rounded px-4 py-2 text-white placeholder-gray-400" placeholder="Company Name" />
              <input className="bg-[#232323] rounded px-4 py-2 text-white placeholder-gray-400" placeholder="Industry" />
              <input className="bg-[#232323] rounded px-4 py-2 text-white placeholder-gray-400" placeholder="Target Customer" />
              <input className="bg-[#232323] rounded px-4 py-2 text-white placeholder-gray-400" placeholder="Unique Value Proposition" />
              <input className="bg-[#232323] rounded px-4 py-2 text-white placeholder-gray-400" placeholder="Key Message" />
              <button className="bg-orange text-black px-6 py-2 rounded font-bold mt-2 self-end hover:opacity-90 transition" type="submit">Generate Pitch</button>
            </form>
            {/* AI-Generated Pitch Card */}
            <div className="flex-1 bg-cardBg rounded-xl p-6 flex flex-col gap-4">
              <div className="font-bold mb-2 flex items-center gap-2">
                <svg className="w-6 h-6 text-orange" fill="currentColor" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="3" /></svg>
                AI-Generated Pitch
              </div>
              <textarea className="bg-[#232323] rounded px-4 py-2 text-white placeholder-gray-400 h-40 resize-none" value={"PitchBot Solutions is redefining the investment process..."} readOnly />
              <div className="flex items-center gap-2">
                <button className="bg-[#232323] border border-orange text-orange px-4 py-2 rounded font-bold hover:bg-orange hover:text-black transition flex items-center gap-2">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24"><path d="M8 12h8M12 8v8" /></svg>
                  Copy
                </button>
                <div className="flex-1 flex items-center gap-2 ml-4">
                  <span className="text-xs text-gray-400">Pitch Quality</span>
                  <div className="w-32 h-2 bg-[#232323] rounded">
                    <div className="h-2 bg-orange rounded" style={{ width: '80%' }}></div>
                  </div>
                  <span className="text-xs text-orange font-bold ml-2">80%</span>
                </div>
              </div>
            </div>
          </div>
          {/* Pro Tip Section */}
          <div className="bg-[#232323] rounded-xl p-6 border-l-4 border-orange mt-2 flex items-center gap-4">
            <div className="flex-1">
              <div className="font-bold text-white mb-1">Pro Tip: Refine Your Pitch</div>
              <div className="text-gray-300 text-sm">For the best results, ensure your pitch details are concise, differentiated, and tailored to your target audience. Use the AI-generated pitch as a starting point, then personalize for maximum impact.</div>
            </div>
            <input className="bg-cardBg rounded px-4 py-2 text-white placeholder-gray-400 w-64" placeholder="Add your own notes..." />
          </div>
        </section>
      </main>
    </div>
  );
} 