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

const partners = [
  {
    name: "Sarah Chen",
    title: "Partner, Sequoia Capital",
    desc: "Expert in SaaS, AI, and large-scale enterprise growth. Focused on early-stage investments.",
    img: "https://randomuser.me/api/portraits/women/44.jpg",
    bg: "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=400&q=80"
  },
  {
    name: "M.J. Williams",
    title: "Managing Partner, GrowthX",
    desc: "Specializes in fintech and B2B SaaS. Known for hands-on mentorship and scaling startups.",
    img: "https://randomuser.me/api/portraits/men/32.jpg",
    bg: "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80"
  },
  {
    name: "Mai Lan",
    title: "Principal, Vertex Ventures",
    desc: "Deep experience in healthtech and consumer apps. Passionate about impact investing.",
    img: "https://randomuser.me/api/portraits/women/65.jpg",
    bg: "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80"
  },
  {
    name: "Klaus Viktor",
    title: "Partner, Northzone",
    desc: "Focus on marketplaces and logistics. Invests in high-growth European startups.",
    img: "https://randomuser.me/api/portraits/men/45.jpg",
    bg: "https://images.unsplash.com/photo-1465101178521-c1a9136a3b99?auto=format&fit=crop&w=400&q=80"
  },
  {
    name: "Nia Lang",
    title: "Venture Partner, Lightspeed",
    desc: "Expert in product-led growth and SaaS. Loves working with diverse founding teams.",
    img: "https://randomuser.me/api/portraits/women/68.jpg",
    bg: "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80"
  },
  {
    name: "Tej Patel",
    title: "General Partner, Accel",
    desc: "Specializes in AI, cloud, and security. Invests in global scale-ups.",
    img: "https://randomuser.me/api/portraits/men/67.jpg",
    bg: "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=400&q=80"
  }
];

const features = [
  {
    title: "Discovery",
    desc: "Explore a wide range of VC partners, simulating their questioning styles, investing their specialties using AI investor personas.",
    icon: (
      <svg className="w-7 h-7 text-orange" fill="none" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="currentColor" /></svg>
    ),
  },
  {
    title: "Industry Knowledge",
    desc: "Understand what matters most to each investor, from SaaS metrics to healthcare innovation.",
    icon: (
      <svg className="w-7 h-7 text-orange" fill="none" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="3" fill="currentColor" /></svg>
    ),
  },
  {
    title: "Personalized Simulation",
    desc: "Practice your pitch with tailored feedback and simulated Q&A from your chosen VC persona.",
    icon: (
      <svg className="w-7 h-7 text-orange" fill="none" viewBox="0 0 24 24"><polygon points="12,2 22,22 2,22" fill="currentColor" /></svg>
    ),
  },
];

export default function VcPartners() {
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
          <h1 className="text-2xl font-bold mb-1">Venture Capitalist Partners</h1>
          <p className="text-gray-300 mb-6 text-sm">Explore our network of outstanding profiles that PitchDeck AI can simulate and challenge your pitch for positive outcomes.</p>
          {/* Search Bar */}
          <div className="flex mb-6">
            <input className="flex-1 bg-cardBg rounded-l px-4 py-2 text-white placeholder-gray-400 border border-[#232323]" placeholder="Search partners..." />
            <button className="bg-orange text-black px-6 py-2 rounded-r font-bold hover:opacity-90 transition">Search</button>
          </div>
          {/* VC Partner Cards Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-8">
            {partners.map((p, i) => (
              <div key={p.name} className="bg-cardBg rounded-xl overflow-hidden shadow-lg flex flex-col">
                <div className="h-32 w-full bg-cover bg-center" style={{ backgroundImage: `url(${p.bg})` }}></div>
                <div className="flex items-center gap-4 px-6 -mt-8">
                  <img src={p.img} alt={p.name} className="w-16 h-16 rounded-full border-4 border-orange bg-cardBg" />
                  <div className="flex-1">
                    <div className="font-bold text-lg text-white">{p.name}</div>
                    <div className="text-xs text-gray-400 mb-1">{p.title}</div>
                  </div>
                </div>
                <div className="px-6 pb-4 pt-2 flex-1 flex flex-col">
                  <div className="text-sm text-gray-300 mb-4 flex-1">{p.desc}</div>
                  <button className="text-orange text-sm font-bold hover:underline self-end">Page &gt;</button>
                </div>
              </div>
            ))}
          </div>
          {/* How Investor Simulation Works */}
          <div className="flex flex-col md:flex-row gap-8 mb-8">
            {features.map((f, i) => (
              <div key={f.title} className="flex-1 bg-cardBg rounded-xl p-6 flex flex-col items-start">
                <div className="mb-3">{f.icon}</div>
                <h4 className="font-bold text-lg mb-1">{f.title}</h4>
                <p className="text-gray-400 text-sm mb-4">{f.desc}</p>
              </div>
            ))}
          </div>
          {/* CTA Bar */}
          <div className="flex gap-8 items-start">
            <div className="flex-1 flex gap-4">
              <button className="bg-orange text-black px-6 py-2 rounded font-bold hover:opacity-90 transition">Request New Company Profile</button>
              <button className="bg-cardBg text-orange px-6 py-2 rounded font-bold border border-orange hover:bg-orange hover:text-black transition">Contact Us</button>
            </div>
            <div className="w-64 bg-orange rounded-xl p-6 flex flex-col items-center text-black font-bold text-center text-sm">
              <span className="mb-2">Pro Tip: Study your target VC's background and portfolio to tailor your pitch and anticipate their questions.</span>
              <svg className="w-10 h-10 text-black" fill="currentColor" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="3" /></svg>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
} 