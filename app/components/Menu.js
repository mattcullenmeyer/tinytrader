import React from 'react';
import MenuItem from './MenuItem';

const Menu = ({ menus, selectedMenu, onMenuSelect }) => {

  const renderedMenuList = menus.map(menu => {
    return (
      <MenuItem 
        key={menu.id}
        menu={menu}
        selectedMenu={selectedMenu}
        onMenuSelect={onMenuSelect}
      />
    )
  })
  
  return <div>{renderedMenuList}</div>;
}

export default Menu;