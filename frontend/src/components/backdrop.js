import React, { useState } from 'react';
import './backdrop.css';

function Backdrop() {

  const [changed, setChanged] = useState(false);

  function clicked() {
    if (!changed) {
      setChanged(true);
    }
  }

  return (
    <div className={"absolute bg-light_red base " + (changed ? "shrunk" : "fullscreen")}>
        <div className={"text-white text-left pl-[3%] pt-[2%] text-3xl absolute z-10 duration-1000 font-medium " + (changed ? "text-xl" : "text-3xl")}> 
            mood
        </div>

        <div class="justify-center items-center flex absolute z-0 inset-0 duration-1000">
            <button className={"text-white duration-1000 " + (changed ? "text-xl" : "text-2xl")} onClick={clicked}>Click Me</button>
        </div>
      </div>
  )
}

export default Backdrop;