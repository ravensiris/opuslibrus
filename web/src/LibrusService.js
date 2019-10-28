const axios = require("axios").default;

axios.defaults.baseURL = "/api";

export class LibrusService {
  getToken(username, password) {
    const auth =
      "Basic " + Buffer.from(`${username}:${password}`).toString("base64");
    return axios.get("/token/get", {
      headers: { Authorization: auth }
    });
  }

  getTimetable(token, timestamp = "") {
    if (timestamp) {
      timestamp = `/${timestamp}`;
    }
    return axios.get(`/timetable/get${timestamp}`, {
      headers: { "X-API-KEY": token }
    });
  }

  checkToken(token) {
    if (!token) {
      return false;
    }
    return axios.get("/token/check", {
      headers: { "X-API-KEY": token }
    });
  }
}
