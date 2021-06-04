import React from 'react';
import ReactDOM from 'react-dom';

const ticker = window.location.pathname.split('/')[2]

const App = () => {
  return (
    <h1>{ticker}</h1>
  );
}

export default App;