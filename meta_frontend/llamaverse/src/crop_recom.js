
import React, { useState } from 'react';
import { getcropRecomend,convertHindi } from './api';
import { SiConvertio } from "react-icons/si";
import ClipLoader from 'react-spinners/ClipLoader';
const Recom = () => {
    const [file,setfile]=useState(null)
    const [response,setResponse]=useState("")
    const [location,setLocation]=useState("")
    const [month,setMonth]=useState("")
    const [loader,setloader] =useState(false)
    const [hloader,sethloader] =useState(false)

  return (
    <div className="flex flex-col w-[80%] m-auto mt-[2.5%] h-[80%] p-4 border rounded-lg shadow-lg bg-white">
       <div className='overflow-scroll'>
      <div className="h-64">
    {file&&<div  className=" text-white my-4 py-2 px-4 rounded-2xl bg-blue-500  max-w-[40%] self-start ">
       {location&&<span class=" text-white dark:text-gray-400">Location: {location}</span>}
       <br></br>
       {location&&<span class=" text-white dark:text-gray-400">Month: {month}</span>}
       <br></br>
       Soil Image:
        <img className="ml-4 my-4 h-64 w-64" src={URL.createObjectURL(file)}></img>
          </div>}
      </div>
      <div className="mt-8 h-64">
      {response!=""&&<div  className=" my-4 py-2 px-4 rounded-2xl bg-gray-200  max-w-[50%] self-start  ml-[50%]">
        {!hloader&&<SiConvertio className='ml-[98%] cursor-pointer' onClick={()=>{sethloader(true);convertHindi(response).then((action)=>{setResponse(action)});sethloader(false)}}></SiConvertio>
       }   {response.split('\n').map((line, index) => (
    <div key={index}>{line}</div>
  ))}
           {/* <textarea value={response}></textarea> */}
          </div>}
</div>
</div>
<div class="flex items-center justify-center w-full">
    <label for="dropzone-file" class="flex flex-col items-center justify-center w-full h-28 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
        <div class="flex flex-col items-center justify-center pt-5 pb-6">
            <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
            </svg>
            <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
            <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
            {file&&<span class="text-xs text-gray-500 dark:text-gray-400">{file.name}</span>}
        </div>
        <input id="dropzone-file" type="file" class="hidden" onChange={(e)=>{setfile(e.target.files[0]);setResponse("")}} />
    </label>
    <div className='ml-2 flex-col'>
    <input type="text" value={location} onChange={(e)=>{setLocation(e.target.value)}} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="location" required />
    <input type="text" value={month} onChange={(e)=>{setMonth(e.target.value)}} class="mt-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="month" required />
       
    </div>
    {!loader?<button type="submit" className="ml-2 p-2 text-white bg-blue-600 rounded-lg hover:bg-blue-700"
    onClick={()=>{setResponse("");setloader(true);getcropRecomend(file,location,month).then((action)=>{setResponse(action);setloader(false);})}}
    >
          Send
        </button>:<ClipLoader></ClipLoader>}
</div> 

    </div>
  );
};

export default Recom;
