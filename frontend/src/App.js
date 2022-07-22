import axios from 'axios';
import logo from './logo.svg';
import './App.css';

function App() {

  const axios = require('axios').default;

  const url = '/test';

  axios.get(url)
    .then(response => {
      console.log(response)
    });
    

  return <p> hi</p>
}

export default App;