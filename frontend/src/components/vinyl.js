import React, { useState } from 'react'
const Vinyl = () => {
  const [currentSong, setCurrentSong] = useState("");
  const [nextSong, setNextSong] = useState("");
  const [previousSong, setPreviousSong] = useState("");

  componentDidMount => () => {
    getCurrentSong();
    getNextSong();
    getPreviousSong();
  }

  const getCurrentSong = () => {
    axios.post('../localhost8000:INSERTLINKHERE')
    .then(function() {
      setCurrentSong(res.data);
    })
    .catch(function(error) {
        console.log(error);
    })
  }

  const getPreviousSong = () => {
    axios.post('../localhost8000:INSERTLINKHERE')
    .then(function() {
      setPreviousSong(res.data);
    })
    .catch(function(error) {
        console.log(error);
    })
  }

  const getNextSong = () => {
    axios.post('../localhost8000:INSERTLINKHERE')
    .then(function() {
      setNextSong(res.data);
    })
    .catch(function(error) {
        console.log(error);
    })
  }

  return (
    <div> 
      <div class="flex justify-center items-center">
        <div class="bg-black w-96 h-96 rounded-full relative z-0"> 
          <p class="text-gray-300 flex justify-center items-center pl-24 pt-36 rotate-[315deg]">{previousSong.length > 0 ? setPreviousSong : "previous song"}</p>
          <p class="text-white flex justify-center items-center pl-60 pt-3">{currentSong.length > 0 ? currentSong : "current song"}</p>
          <p class="text-gray-300 flex justify-center items-center pl-40 pb-12 rotate-[42deg]">{nextSong.length > 0 ? nextSong : "next song"} </p>
          <div class="absolute inset-0 flex justify-center items-center z-20">
            <div class="bg-white w-28 h-28 rounded-full relative z-30"> 
              <div class="absolute inset-0 flex justify-center items-center z-40">
                <div class="bg-black w-4 h-4 rounded-full relative z-0"/>  
                  
              </div>
            </div>
          
          </div>
        </div> 
      </div>
    </div>

  )
}

export default Vinyl 
