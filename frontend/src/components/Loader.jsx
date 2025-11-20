import { motion } from "framer-motion";

function Loader({ label = "Thinking" }) {
  return (
    <div className="flex flex-col items-center gap-3 py-10 text-white/70">
      <motion.div
        animate={{ rotate: 360 }}
        transition={{ duration: 1.2, repeat: Infinity, ease: "linear" }}
        className="w-10 h-10 border-2 border-brand-500 border-t-transparent rounded-full"
      />
      <p className="text-sm tracking-wide uppercase">{label}</p>
    </div>
  );
}

export default Loader;

