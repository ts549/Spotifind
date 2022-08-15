import React from 'react';
import Backdrop from './backdrop';

function Background() {
    return (
        <div className="fixed h-screen w-screen">
            <p className= "text-black absolute flex items-left text-left pl-[3%] pt-[2%] font-bold text-3xl">mood</p>
            <div>
                <Backdrop className="relative"/>
            </div>
            {/* <div>
                <p className="absolute">mood</p>
                <Backdrop className="absolute"/>
            </div> */}
        </div>
    )
}

export default Background;