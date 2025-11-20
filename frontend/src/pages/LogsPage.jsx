import { useEffect, useState } from "react";
import JsonViewer from "../components/JsonViewer.jsx";
import { api } from "../services/api.js";

function LogsPage() {
  const [logs, setLogs] = useState([]);
  const [memory, setMemory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;
    async function load() {
      try {
        const [logData, memoryData] = await Promise.all([
          api.fetchLogs(60),
          api.fetchMemory(),
        ]);
        if (mounted) {
          setLogs(logData);
          setMemory(memoryData);
        }
      } finally {
        if (mounted) setLoading(false);
      }
    }
    load();
    return () => {
      mounted = false;
    };
  }, []);

  if (loading) {
    return (
      <div className="text-white/70 bg-slate-900/60 rounded-3xl p-10 text-center border border-white/5">
        Loading logs...
      </div>
    );
  }

  return (
    <div className="grid md:grid-cols-2 gap-6">
      <div className="bg-slate-900/60 rounded-3xl p-6 border border-white/5">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold">Recent Logs</h3>
          <span className="text-xs uppercase text-white/50">{logs.length} entries</span>
        </div>
        <div className="space-y-3 max-h-[600px] overflow-y-auto pr-2">
          {logs.map((log, idx) => (
            <div
              key={idx}
              className="bg-slate-950/60 border border-white/5 rounded-2xl p-3 text-xs"
            >
              <div className="flex justify-between text-white/60 mb-1">
                <span>{log.agent.toUpperCase()}</span>
                <span>{new Date(log.timestamp).toLocaleTimeString()}</span>
              </div>
              <p className="text-white/80">{log.content_preview}</p>
            </div>
          ))}
        </div>
      </div>
      <div className="bg-slate-900/60 rounded-3xl p-6 border border-white/5">
        <h3 className="text-lg font-semibold mb-4">Long-term Memory</h3>
        <JsonViewer data={memory} />
      </div>
    </div>
  );
}

export default LogsPage;

