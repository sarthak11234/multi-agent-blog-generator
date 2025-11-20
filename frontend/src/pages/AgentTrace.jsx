import { useMemo } from "react";
import AgentStepCard from "../components/AgentStepCard.jsx";
import MetricTag from "../components/MetricTag.jsx";
import JsonViewer from "../components/JsonViewer.jsx";
import { useRun } from "../context/RunContext.jsx";
import { Link } from "react-router-dom";

function AgentTrace() {
  const { currentRun } = useRun();
  const steps = currentRun?.steps;

  const seoReport = useMemo(() => steps?.editor?.seo_report ?? null, [steps]);

  if (!currentRun) {
    return (
      <div className="bg-slate-900/60 rounded-3xl p-10 text-center border border-white/5">
        <p className="text-white/70 mb-4">No run data yet.</p>
        <Link className="text-brand-400 underline" to="/">
          Start a run from the Home page.
        </Link>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      <div className="flex flex-wrap gap-4">
        <MetricTag label="Topic" value={currentRun.topic} />
        <MetricTag label="Goal" value={currentRun.goal} />
        <MetricTag label="Run ID" value={currentRun.run_id.slice(0, 8)} />
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        <AgentStepCard
          title="Researcher Agent"
          content={steps.researcher.summary}
          meta="Search & Synthesis"
        />
        <JsonViewer data={steps.researcher.sources} />
        <AgentStepCard
          title="Writer Agent"
          content={steps.writer.draft}
          meta="Drafting"
        />
        <AgentStepCard
          title="Editor Agent"
          content={steps.editor.final_content}
          meta="Editing & SEO"
        />
      </div>

      {seoReport && (
        <div className="bg-slate-900/60 rounded-3xl p-6 border border-white/5">
          <h3 className="text-lg font-semibold mb-2">SEO Analyzer</h3>
          <p className="text-white/80 whitespace-pre-line text-sm">
            {seoReport.suggestions}
          </p>
        </div>
      )}
    </div>
  );
}

export default AgentTrace;

