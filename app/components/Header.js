import React from 'react';
import { useSelector } from 'react-redux';

import './Header.css';

const Header = () => {

  const ticker = useSelector(state => state.ticker.value);
  
  return (
    <div>
      <h1 className="company-name">
        <span>Company Name</span>
        <span className="ticker-symbol"> ({ticker})</span>
      </h1>

    </div>
  );
}

export default Header;