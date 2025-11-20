import axios from "axios";

// Hardcoded to ensure connection works
const API_BASE = "http://127.0.0.1:8000";

export const api = {
  async generate(payload) {
    const { data } = await axios.post(`${API_BASE}/generate`, payload);
    return data;
  },
  async fetchLogs(limit = 40) {
    const { data } = await axios.get(`${API_BASE}/logs`, { params: { limit } });
    return data.logs;
  },
  async fetchMemory() {
    const { data } = await axios.get(`${API_BASE}/memory`);
    return data.memory;
  },
};

