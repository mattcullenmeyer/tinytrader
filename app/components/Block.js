import React from 'react';
import './Block.css';

const Block = ({ children }) => {
  return <div className="block-container">{children}</div>;
}

export default Block;