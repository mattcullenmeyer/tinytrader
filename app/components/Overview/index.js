import React from 'react';
// Components
import Card from '../Card';
import CardTitle from '../CardTitle';
import CardValue from '../CardValue';
import RankCircle from '../RankCircle';


const Overview = ({ metadata }) => {

  return (
    <div>
      <Card title="Price" size="small" location="left">
        <CardTitle title="Price" />
        <CardValue value={metadata.price} />
        <CardTitle title="Volume" />
        <CardValue value={metadata.volume} />
      </Card>
      <Card size="small" location="middleLeft">
        <CardTitle title="Bid-Ask" /> 
        <CardValue value={`${metadata.bid}-${metadata.ask}`} />
        <CardTitle title="Bid-Ask Spread" />
      </Card>
      <Card size="small" location="middleRight">
        <CardTitle title="Market Cap" /> 
        <CardValue value={metadata.market_cap} />
        <CardTitle title="Market Cap Size" />
        <CardValue value={metadata.market_cap_size.market_cap_size} />
      </Card>
      <Card size="small" location="right">
        <CardTitle title="Sector" /> 
        <CardValue value={metadata.sector.sector} />
        <CardTitle title="Industry" />
        <CardValue value={metadata.industry.industry} />
      </Card>
      
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
    </div>
  );
};

export default Overview;