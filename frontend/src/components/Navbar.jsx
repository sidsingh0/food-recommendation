import React from 'react'
import { Link } from 'react-router-dom';
import 'boxicons';
function Navbar() {
  return (
    <nav className='navbar container'>
        <Link to="/" className='nav_link nav_logo'><span className='nav_link_span'>RECIPE</span>LAB</Link>
        <div className='navbar_mid'>
            <Link to="/" className='nav_link'>Home</Link>
            <Link to="/explore" className='nav_link'>Explore</Link>
            <Link to="/wishlist" className='nav_link'>Wishlist</Link>
        </div>
        <Link to="/"><box-icon name='user-circle' className='nav_link'></box-icon></Link>
    </nav>
  )
}

export default Navbar