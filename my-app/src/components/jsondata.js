import React from 'react'
import Records from './data.json'

const jsondata = () => {
  return (
    <div className='app'>
        <h1>web style press</h1>
        <br></br>

        {
            Records.map(record => {
                return (
                    <div className='box'>
                        {record.name}
                    </div>
                )
            } )
        }

    </div>
  )
}

export default jsondata
