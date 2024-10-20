import React, { useState } from 'react';
import { CgProfile } from "react-icons/cg";
import {getQueryResponse} from "./api.js"
import { FaRobot } from "react-icons/fa6";
import ClipLoader from "react-spinners/ClipLoader";
const Chatbot = () => {
  const [messages, setMessages] = useState([{"text":"Hello How Can I assist you"}]);
  const [input, setInput] = useState('');
  const [loader,setloader] =useState(false)

  const handleSend = (e) => {
    e.preventDefault();
    if (input.trim() === '') return;
    setloader(true)
    // Add user message
    const userMessage = { text: input, sender: 'user' };
    setMessages((prev) => [...prev, userMessage]);

    // Simulate bot response
    getQueryResponse(input).then((action)=>{
        setMessages((prev) => [...prev,{ text: action, sender: 'bot' } ])
        setloader(false)
    })
    

    setInput('');
  };

  return (
    <div className="flex flex-col w-[80%] m-auto mt-[2.5%] h-[80%] p-4 border rounded-lg shadow-lg bg-white">
      <div className="flex-1 overflow-y-auto p-2">
        {messages.map((msg, index) => (
          <div key={index} className={` my-4 py-2 px-4 rounded-2xl ${msg.sender !== 'user' ? 'bg-gray-200  max-w-[40%]' : 'bg-blue-500 text-white self-start max-w-[40%] ml-[60%]'}`}>
           {msg.sender === 'user'?<div className="flex"><CgProfile size={25}></CgProfile><span className='ml-2'>Farmer</span></div>:<div className="flex"><FaRobot size={25}></FaRobot><span className='ml-2'>Bot</span></div>}
            {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={handleSend} className="flex mt-4">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
          className="flex-1 p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        {loader?<ClipLoader></ClipLoader>:<button type="submit" className="ml-2 p-2 text-white bg-blue-600 rounded-lg hover:bg-blue-700">
          Send
        </button>}
      </form>
    </div>
  );
};

export default Chatbot;
