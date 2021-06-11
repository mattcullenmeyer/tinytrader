import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchTickerdata } from '../reducers/tickerdataSlice';
import { fetchMetadata } from '../reducers/metadataSlice';
import './Header.css';


const Header = () => {
  
  const ticker = window.location.pathname.split('/')[2]

  const dispatch = useDispatch()

  const tickerdata = useSelector(state => state.tickerdata.data); 
  const tickerStatus = useSelector(state => state.tickerdata.status);

  const metadata = useSelector(state => state.metadata.data);
  const metaStatus = useSelector(state => state.metadata.status);
  
  useEffect(() => {
    if (tickerStatus === 'idle') {
      dispatch(fetchTickerdata(ticker));
    }
      
    if (tickerStatus === 'success') {
      dispatch(fetchMetadata(tickerdata.id));
    }
  }, [tickerStatus, dispatch]);

  const formattedDate = () => {
    const date = new Date(metadata.last_updated);
    const date_formatted = date.toLocaleString('default', { month: 'short', day: 'numeric', year: 'numeric' });
    return date_formatted;
  }

  const header = () => {
    if (metaStatus === 'success') {
      return (
        <div>
          <h1 className="company-name">
            <span>{metadata.company_name}</span>
            <span className="ticker-symbol"> ({tickerdata.ticker})</span>
          </h1>
          <div className="timestamp">Market close {formattedDate()}</div>
        </div>
      );
    }
    return;
  }

  return (
    <div>
      {header()}
    </div>
  );
}

export default Header;