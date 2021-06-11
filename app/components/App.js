import React, { useState, useEffect } from 'react';
import Header from './Header';
import Menu from './Menu';
import { menus } from '../menu';
/*
const menus = [
  {id: 0, name: 'Overview'}, 
  {id: 1, name: 'Valuation'},
  {id: 2, name: 'Momentum'},
  {id: 3, name: 'Quality'}
];
*/
const App = () => {
  const [selectedMenu, setSelectedMenu] = useState(menus[0]);

  return (
    <div>
      <Header />
      <Menu 
        menus={menus} 
        selectedMenu={selectedMenu} 
        onMenuSelect={setSelectedMenu} 
      />
    </div>
  );
}

export default App;