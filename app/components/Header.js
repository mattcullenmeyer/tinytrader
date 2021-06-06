import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchTicker } from '../tickerSlice';
import { fetchMetadata } from '../metadataSlice';
import './Header.css';



const Header = () => {
  
  const dispatch = useDispatch()
  const ticker = useSelector(state => state.ticker.data.ticker); //state.ticker.company_name_ticker);
  //const company_name = useSelector(state => state.ticker.data.company_name);

  const company_name = useSelector(state => state.metadata.data.company_name);
  
  useEffect(() => {
    dispatch(fetchTicker());
    dispatch(fetchMetadata());
  }, []);

  return (
    <div>
      <h1 className="company-name">
        <span>{company_name}</span>
        <span className="ticker-symbol"> ({ticker})</span>
      </h1>

    </div>
  );
}

export default Header;