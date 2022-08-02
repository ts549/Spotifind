import axios from 'axios';
import './App.css';
import PlayButton from './components/PlayButton';
import Title from './components/Title';
import Searchbar from './components/Searchbar';

function App() {

  const axios = require('axios').default;

  const url = '/test';

  axios.get(url)
    .then(response => {
      console.log(response)
    });
    
  return <div class="header">
    <Title/>
    <Searchbar/>
    <div class="header">
      <img id="spotify-logo" src="../icons/spotify-logo.png" alt="Error IMG"></img>
      <h1 class="h1">SPOTIFIND</h1>
      <img id="menu" src="../icons/menu.png" alt="Error IMG"></img>
    </div>

    <div>
      <img id="audio-gif" src="../icons/audio.gif" alt="Error GIF"></img>
      <PlayButton id="PlayButton" />
    </div>
  </div>
}

export default App;