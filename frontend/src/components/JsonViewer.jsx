function JsonViewer({ data }) {
  return (
    <pre className="bg-slate-900/70 rounded-xl p-4 text-xs text-white/80 overflow-auto border border-white/5">
      {JSON.stringify(data, null, 2)}
    </pre>
  );
}

export default JsonViewer;

