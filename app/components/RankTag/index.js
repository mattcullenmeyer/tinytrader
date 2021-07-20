import './index.css';
import React from 'react';

const RankTag = ({ tagName }) => {
  return (
    <div className="rank-tag-container">
      <div className="rank-tag">{tagName}</div>
    </div>
  );
};

export default RankTag;