import React from 'react';
import './index.css';


const sizeConfig = {
  small: {
    height: '16em'
  },
  large: {
    height: '26.5em' //'24.5em'
  }
};

const marginConfig = {
  left: {
    marginClass: 'margin-1'
  },
  middleLeft: {
    marginClass: 'margin-2'
  },
  middleRight: {
    marginClass: 'margin-1'
  },
  right: {
    marginClass: ''
  }
};

const Card = ({ size, location, children }) => {
  const { height } = sizeConfig[size];
  const cardStyle = {
    height: height,
  };

  const { marginClass } = marginConfig[location];
    
  return (
		<div className={`card ${marginClass}`} style={cardStyle}>
      {children}
    </div>
	)
};

Card.defaultProps = {
  margin: '',
  location: ''
};

export default Card;