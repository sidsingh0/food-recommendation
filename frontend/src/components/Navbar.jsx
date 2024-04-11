import React from 'react'
import { Link } from 'react-router-dom';
import Logo from '/logo.png';

function Navbar() {
  const token = localStorage.getItem("token");
  const handleSignout = () =>{
    localStorage.setItem(null);
  }
  return (
    <nav className='navbar container'>
        <div className='navbar_start'>
            <Link to="/" className='nav_link'>Home</Link>
            <Link to="/questions" className='nav_link'>Explore</Link>
            <Link to="/wishlist" className='nav_link'>Wishlist</Link>
        </div>
        <Link to="/" className='nav_mid'><img src={Logo}/></Link>
        {token? (<button onClick={handleSignout} className='hero_button'>Sign Out</button>):(<Link to="/signin"><button className='hero_button'>Sign in</button></Link>)}
    </nav>
  )
}

export default Navbar