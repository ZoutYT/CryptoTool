import React, { useState, useEffect} from 'react';
import './App.css';
import TodoView from './components/CoversionsView';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'; 


function App() {

  const [todoList, setTodoList] = useState([{}])
  const [addy, setAddy] = useState('')
  const [erc, setERC] = useState('')
  const [coin, setCoin] = useState('')

    

  useEffect(() => {
    axios.get('http://210.246.19.166:8000/api/conversion')
      .then(res => {
        setTodoList(res.data)
      })
    });

  // Post a todo
  const addTodoHandler = () => {
    axios.post('http://210.246.19.166:8000/api/conversion/', {'Address': addy, 'Chain' : erc, 'Coin' : coin})
      .then(res => console.log(res))
  };
  return (
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}} >
      <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">Crypto Converter</h1>
     <div className="card-body">
      <span className="card-text"> 
        <select className="mb-2 form-control titleIn" id ="source" name="source" onClick={event => setERC(event.target.value)}>
          <option value="ERC20">ERC20</option>
          <option value="BTC">BTC</option>
          <option value="Polkadot">Polkadot</option>
        </select>
        <div>
          {erc === 'ERC20' &&(
            <select className="mb-2 form-control titleIn" onClick={event => setCoin(event.target.value)}>
            <option value="Eth">Ethereum</option>
          </select>
          )}
        </div>
        <div>
          {erc === 'BTC' &&(
            <select className="mb-2 form-control titleIn" onClick={event => setCoin(event.target.value)}>
            <option value="Bitcoin">Bitcoin</option>
          </select>
          )}
        </div>
        <div>
          {erc === 'Polkadot' &&(
            <select className="mb-2 form-control titleIn" onClick={event => setCoin(event.target.value)}>
            <option value="Polkadot">Polkadot</option>
            <option value="Moonbeam">Moonbeam</option>
          </select>
          )}
        </div>
        <input className="mb-2 form-control desIn" onChange={event => setAddy(event.target.value)}   placeholder='Address'/>
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}}  onClick={addTodoHandler}>Convert</button>
      </span>
      <h5 className="card text-white bg-dark mb-3">Your Conversions</h5>
      <div >
      <TodoView todoList={todoList} />
      </div>
      </div>
    </div>
  );
}

export default App;


