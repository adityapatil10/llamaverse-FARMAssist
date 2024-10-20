import logo from './logo.svg';
import './App.css';
import Navbar from './navbar';
import Chatbot from './chatbot';
import Recom from './crop_recom';
import Detect from './disease_detect';
import { useState } from 'react';
function App() {
  const [tab,settab]=useState(0)
  return (
    <div className="w-[100vw] h-[100vh]">
      <Navbar tab={tab} settab={settab}></Navbar>
      {tab===0&&<Chatbot className="w-[80%] h-[80%]"></Chatbot>}
      {tab===1&&<Recom className="w-[80%] h-[80%]"></Recom>}
      {tab===2&&<Detect className="w-[80%] h-[80%]"></Detect>}
    </div>
  );
}

export default App;
