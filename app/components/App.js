import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
// Reducers
import { fetchTickerdata } from '../reducers/tickerdataSlice';
import { fetchMetadata } from '../reducers/metadataSlice';
import { fetchMetricData } from '../reducers/metricSlice';
// Components
import Header from './Header';
import Card from './Card';
import CardTitle from './CardTitle';
import RankCircle from './RankCircle';
import Table from './Table';
// import Block from './Block';
// import Menu from './Menu';
// import Overview from './Overview'; 
// Other
// import { menus } from './menuList';
import './App.css';



const App = () => {
  // const [selectedMenu, setSelectedMenu] = useState(menus[0]);

  const ticker = window.location.pathname.split('/')[2]

  const dispatch = useDispatch()

  const tickerdata = useSelector(state => state.tickerdata.data); 
  const tickerStatus = useSelector(state => state.tickerdata.status);

  const metadata = useSelector(state => state.metadata.data);
  const metadataStatus = useSelector(state => state.metadata.status);

  const metric = useSelector(state => state.metric.data);
  
  useEffect(() => {
    if (tickerStatus === 'idle') {
      dispatch(fetchTickerdata(ticker));
    }
      
    if (tickerStatus === 'success') {
      dispatch(fetchMetadata(tickerdata.id));
      dispatch(fetchMetricData(tickerdata.id));
    }
  }, [tickerStatus, dispatch]);

  // const renderPage = () => {
  //   switch(selectedMenu.name) {
  //     case 'Overview':
  //       return <Overview metadata={metadata} />;
  //     case 'Valuation':
  //       return <div>Valuation</div>;
  //     case 'Momentum':
  //       return <div>Momentum</div>;
  //     case 'Quality':
  //       return <div>Quality</div>;
  //     default:
  //       return <Overview metadata={metadata} />
  //   }
  // }

//   return (
//     <div>
//       <Header />

//       <Block>
//         <Menu 
//           menus={menus} 
//           selectedMenu={selectedMenu} 
//           onMenuSelect={setSelectedMenu} 
//         />
//       </Block>
      
//       <Block>
//         {metadataStatus === 'success' && renderPage()}
//       </Block>
      
//      

//     </div>
//   );
// }

  return (
    <>
      <Header />

      <h2>Composite Ranks</h2>

      <Card size="small" location="left">
        <CardTitle title="Overview" /> 
        <RankCircle rank={metadata.composite_rank} />
      </Card>
      <Card size="small" location="middleLeft">
        <CardTitle title="Valuation" /> 
        <RankCircle rank={metadata.value_rank} />
      </Card>
      <Card size="small" location="middleRight">
        <CardTitle title="Momentum" /> 
        <RankCircle rank={metadata.mom_rank} />
      </Card>
      <Card size="small" location="right">
        <CardTitle title="Quality" /> 
        <RankCircle rank={metadata.quality_rank} />
      </Card>

      <h2>Quality Ranks</h2>

      <Card size="small" location="left">
        <CardTitle title="Volatility" /> 
        <RankCircle rank={metadata.vol_rank} />
      </Card>
      <Card size="small" location="middleLeft">
        <CardTitle title="Profitability" /> 
        <RankCircle rank={metadata.profit_rank} />
      </Card>
      <Card size="small" location="middleRight">
        <CardTitle title="Financing" /> 
        <RankCircle rank={metadata.finance_rank} />
      </Card>
      <Card size="small" location="right">
        <CardTitle title="Safety" /> 
        <RankCircle rank={metadata.safety_rank} />
      </Card>

      <h2>Individual Ranks</h2>

      <Card size="large" location="left">
        <CardTitle title="Earnings / Price" />
        <RankCircle rank={metric.pe_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.pe_value}
          secMedian={metric.pe_sec_median}
          secRank={metric.pe_sec_rank}
          indMedian={metric.pe_ind_median}
          indRank={metric.pe_ind_rank}
        />
      </Card>
      <Card size="large" location="middleLeft">
        <CardTitle title="Book / Price" />
        <RankCircle rank={metric.pb_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.pb_value}
          secMedian={metric.pb_sec_median}
          secRank={metric.pb_sec_rank}
          indMedian={metric.pb_ind_median}
          indRank={metric.pb_ind_rank}
        />
      </Card>
      <Card size="large" location="middleRight">
        <CardTitle title="Sales / Price" />
        <RankCircle rank={metric.ps_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.ps_value}
          secMedian={metric.ps_sec_median}
          secRank={metric.ps_sec_rank}
          indMedian={metric.ps_ind_median}
          indRank={metric.ps_ind_rank}
        />
      </Card>
      <Card size="large" location="right">
        <CardTitle title="FCF / Price" />
        <RankCircle rank={metric.pcf_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.pcf_value}
          secMedian={metric.pcf_sec_median}
          secRank={metric.pcf_sec_rank}
          indMedian={metric.pcf_ind_median}
          indRank={metric.pcf_ind_rank}
        />
      </Card>

    </>
    );
  };

export default App;