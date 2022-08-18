import React, { useState, useEffect } from 'react'
import axios from "axios";

const Vinyl = () => {
  const [top3Songs, setTop3Songs] = useState([]);
  const [text, setText] = useState("");
  const [mood, setMood] = useState("");

  const onClick = () => {
    console.log("IN onClick ");
    getTop3Songs();
  };

  const getTop3Songs = () => {
    axios({
      method: 'post',
      url: 'http://localhost:3000/api/start_record',
      data: {
        "time": "5"
      }
    })
    .then(function(res) {
      console.log("in front end")
      setTop3Songs(res['data']['top 3 songs'])
      setText(res['data']['text'])
      setMood(res['data']['mood'])
    })
    .catch(function(error) {
        console.log(error);
    })
  }



  return (
    <div>
      <div class="bg-black w-96 h-96 rounded-full"> 
        <p class="text-white flex justify-center items-center pl-24 pt-36 rotate-[315deg]">
          {top3Songs[0] ? (top3Songs[0].length > 12 ? top3Songs[0].substring(0, 12) + "..." : top3Songs[0]) : ""}
        </p>
        <p class="text-white flex justify-center items-center pl-60 pt-3">
          {top3Songs[1] ? (top3Songs[1].length > 12 ? top3Songs[1].substring(0, 12) + "..." : top3Songs[1]) : ""}
        </p>
        <p class="text-white flex justify-center items-center pl-40 pb-12 rotate-[42deg]">
          {top3Songs[2] ? (top3Songs[2].length > 9 ? top3Songs[2].substring(0, 9) + "..." : top3Songs[2]) : ""}
        </p>
        <div class="absolute inset-0 flex justify-center items-center">
          <div class="bg-white w-28 h-28 rounded-full relative"> 
            <div class="absolute inset-0 flex justify-center items-center">
              <div class="bg-black w-4 h-4 rounded-full relative"/>  
            </div>
          </div>
        </div>
      </div> 

      
      <h1 class="z-30">{mood ? mood : "mood"}</h1>
      <h1 class="z-30">{text ? text : "text"}</h1>


      <button onClick={() => onClick()} class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"> record</button>
    
    </div>
    



  )
}

export default Vinyl 
