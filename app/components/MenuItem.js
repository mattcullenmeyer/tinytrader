import React from 'react';
import './MenuItem.css';

const MenuItem = ({ menu, selectedMenu, onMenuSelect }) => {
  return (
      <button 
        onClick={() => onMenuSelect(menu)} 
        className={`menu-button ${menu === selectedMenu ? 'active' : ''}`}
      >
        {menu.name}
      </button>
  );
}

export default MenuItem;