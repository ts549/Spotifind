import React from 'react'

const login = () => {
  return (
    <div>login</div>
  )
}

export default login

import LoginButton from './LoginButton'
import { useHistory } from 'react-router-dom'

const Login = () => {
    const { push } = useHistory()


    const onClick = () => {
        push('/login')
    }

  
    return (
    <div>
        <h1 className="lrgtxt">
            Personalized art based on<br/>YOUR music taste
        </h1>
        <h2 className="medtxt">
            Generate art based on top albums, tracks, artists
        </h2>
        <LoginButton onClick = {onClick}/>
    </div>
  )
}

export default Login