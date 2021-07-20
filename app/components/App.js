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
import RankTag from './RankTag';
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
        <RankTag tagName="Value" />
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
        <RankTag tagName="Value" />
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
        <RankTag tagName="Value" />
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
        <RankTag tagName="Value" />
      </Card>

      <Card size="large" location="left">
        <CardTitle title="EBITDA / EV" />
        <RankCircle rank={metric.eve_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.eve_value}
          secMedian={metric.eve_sec_median}
          secRank={metric.eve_sec_rank}
          indMedian={metric.eve_ind_median}
          indRank={metric.eve_ind_rank}
        />
        <RankTag tagName="Value" />
      </Card>
      <Card size="large" location="middleLeft">
        <CardTitle title="6M Price Return" />
        <RankCircle rank={metric.mom_6_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.mom_6_value}
          secMedian={metric.mom_6_sec_median}
          secRank={metric.mom_6_sec_rank}
          indMedian={metric.mom_6_ind_median}
          indRank={metric.mom_6_ind_rank}
        />
        <RankTag tagName="Momentum" />
      </Card>
      <Card size="large" location="middleRight">
      <CardTitle title="12M Price Return" />
        <RankCircle rank={metric.mom_12_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.mom_12_value}
          secMedian={metric.mom_12_sec_median}
          secRank={metric.mom_12_sec_rank}
          indMedian={metric.mom_12_ind_median}
          indRank={metric.mom_12_ind_rank}
        />
        <RankTag tagName="Momentum" />
      </Card>
      <Card size="large" location="right">
      <CardTitle title="5Y Beta" />
        <RankCircle rank={metric.beta_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.beta_value}
          secMedian={metric.beta_sec_median}
          secRank={metric.beta_sec_rank}
          indMedian={metric.beta_ind_median}
          indRank={metric.beta_ind_rank}
        />
        <RankTag tagName="Volatility" />
      </Card>

      <Card size="large" location="left">
      <CardTitle title="12M Volatility" />
        <RankCircle rank={metric.vol_12_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.vol_12_value}
          secMedian={metric.vol_12_sec_median}
          secRank={metric.vol_12_sec_rank}
          indMedian={metric.vol_12_ind_median}
          indRank={metric.vol_12_ind_rank}
        />
        <RankTag tagName="Volatility" />
      </Card>
      <Card size="large" location="middleLeft">
      <CardTitle title="Asset Turnover" />
        <RankCircle rank={metric.asset_turn_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.asset_turn_value}
          secMedian={metric.asset_turn_sec_median}
          secRank={metric.asset_turn_sec_rank}
          indMedian={metric.asset_turn_ind_median}
          indRank={metric.asset_turn_ind_rank}
        />
        <RankTag tagName="Profitability" />
      </Card>
      <Card size="large" location="middleRight">
      <CardTitle title="Gross Profitability" />
        <RankCircle rank={metric.gross_profit_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.gross_profit_value}
          secMedian={metric.gross_profit_sec_median}
          secRank={metric.gross_profit_sec_rank}
          indMedian={metric.gross_profit_ind_median}
          indRank={metric.gross_profit_ind_rank}
        />
        <RankTag tagName="Profitability" />
      </Card>
      <Card size="large" location="right">
      <CardTitle title="Gross Margin" />
        <RankCircle rank={metric.gross_margin_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.gross_margin_value}
          secMedian={metric.gross_margin_sec_median}
          secRank={metric.gross_margin_sec_rank}
          indMedian={metric.gross_margin_ind_median}
          indRank={metric.gross_margin_ind_rank}
        />
        <RankTag tagName="Profitability" />
      </Card>

      <Card size="large" location="left">
      <CardTitle title="Return on Assets" />
        <RankCircle rank={metric.return_asset_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.return_asset_value}
          secMedian={metric.return_asset_sec_median}
          secRank={metric.return_asset_sec_rank}
          indMedian={metric.return_asset_ind_median}
          indRank={metric.return_asset_ind_rank}
        />
        <RankTag tagName="Profitability" />
      </Card>
      <Card size="large" location="middleLeft">
      <CardTitle title="External Financing" />
        <RankCircle rank={metric.ext_fin_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.ext_fin_value}
          secMedian={metric.ext_fin_sec_median}
          secRank={metric.ext_fin_sec_rank}
          indMedian={metric.ext_fin_ind_median}
          indRank={metric.ext_fin_ind_rank}
        />
        <RankTag tagName="Financing" />
      </Card>
      <Card size="large" location="middleRight">
      <CardTitle title="Cash Flow / Debt" />
        <RankCircle rank={metric.cf_debt_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.cf_debt_value}
          secMedian={metric.cf_debt_sec_median}
          secRank={metric.cf_debt_sec_rank}
          indMedian={metric.cf_debt_ind_median}
          indRank={metric.cf_debt_ind_rank}
        />
        <RankTag tagName="Financing" />
      </Card>
      <Card size="large" location="right">
      <CardTitle title="Accruals / Assets" />
        <RankCircle rank={metric.accrual_sec_rank} />
        <Table
          ticker={tickerdata.ticker}
          value={metric.accrual_value}
          secMedian={metric.accrual_sec_median}
          secRank={metric.accrual_sec_rank}
          indMedian={metric.accrual_ind_median}
          indRank={metric.accrual_ind_rank}
        />
        <RankTag tagName="Safety" />
      </Card>

    </>
    );
  };

export default App;