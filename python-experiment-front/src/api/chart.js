import axios from "axios";

const request = axios.create({
  baseURL: "/api",
  timeout: 600000,
  headers: {
    "Content-Type": "application/json",
  },
});

export const createLineChartApi = (data) => {
  return request.post("/lineChart", data);
};

export const createPieChartApi = (data) => {
  return request.post("/pieChart", data);
};

export const createBarChartApi = (data) => {
  return request.post("/barChart", data);
};

export default request;
