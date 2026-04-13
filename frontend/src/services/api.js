import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const fetchStats = () => API.get("/stats");
export const fetchProcesses = () => API.get("/processes");

export const killProcess = (pid) => {
  return API.post(`/process/kill/${pid}`);
};