import React from 'react'
import { Link } from 'react-router-dom'
import HeroImg from '/hero.png'
function Home() {
  return (
    <div className='container home_banner'>
      <h1 className='col-xl-4'><span>Flavors </span> at your Fingertips</h1>
      <p className='mt-2'>Unlock a world of endless recipes personalised for you.</p>
      <Link className='hero_btn mt-4'><box-icon name='bowl-rice' color="white"></box-icon>Explore Recipes</Link>
    </div>
  )
}

export default Home