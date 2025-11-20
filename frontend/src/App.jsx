import { Route, Routes, NavLink } from "react-router-dom";
import Home from "./pages/Home.jsx";
import AgentTrace from "./pages/AgentTrace.jsx";
import LogsPage from "./pages/LogsPage.jsx";
import FinalOutput from "./pages/FinalOutput.jsx";

const navLinks = [
  { to: "/", label: "Home" },
  { to: "/trace", label: "Agent Trace" },
  { to: "/logs", label: "Logs" },
  { to: "/output", label: "Final Output" },
];

function App() {
  return (
    <div className="min-h-screen text-white relative z-10">
      <nav className="border-b border-white/5 bg-black/40 backdrop-blur-xl sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="text-2xl font-bold tracking-tight gradient-text">
            AI Capstone Agents
          </div>
          <div className="flex gap-2 text-sm">
            {navLinks.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                className={({ isActive }) =>
                  `nav-link px-4 py-2 rounded-lg transition-all ${isActive
                    ? "bg-purple-500/10 text-purple-300"
                    : "text-gray-400 hover:text-purple-300"
                  }`
                }
              >
                {item.label}
              </NavLink>
            ))}
          </div>
        </div>
      </nav>
      <main className="max-w-6xl mx-auto px-6 py-10 space-y-10 relative z-10">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/trace" element={<AgentTrace />} />
          <Route path="/logs" element={<LogsPage />} />
          <Route path="/output" element={<FinalOutput />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
