import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {faMicrophone} from '@fortawesome/free-solid-svg-icons';

const Microphone = () => {
  const onClick = () => {

    console.log("IN onClick ");
  };

  return (
    <div class="flex w-screen h-screen relative justify-center items-center">
      <button onClick={() => onClick()} class=""> <FontAwesomeIcon icon={faMicrophone} className="text-9xl fill-current align-middle hover:text-blue-400 "/></button>

      
    </div>
    
  )
}

export default Microphone