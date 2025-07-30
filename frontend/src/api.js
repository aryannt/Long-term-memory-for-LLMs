import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_BACKEND_URL,
});

export const sendMessage = async (userId, message) => {
  const res = await api.post('/message', { userId, message });
  return res.data.reply;
};

export const forgetMemory = async (userId, message) => {
  const res = await api.post('/forget', { userId, message });
  return res.data;
};
