import axios from "axios";

const request = axios.create({
  baseURL: "/api",
  timeout: 600000,
});

export const selectChart1Api=()=>{
    return request.get("/chart1")
}

export const selectChart2Api=()=>{
    return request.get("/chart2")
}

export const selectChart3Api=()=>{
    return request.get("/chart3")
}

export default request;