import React, { useContext } from 'react';
import { AuthContext } from '../services/AuthContext'; 
import { Link } from 'react-router-dom';
import Logo from '/logo.png';
import {List} from 'react-bootstrap-icons'

function Navbar() {
  const { isLoggedIn, handleLogout } = useContext(AuthContext);

  return (
    <nav className='navbar container'>
        <div className='navbar_start'>
            <Link to="/" className='nav_link'>Home</Link>
            <Link to="/questions" className='nav_link'>Explore</Link>
            <Link to="/wishlist" className='nav_link'>Wishlist</Link>
        </div>
        <Link to="/" className='nav_mid'><img src={Logo}/></Link>
        {isLoggedIn? (<button onClick={handleLogout} className='hero_button'>Sign Out</button>):(<Link to="/signin"><button className='hero_button'>Sign in</button></Link>)}
        <div className="dropdown nav_dropdown">
          <button className="navbar_btn" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            <List size={20} color={"#000"}/>
          </button>
          <ul className="dropdown-menu">
            <li><Link to="/" className='dropdown-item nav_link'>Home</Link></li>
            <li><Link to="/questions" className='dropdown-item nav_link'>Explore</Link></li>
            <li><Link to="/wishlist" className='dropdown-item nav_link'>Wishlist</Link></li>
            <li>{isLoggedIn? (<Link onClick={handleLogout} className='dropdown-item nav_link'>Sign Out</Link>):(<Link to="/signin" className='dropdown-item nav_link'>Sign In</Link>)}</li>
          </ul>
        </div>
    </nav>
  )
}

export default Navbar