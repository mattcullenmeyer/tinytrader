import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
// Reducers
import { fetchTickerdata } from '../reducers/tickerdataSlice';
import { fetchMetadata } from '../reducers/metadataSlice';
import { fetchMetricData } from '../reducers/metricSlice';
// Components
import Header from './Header';
import Block from './Block';
import Menu from './Menu';
import Overview from './Overview'; 
// Other
import { menus } from './menuList';


const App = () => {
  const [selectedMenu, setSelectedMenu] = useState(menus[0]);

  const ticker = window.location.pathname.split('/')[2]

  const dispatch = useDispatch()

  const tickerdata = useSelector(state => state.tickerdata.data); 
  const tickerStatus = useSelector(state => state.tickerdata.status);

  const metadata = useSelector(state => state.metadata.data);
  
  useEffect(() => {
    if (tickerStatus === 'idle') {
      dispatch(fetchTickerdata(ticker));
    }
      
    if (tickerStatus === 'success') {
      dispatch(fetchMetadata(tickerdata.id));
      dispatch(fetchMetricData(tickerdata.id));
    }
  }, [tickerStatus, dispatch]);

  const renderPage = () => {
    switch(selectedMenu.name) {
      case 'Overview':
        return <Overview metadata={metadata} />;
      case 'Valuation':
        return <div>Valuation</div>;
      case 'Momentum':
        return <div>Momentum</div>;
      case 'Quality':
        return <div>Quality</div>;
      default:
        return <Overview metadata={metadata} />
    }
  }

  return (
    <div>
      <Header />

      <Block>
        <Menu 
          menus={menus} 
          selectedMenu={selectedMenu} 
          onMenuSelect={setSelectedMenu} 
        />
      </Block>
      
      <Block>
        {renderPage()}
      </Block>
      
      

    </div>
  );
}

export default App;