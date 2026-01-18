// src/App.js

import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LeftPanel from "./components/LeftPanel";
import RightPanel from "./components/RightPanel";
import Dashboard from "./components/Dashboard";
import VoiceAgent from "./components/VoiceAgent";
import SessionReview from "./components/SessionReview";
import CompanyPitchPrep from "./components/CompanyPitchPrep";
import VcPartners from "./components/VcPartners";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={
            <div className="min-h-screen flex bg-darkBg font-sans">
              <div className="flex-[1.1] flex items-center justify-end pr-4 bg-darkBg">
                <LeftPanel />
              </div>
              <div className="flex-1 flex items-center justify-start pl-4 bg-darkBg">
                <RightPanel />
              </div>
            </div>
          }
        />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/voice-agent" element={<VoiceAgent />} />
        <Route path="/session-review" element={<SessionReview />} />
        <Route path="/company-pitch-prep" element={<CompanyPitchPrep />} />
        <Route path="/vc-partners" element={<VcPartners />} />
      </Routes>
    </Router>
  );
}
