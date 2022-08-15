import './App.css';
import Vinyl from './components/vinyl';
import Square from './components/square'

function App() {
  <head>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap" rel="stylesheet"/>
  </head>

  return (
    <div>
      <div class="relative w-screen h-screen flex items-center justify-center">
        <div class="relative ">
          <div class="pb-2"> 
            <Vinyl/>
          </div>
          <div class="absolute right-44 bottom-0"> 
            <Square/>
          </div>
        </div>
      </div>
    </div>

    
  
  );
}

export default App;

