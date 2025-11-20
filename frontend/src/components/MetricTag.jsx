function MetricTag({ label, value }) {
  return (
    <div className="bg-white/5 border border-white/10 rounded-xl px-4 py-2 text-center">
      <div className="text-xs uppercase text-white/60 tracking-wide">
        {label}
      </div>
      <div className="text-lg font-semibold text-white">{value ?? "—"}</div>
    </div>
  );
}

export default MetricTag;

