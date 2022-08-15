import './App.css';
import Backdrop from './components/backdrop'
import Vinyl from './components/vinyl';
import Spinner from './components/spinner/spinner';
import Square from './components/square'

import Wheel from './components/wheel';
function App() {
  <head>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap" rel="stylesheet"/>
  </head>
  return (
    <div className = "flex justify-center items-center relative">
      <div className="absolute">
        <Vinyl/>
      </div>
      <div className="absolute right-[0px]">
        <Square/>
      </div>
      
    </div>
    
  
  );
}

export default App;

