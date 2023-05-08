import React from 'react'
import mardi from './components/mardi'



function home() {
  return (
    <div>
      <h1>this is home page</h1>
      <button onClick={mardi}>
        Click me!
      </button>
    </div>
  )
}

export default home
