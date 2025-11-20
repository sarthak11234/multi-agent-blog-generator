import { motion } from "framer-motion";

function AgentStepCard({ title, content, meta }) {
  return (
    <motion.div
      layout
      className="bg-slate-900/60 rounded-2xl p-6 border border-white/5 shadow-xl"
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
    >
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold">{title}</h3>
        {meta && (
          <span className="text-xs uppercase tracking-wide text-white/60 bg-white/5 px-2 py-1 rounded-full">
            {meta}
          </span>
        )}
      </div>
      <p className="text-white/80 whitespace-pre-line leading-relaxed text-sm">
        {content}
      </p>
    </motion.div>
  );
}

export default AgentStepCard;

