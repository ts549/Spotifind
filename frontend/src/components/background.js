import React from 'react';
import Backdrop from './backdrop';
import Vinyl from './vinyl';

function Background() {
    return (
        <div className="fixed h-screen w-screen">
            <p className= "text-black absolute flex items-left text-left pl-[3%] pt-[2%] font-bold text-3xl">mood</p>
            
            <div className="relative w-screen h-screen content-center flex items-center z-10">
                <div className="relative ml-[46%] mt-[7.25%]">
                    <div className="pb-2">
                        <Vinyl />
                    </div>
                </div>

                {/* <div id="backdrop" className="absolute bottom-0 w-screen h-screen"> */}
                    <Backdrop className="relative z-0"/>
                {/* </div>   */}
            </div>
            
        </div>
    )
}

export default Background;