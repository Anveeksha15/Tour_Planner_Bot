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

export default function VoiceAgent() {
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
        <section className="flex-1 px-10 py-8 bg-darkBg flex gap-8">
          {/* Main Chat Area */}
          <div className="flex-1 flex flex-col gap-6">
            <h1 className="text-2xl font-bold mb-2">Voice Q&amp;A Session</h1>
            <p className="text-gray-300 mb-2 text-sm">Real-time, personalized Q&amp;A with AI investor personas</p>
            {/* Chat Bubbles */}
            <div className="bg-cardBg rounded-xl p-6 flex flex-col gap-4 mb-2">
              {/* Investor Bubble */}
              <div className="flex items-start gap-4">
                <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Investor" className="w-12 h-12 rounded-full border-2 border-orange" />
                <div>
                  <div className="font-bold text-white">Sarah Chen <span className="text-xs text-gray-400 font-normal ml-2">Partner at Sequoia Capital</span></div>
                  <div className="bg-[#232323] rounded-lg px-4 py-2 mt-1 text-sm text-white max-w-xl">Tell me about your revenue model. How do you plan to monetize your product?</div>
                </div>
              </div>
              {/* Agent Bubble (speaking) */}
              <div className="flex items-start gap-4">
                <div className="w-12 h-12 rounded-full bg-orange flex items-center justify-center text-black font-bold text-xl">A</div>
                <div>
                  <div className="font-bold text-white">You <span className="text-xs text-green-400 font-normal ml-2">Active</span></div>
                  <div className="bg-[#232323] rounded-lg px-4 py-2 mt-1 text-sm text-orange max-w-xl flex items-center gap-2">
                    <span>We have a tiered subscription model. Our freemium tier offers basic features, while our premium tiers are $29 and $99 per month, providing advanced analytics and priority support. We also offer volume discounts for enterprise customers.</span>
                    <span className="animate-pulse text-orange">●●●</span>
                  </div>
                </div>
              </div>
              {/* Investor Follow-up */}
              <div className="flex items-start gap-4">
                <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Investor" className="w-12 h-12 rounded-full border-2 border-orange" />
                <div>
                  <div className="font-bold text-white">Sarah Chen <span className="text-xs text-gray-400 font-normal ml-2">Partner at Sequoia Capital</span></div>
                  <div className="bg-[#232323] rounded-lg px-4 py-2 mt-1 text-sm text-white max-w-xl">That's interesting. What is your estimated acquisition cost, and how does that compare to your lifetime value?</div>
                </div>
              </div>
            </div>
            {/* Voice Input Box */}
            <div className="flex items-center bg-cardBg rounded-xl px-4 py-3 gap-3">
              <span className="text-gray-400 text-sm flex-1">Voice recognition active - speak your response</span>
              <input className="flex-1 bg-transparent outline-none text-white placeholder-gray-400" placeholder="Type your response or press the mic button..." />
              <button className="bg-orange rounded-full w-12 h-12 flex items-center justify-center ml-2 hover:scale-105 transition" title="Speak">
                <svg className="w-6 h-6 text-black" fill="currentColor" viewBox="0 0 24 24"><path d="M12 18c1.66 0 3-1.34 3-3V7c0-1.66-1.34-3-3-3s-3 1.34-3 3v8c0 1.66 1.34 3 3 3zm5-3c0 2.33-1.46 4.32-3.5 4.77V21h-3v-1.23C8.46 19.32 7 17.33 7 15h2c0 1.3.84 2.4 2 2.82V21h2v-3.18c1.16-.42 2-1.52 2-2.82h2z" /></svg>
              </button>
            </div>
            {/* Session Controls */}
            <div className="bg-cardBg rounded-xl p-4 flex gap-4 items-center mt-2">
              <button className="bg-[#232323] text-white px-4 py-2 rounded font-bold">Pause Session</button>
              <button className="bg-[#232323] text-white px-4 py-2 rounded font-bold">Repeat Question</button>
              <button className="bg-[#232323] text-white px-4 py-2 rounded font-bold">Adjust Volume</button>
              <button className="bg-red-600 text-white px-6 py-2 rounded font-bold ml-auto">End Q&amp;A Session</button>
            </div>
          </div>
          {/* Right Sidebar: Investor Profile, Analytics, Suggestions */}
          <div className="w-[350px] flex flex-col gap-6">
            {/* AI Investor Profile */}
            <div className="bg-cardBg rounded-xl p-5 flex flex-col items-center">
              <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Investor" className="w-16 h-16 rounded-full border-2 border-orange mb-2" />
              <div className="font-bold text-white">Sarah Chen</div>
              <div className="text-xs text-gray-400 mb-2">Partner at Sequoia Capital</div>
              <div className="flex items-center gap-1 mb-1">
                {[...Array(5)].map((_, i) => (
                  <svg key={i} className="w-4 h-4 text-orange" fill="currentColor" viewBox="0 0 20 20"><polygon points="10,1 12,7 18,7 13,11 15,17 10,13 5,17 7,11 2,7 8,7" /></svg>
                ))}
              </div>
              <div className="text-xs text-gray-300 text-center">Nigerian-born AI English questions and answers on startup growth, product-market fit, and business models. Pitch decks since 2018.</div>
            </div>
            {/* Session Analytics */}
            <div className="bg-cardBg rounded-xl p-5">
              <div className="font-bold mb-2">Session Analytics</div>
              <div className="flex flex-col gap-2 mb-2">
                <div className="flex justify-between text-xs">
                  <span>Response Quality</span>
                  <span className="text-orange">81%</span>
                </div>
                <div className="w-full h-2 bg-[#232323] rounded">
                  <div className="h-2 bg-orange rounded" style={{ width: '81%' }}></div>
                </div>
                <div className="flex justify-between text-xs">
                  <span>Confidence Level</span>
                  <span className="text-orange">74%</span>
                </div>
                <div className="w-full h-2 bg-[#232323] rounded">
                  <div className="h-2 bg-orange rounded" style={{ width: '74%' }}></div>
                </div>
                <div className="flex justify-between text-xs">
                  <span>Data Accuracy</span>
                  <span className="text-orange">92%</span>
                </div>
                <div className="w-full h-2 bg-[#232323] rounded">
                  <div className="h-2 bg-orange rounded" style={{ width: '92%' }}></div>
                </div>
              </div>
              {/* Pie Chart Placeholder */}
              <div className="mt-4">
                <div className="text-xs mb-1">Top Question Categories</div>
                <div className="w-full flex justify-center">
                  <svg width="120" height="80" viewBox="0 0 120 80">
                    <circle cx="60" cy="40" r="32" fill="#232323" />
                    <path d="M60 40 L60 8 A32 32 0 0 1 92 40 Z" fill="#ff9900" />
                    <path d="M60 40 L92 40 A32 32 0 1 1 60 8 Z" fill="#26e67c" />
                    <path d="M60 40 L60 72 A32 32 0 0 1 28 40 Z" fill="#fff" fillOpacity="0.2" />
                  </svg>
                </div>
                <div className="flex justify-between text-xs mt-2">
                  <span className="text-orange">Revenue Model (40%)</span>
                  <span className="text-green-400">Competition (30%)</span>
                  <span className="text-gray-400">Other (30%)</span>
                </div>
              </div>
            </div>
            {/* Suggested Responses */}
            <div className="bg-cardBg rounded-xl p-5">
              <div className="font-bold mb-2">Suggested Responses</div>
              <div className="text-xs text-gray-300 mb-2">When planning an expanded digital marketing strategy, consider aligning spend with acquisition cost and expected LTV. Highlight your unique value proposition and traction.</div>
              <div className="text-xs text-gray-300 mb-2">Our gross margin includes recurring software revenue and professional services. Investors often look for >70% in SaaS businesses.</div>
              <div className="text-xs text-gray-300 mb-4">"We’re focusing on scaling CAC through community-building and channel partnerships. Explore more suggestions below."</div>
              <button className="w-full py-2 rounded bg-[#232323] border border-orange text-orange font-bold text-sm hover:bg-orange hover:text-black transition">Generate More Suggestions</button>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
} 