import React, { useState, useEffect } from 'react'
import axios from "axios";
import './vinyl.css';

const Vinyl = () => {
  const [top3Songs, setTop3Songs] = useState([]);
  const [currentSong, setCurrentSong] = useState("") 
  const [previousSong, setPreviousSong] = useState("") 
  const [nextSong, setNextSong] = useState("") 
  

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
    
    })
    .catch(function(error) {
        console.log(error);
    })
  }



  return (
    <div class>
      <div className="bg-black circle rounded-full"> 
        <p class="text-white flex justify-center items-center pl-24 pt-36 rotate-[315deg]">
          {top3Songs[0] ? (top3Songs[0].length > 12 ? top3Songs[0].substring(0, 12) + "..." : top3Songs[0]) : ""}
        </p>
        <p className="text-white flex justify-center items-center pl-60 pt-3">
          {top3Songs[1] ? (top3Songs[1].length > 12 ? top3Songs[1].substring(0, 12) + "..." : top3Songs[1]) : ""}
        </p>
        <p className="text-white flex justify-center items-center pl-40 pb-12 rotate-[42deg]">
          {top3Songs[2] ? (top3Songs[2].length > 9 ? top3Songs[2].substring(0, 9) + "..." : top3Songs[2]) : ""}
        </p>
        <div className="absolute inset-0 flex justify-center items-center">
          <div className="bg-white small_circle rounded-full relative"> 
            <div className="absolute inset-0 flex justify-center items-center">
              <div className="bg-black dot rounded-full relative"/>  
            </div>
          </div>
        </div>
      </div> 

      <button onClick={() => onClick()} className="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"> record</button>
    
    </div>
    



  )
}

export default Vinyl 
