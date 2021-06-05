import React from 'react';
import { useDispatch } from 'react-redux'
import { update } from '../tickerSlice';
import Header from './Header';

const App = () => {
  // get ticker symbol from url path
  const ticker = window.location.pathname.split('/')[2]
  const dispatch = useDispatch()
  dispatch(update(ticker))
  
  return (
    <div>
      <Header />
    </div>
  );
}

export default App;