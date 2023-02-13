import axios from 'axios'
import React from 'react'

function ConversionItem(props) {
    const deleteConversionHandler = (Coin) => {
    axios.delete(`http://210.246.19.166:8000/api/conversion/${Coin}`)
        .then(res => console.log(res.data)) }
  
    return (
        <div>
            <p>
                <span style={{ fontWeight: 'bold, underline' }}>{props.todo.Amount} = </span> ${props.todo.Price} : {props.todo.Coin}
                <button onClick={() => deleteConversionHandler(props.todo.Coin)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default ConversionItem;