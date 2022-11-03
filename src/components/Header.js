import React from 'react';
import { NavLink } from 'react-router-dom';

const Header = () => {
  return (
    <header>
      <h1>Management App</h1>
      <hr />
      <div className="links">
        <NavLink to="/" className="link" activeClassName="active" exact>
          Users list
        </NavLink>
        <NavLink to="/add" className="link" activeClassName="active">
          Add new user
        </NavLink>
      </div>
    </header>
  );
};

export default Header;
