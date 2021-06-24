import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchTickerdata } from '../reducers/tickerdataSlice';
import { fetchMetadata } from '../reducers/metadataSlice';
import { fetchMetricData } from '../reducers/metricSlice';
import Header from './Header';
import Block from './Block';
import Menu from './Menu';
import Card from './Card';
import RankCircle from './RankCircle';
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
        <Card title="Overall" size="small" location="left">
          <RankCircle rank={metadata.composite_rank} />
        </Card>
      </Block>
      
      

    </div>
  );
}

export default App;