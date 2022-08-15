import React, { useState } from 'react';

function Backdrop() {

  const [changed, setChanged] = useState(false);

  function clicked() {
    if (!changed) {
      setChanged(true);
    }
  }

  return (
    <div className={"bg-light_red relative duration-500 " + (changed ? "w-96 h-96 mx-auto my-[9%]" : "w-screen h-screen")}>
        <div className={"text-white text-left pl-[3%] pt-[2%] text-3xl absolute z-10 duration-500" + (changed ? "text-3xl" : "text-xl")}> 
            mood
        </div>

        <div class="justify-center items-center flex absolute z-0 inset-0">
            <button className={"text-white duration-500 " + (changed ? "text-xl" : "text-2xl")} onClick={clicked}>Click Me</button>
        </div>
      </div>
  )
}

export default Backdrop