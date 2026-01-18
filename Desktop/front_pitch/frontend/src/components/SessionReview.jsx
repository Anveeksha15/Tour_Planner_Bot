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

export default function SessionReview() {
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
          {/* Session Header */}
          <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-2">
            <div>
              <h1 className="text-2xl font-bold mb-1">Pitch Session Review</h1>
              <div className="text-gray-400 text-sm">Monday, May 13, 2024 &bull; 12:45 PM</div>
            </div>
            <div className="flex gap-2">
              <button className="bg-cardBg px-4 py-2 rounded text-sm text-white border border-[#232323]">Download Report</button>
              <button className="bg-orange px-4 py-2 rounded text-sm text-black font-bold">Share</button>
            </div>
          </div>
          {/* Pie Charts Row */}
          <div className="flex flex-wrap gap-8 mb-2">
            {["Overall Performance", "Response Quality", "Clarity Score"].map((label, i) => (
              <div key={label} className="flex flex-col items-center bg-cardBg rounded-xl p-4 w-64">
                <div className="text-sm font-bold mb-2">{label}</div>
                <svg width="100" height="100" viewBox="0 0 100 100">
                  <circle cx="50" cy="50" r="40" fill="#232323" />
                  <path d="M50 50 L50 10 A40 40 0 0 1 90 50 Z" fill="#ff9900" />
                  <path d="M50 50 L90 50 A40 40 0 1 1 50 10 Z" fill="#26e67c" />
                  <path d="M50 50 L50 90 A40 40 0 0 1 10 50 Z" fill="#fff" fillOpacity="0.2" />
                </svg>
                <div className="flex justify-between w-full text-xs mt-2">
                  <span className="text-orange">Pitch</span>
                  <span className="text-green-400">Q&A</span>
                  <span className="text-gray-400">Other</span>
                </div>
              </div>
            ))}
          </div>
          {/* Performance Trends & Key Areas */}
          <div className="flex flex-col md:flex-row gap-8">
            <div className="flex-1 bg-cardBg rounded-xl p-6">
              <div className="font-bold mb-2">Performance Trends</div>
              <svg width="100%" height="60" viewBox="0 0 400 60">
                <rect x="0" y="0" width="400" height="60" fill="#232323" />
                <polyline points="0,50 40,40 80,35 120,30 160,25 200,20 240,25 280,30 320,35 360,40 400,45" fill="none" stroke="#ff9900" strokeWidth="4" />
              </svg>
            </div>
            <div className="w-96 bg-cardBg rounded-xl p-6 flex flex-col gap-2">
              <div className="font-bold mb-2">Key Areas for Improvement</div>
              {[{label: "Response Quality", value: 78}, {label: "Content Clarity", value: 64}, {label: "Engagement", value: 82}, {label: "Organization", value: 56}].map((item) => (
                <div key={item.label} className="mb-2">
                  <div className="flex justify-between text-xs mb-1">
                    <span>{item.label}</span>
                    <span className="text-orange">{item.value}%</span>
                  </div>
                  <div className="w-full h-2 bg-[#232323] rounded">
                    <div className="h-2 bg-orange rounded" style={{ width: `${item.value}%` }}></div>
                  </div>
                </div>
              ))}
            </div>
          </div>
          {/* Q&A Section */}
          <div className="bg-cardBg rounded-xl p-6">
            <div className="font-bold mb-4">All Questions &amp; Your Responses</div>
            {[1,2,3,4].map((q) => (
              <div key={q} className="mb-4">
                <div className="text-orange font-bold mb-1">Question {q}:</div>
                <div className="text-gray-300 mb-1 text-sm">Explain your biggest market need and why they need your solution.</div>
                <div className="bg-[#232323] rounded-lg px-4 py-2 text-sm text-white">Our solution addresses a significant gap in the market by providing...</div>
              </div>
            ))}
          </div>
          {/* Delivery & Content Analysis */}
          <div className="flex flex-col md:flex-row gap-8">
            <div className="flex-1 bg-cardBg rounded-xl p-6">
              <div className="font-bold mb-2">Delivery Analysis</div>
              <div className="flex flex-col gap-2 mb-2">
                {[{label: "Pace", value: 72}, {label: "Filler Words", value: 18}, {label: "Voice Modulation", value: 85}].map((item) => (
                  <div key={item.label} className="mb-1">
                    <div className="flex justify-between text-xs mb-1">
                      <span>{item.label}</span>
                      <span className="text-orange">{item.value}%</span>
                    </div>
                    <div className="w-full h-2 bg-[#232323] rounded">
                      <div className="h-2 bg-orange rounded" style={{ width: `${item.value}%` }}></div>
                    </div>
                  </div>
                ))}
              </div>
              <svg width="100%" height="40" viewBox="0 0 400 40">
                <rect x="0" y="0" width="400" height="40" fill="#232323" />
                <polyline points="0,30 40,28 80,25 120,20 160,18 200,15 240,18 280,20 320,25 360,28 400,30" fill="none" stroke="#ff9900" strokeWidth="3" />
              </svg>
            </div>
            <div className="flex-1 bg-cardBg rounded-xl p-6">
              <div className="font-bold mb-2">Content Analysis</div>
              <div className="flex flex-col gap-2 mb-2">
                {[{label: "Market Positioning", value: 80}, {label: "Value Proposition", value: 70}, {label: "Storytelling", value: 65}].map((item) => (
                  <div key={item.label} className="mb-1">
                    <div className="flex justify-between text-xs mb-1">
                      <span>{item.label}</span>
                      <span className="text-orange">{item.value}%</span>
                    </div>
                    <div className="w-full h-2 bg-[#232323] rounded">
                      <div className="h-2 bg-orange rounded" style={{ width: `${item.value}%` }}></div>
                    </div>
                  </div>
                ))}
              </div>
              <svg width="100%" height="40" viewBox="0 0 400 40">
                <rect x="0" y="0" width="400" height="40" fill="#232323" />
                <polyline points="0,30 40,28 80,25 120,20 160,18 200,15 240,18 280,20 320,25 360,28 400,30" fill="none" stroke="#26e67c" strokeWidth="3" />
              </svg>
            </div>
          </div>
          {/* Call to Action Bar */}
          <div className="bg-orange rounded-xl p-6 flex items-center justify-between mt-2">
            <div className="font-bold text-black">Ready to improve your pitch?</div>
            <button className="bg-black text-orange px-6 py-2 rounded font-bold hover:bg-[#232323] transition">Get Feedback</button>
          </div>
          {/* All Feedback Summary */}
          <div className="bg-cardBg rounded-xl p-6 mt-2">
            <div className="font-bold mb-4">All Feedback Summary</div>
            <div className="flex flex-col md:flex-row gap-8">
              <div className="flex-1 flex flex-col gap-2">
                <div className="flex items-center gap-2 mb-1">
                  <svg className="w-5 h-5 text-orange" fill="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /></svg>
                  <span className="font-bold text-orange">Strengths</span>
                </div>
                <div className="text-xs text-gray-300 mb-2">Strong market understanding, clear value proposition, and effective use of visuals for trend illustration.</div>
                <div className="flex items-center gap-2 mb-1">
                  <svg className="w-5 h-5 text-orange" fill="currentColor" viewBox="0 0 24 24"><polygon points="12,2 22,22 2,22" /></svg>
                  <span className="font-bold text-orange">Opportunities</span>
                </div>
                <div className="text-xs text-gray-300 mb-2">Could improve storytelling and engagement, especially when explaining complex data.</div>
                <div className="flex items-center gap-2 mb-1">
                  <svg className="w-5 h-5 text-orange" fill="currentColor" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="3" /></svg>
                  <span className="font-bold text-orange">Areas to Improve</span>
                </div>
                <div className="text-xs text-gray-300 mb-2">Work on pacing and clarity, and reduce filler words during transitions.</div>
              </div>
              <div className="flex-1 flex flex-col gap-2">
                <div className="font-bold mb-2">Score Breakdown</div>
                <div className="flex flex-col gap-2">
                  {[{label: "Overall", value: 82}, {label: "Delivery", value: 76}, {label: "Content", value: 88}].map((item) => (
                    <div key={item.label} className="mb-1">
                      <div className="flex justify-between text-xs mb-1">
                        <span>{item.label}</span>
                        <span className="text-orange">{item.value}%</span>
                      </div>
                      <div className="w-full h-2 bg-[#232323] rounded">
                        <div className="h-2 bg-orange rounded" style={{ width: `${item.value}%` }}></div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
} 