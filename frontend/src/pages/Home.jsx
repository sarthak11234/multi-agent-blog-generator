import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { api } from "../services/api.js";
import { useRun } from "../context/RunContext.jsx";
import Loader from "../components/Loader.jsx";
import MetricTag from "../components/MetricTag.jsx";

function Home() {
  const [topic, setTopic] = useState("");
  const [goal, setGoal] = useState("Publish a helpful technical article.");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { currentRun, setCurrentRun } = useRun();

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!topic.trim()) {
      setError("Please provide a topic.");
      return;
    }
    setLoading(true);
    setError("");
    try {
      const result = await api.generate({ topic, goal });
      setCurrentRun(result);
      navigate("/trace");
    } catch (err) {
      setError(err?.response?.data?.detail || err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-10 relative z-10" style={{ minHeight: '80vh', position: 'relative' }}>
      <motion.section
        className="glass-card rounded-2xl p-10 shadow-2xl relative z-10"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
      >
        <h1 className="text-5xl font-bold mb-6 galaxy-title">
          Multi-Agent Blog Generation
        </h1>
        <p className="text-gray-400 text-lg mb-8">
          Harness the power of AI agents to create stellar content across the cosmos of knowledge.
        </p>
        <form className="space-y-6" onSubmit={handleSubmit}>
          <div>
            <label className="text-sm text-purple-300 block mb-2 font-medium">Topic</label>
            <input
              className="w-full modern-input rounded-xl text-lg"
              placeholder="e.g., Artificial Intelligence"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
            />
          </div>
          <div>
            <label className="text-sm text-purple-300 block mb-2 font-medium">
              Content Goal
            </label>
            <textarea
              className="w-full modern-input rounded-xl text-lg"
              rows="4"
              value={goal}
              onChange={(e) => setGoal(e.target.value)}
            />
          </div>
          {error && (
            <div className="error-message">
              {error}
            </div>
          )}
          <button
            type="submit"
            className="w-full modern-button rounded-xl text-lg py-4"
            disabled={loading}
          >
            {loading ? "🌟 Generating..." : "🚀 Generate Content"}
          </button>
        </form>
      </motion.section>

      {loading && <Loader label="🌌 Agents collaborating across the cosmos" />}

      {currentRun && !loading && (
        <section className="grid md:grid-cols-3 gap-4 relative z-10">
          <MetricTag label="Run ID" value={currentRun.run_id.slice(0, 8)} />
          <MetricTag label="Word Count" value={currentRun.evaluation.word_count} />
          <MetricTag label="Flesch Score" value={currentRun.evaluation.flesch_score} />
        </section>
      )}

      {/* Feature Information Blocks */}
      <section className="grid md:grid-cols-3 gap-6 mt-16 relative z-10">
        <motion.div
          className="glass-card rounded-xl p-6"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
        >
          <div className="text-4xl mb-4">🔬</div>
          <h3 className="text-xl font-bold text-purple-300 mb-3">Research Agent</h3>
          <p className="text-gray-400 text-sm leading-relaxed">
            Automatically gathers comprehensive information about your topic from multiple sources,
            analyzing key concepts and identifying the most relevant insights.
          </p>
        </motion.div>

        <motion.div
          className="glass-card rounded-xl p-6"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
        >
          <div className="text-4xl mb-4">✍️</div>
          <h3 className="text-xl font-bold text-purple-300 mb-3">Writer Agent</h3>
          <p className="text-gray-400 text-sm leading-relaxed">
            Crafts engaging, well-structured content based on research findings.
            Creates compelling narratives that resonate with your target audience.
          </p>
        </motion.div>

        <motion.div
          className="glass-card rounded-xl p-6"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
        >
          <div className="text-4xl mb-4">✨</div>
          <h3 className="text-xl font-bold text-purple-300 mb-3">Editor Agent</h3>
          <p className="text-gray-400 text-sm leading-relaxed">
            Polishes and refines the content for clarity, grammar, and SEO optimization.
            Ensures your final output is publication-ready and professional.
          </p>
        </motion.div>
      </section>

      {/* How It Works Section */}
      <motion.section
        className="glass-card rounded-xl p-8 mt-8 relative z-10"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
      >
        <h2 className="text-3xl font-bold gradient-text mb-6">How It Works</h2>
        <div className="grid md:grid-cols-2 gap-8">
          <div>
            <h4 className="text-lg font-semibold text-purple-300 mb-3">🎯 Multi-Agent Collaboration</h4>
            <p className="text-gray-400 text-sm leading-relaxed mb-4">
              Our system uses specialized AI agents that work together seamlessly. Each agent has a specific role -
              researching, writing, or editing - ensuring high-quality output through collaborative intelligence.
            </p>
          </div>
          <div>
            <h4 className="text-lg font-semibold text-purple-300 mb-3">🚀 Powered by Advanced AI</h4>
            <p className="text-gray-400 text-sm leading-relaxed mb-4">
              Built on cutting-edge language models, the system understands context, maintains consistency,
              and generates human-like content that meets professional standards.
            </p>
          </div>
          <div>
            <h4 className="text-lg font-semibold text-purple-300 mb-3">📊 Quality Metrics</h4>
            <p className="text-gray-400 text-sm leading-relaxed mb-4">
              Every generated piece is evaluated for readability, coherence, and SEO effectiveness.
              Track metrics like word count and Flesch reading score to ensure optimal content quality.
            </p>
          </div>
          <div>
            <h4 className="text-lg font-semibold text-purple-300 mb-3">💡 Use Cases</h4>
            <p className="text-gray-400 text-sm leading-relaxed mb-4">
              Perfect for blog posts, technical articles, educational content, marketing copy, and more.
              Save time while maintaining high editorial standards across all your content needs.
            </p>
          </div>
        </div>
      </motion.section>
    </div>
  );
}

export default Home;
