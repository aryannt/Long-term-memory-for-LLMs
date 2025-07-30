import React from 'react';

const Message = ({ text, sender }) => (
  <div
    className={`${
      sender === 'user' ? 'bg-blue-100 self-end' : 'bg-gray-100 self-start'
    } rounded-xl px-4 py-2 m-2 max-w-xs shadow`}
  >
    {text}
  </div>
);

export default Message;
