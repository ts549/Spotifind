import React from 'react';
import Backdrop from './backdrop';
import Vinyl from './vinyl';

function Background() {
    return (
        <div className="fixed h-screen w-screen">
            <p className= "text-black absolute flex items-left text-left pl-[3%] pt-[2%] font-bold text-3xl">mood</p>
            
            <div className="relative w-screen h-screen flex items-center justify-center z-10">
                <div className="relative top-[11.4%] left-32">
                    <div className="pb-2">
                        <Vinyl />
                    </div>
                </div>

                <div className="absolute bottom-0">
                    <Backdrop className="relative z-0"/>
                </div>  
            </div>
            
        </div>
    )
}

export default Background;