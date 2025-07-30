import React, { useState } from 'react';
import { sendMessage, forgetMemory } from '../api';
import Message from './Message';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const userId = 'user-123'; // Example userId, make dynamic as needed

  const handleSend = async () => {
    if (!input.trim()) return;

    setMessages((prev) => [...prev, { sender: 'user', text: input }]);

    let reply;
    if (input.toLowerCase().includes("don't") || input.toLowerCase().includes('forget')) {
      const res = await forgetMemory(userId, input);
      reply = res.deleted
        ? `I've forgotten "${res.keyword}".`
        : "I couldn't identify anything to forget.";
    } else {
      reply = await sendMessage(userId, input);
    }

    setMessages((prev) => [...prev, { sender: 'bot', text: reply }]);
    setInput('');
  };

  return (
    <div className="flex flex-col h-screen p-4 bg-gray-50">
      <div className="flex-1 overflow-auto flex flex-col">
        {messages.map((msg, idx) => (
          <Message key={idx} sender={msg.sender} text={msg.text} />
        ))}
      </div>

      <div className="flex">
        <input
          className="flex-1 border rounded p-2 mr-2"
          placeholder="Type a message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
        />
        <button
          className="bg-blue-500 text-white px-4 rounded"
          onClick={handleSend}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Chat;
