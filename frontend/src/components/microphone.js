import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {faMicrophone} from '@fortawesome/free-solid-svg-icons';

const Microphone = () => {
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
    <div class="flex w-screen h-screen relative justify-center items-center">
        <button onClick={() => onClick()} class=""> <FontAwesomeIcon icon={faMicrophone} className="text-9xl fill-current align-middle hover:text-blue-400 "/></button>
    </div>

    )
}

export default Microphone



