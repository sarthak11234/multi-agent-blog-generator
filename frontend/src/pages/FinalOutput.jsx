import { useRun } from "../context/RunContext.jsx";
import { Link } from "react-router-dom";
import JsonViewer from "../components/JsonViewer.jsx";

function FinalOutput() {
  const { currentRun } = useRun();

  if (!currentRun) {
    return (
      <div className="bg-slate-900/60 rounded-3xl p-10 text-center border border-white/5">
        <p className="text-white/70 mb-4">No final output available yet.</p>
        <Link className="text-brand-400 underline" to="/">
          Trigger a generation first.
        </Link>
      </div>
    );
  }

  const finalContent = currentRun.steps.editor.final_content;

  return (
    <div className="space-y-8">
      <div className="bg-slate-900/60 rounded-3xl p-8 border border-white/5">
        <div className="flex items-center justify-between mb-4">
          <div>
            <p className="text-sm text-white/60 uppercase tracking-wide">
              Topic
            </p>
            <h2 className="text-2xl font-semibold">{currentRun.topic}</h2>
          </div>
          <button
            onClick={() => navigator.clipboard.writeText(finalContent)}
            className="px-4 py-2 rounded-xl border border-white/10 hover:bg-white/5 text-sm"
          >
            Copy
          </button>
        </div>
        <article className="space-y-4 text-white/80 leading-relaxed">
          {finalContent.split("\n\n").map((para, idx) => (
            <p key={idx}>
              {para}
            </p>
          ))}
        </article>
      </div>

      <div className="bg-slate-900/60 rounded-3xl p-6 border border-white/5">
        <h3 className="text-lg font-semibold mb-2">Evaluation</h3>
        <JsonViewer data={currentRun.evaluation} />
      </div>
    </div>
  );
}

export default FinalOutput;

