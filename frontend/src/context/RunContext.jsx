import { createContext, useContext, useState } from "react";

const RunContext = createContext();

export function RunProvider({ children }) {
  const [currentRun, setCurrentRun] = useState(null);
  return (
    <RunContext.Provider value={{ currentRun, setCurrentRun }}>
      {children}
    </RunContext.Provider>
  );
}

export function useRun() {
  const ctx = useContext(RunContext);
  if (!ctx) throw new Error("useRun must be used inside RunProvider");
  return ctx;
}

