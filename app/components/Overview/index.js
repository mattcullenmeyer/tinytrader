import React from 'react';
import Card from '../Card';
import RankCircle from '../RankCircle';


const Overview = ({ metadata }) => {
  return (
    <>
      <Card title="Overview" size="small" location="left">
        <RankCircle rank={metadata.composite_rank} />
      </Card>
      <Card title="Valuation" size="small" location="middleLeft">
        <RankCircle rank={metadata.value_rank} />
      </Card>
      <Card title="Momentum" size="small" location="middleRight">
        <RankCircle rank={metadata.mom_rank} />
      </Card>
      <Card title="Quality" size="small" location="right">
        <RankCircle rank={metadata.quality_rank} />
      </Card>
    </>
  );
};

export default Overview;