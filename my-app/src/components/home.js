import React from 'react'
import {Link} from 'react-router-dom'




function home() {
  return (
    <div>
      <h1>this is home page</h1>
      
      <Link to='/language'>languages</Link>
      <Link to='/washingmachine'>washing machine</Link>
      <Link to='/stories'>Mardi himal</Link>
      
    </div>
  )
}

export default home;
