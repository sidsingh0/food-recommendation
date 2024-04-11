import React from 'react'
import { Link } from 'react-router-dom'
import HeroImg from '/herodish.png'
import Blob from '/blob.png'
function Home() {
  return (
    <div className="container ">
      <div className="hero_container row">
        <div className="col-xl-5 col-lg-4 col-md-12 col-sm-12">
          <h1 className='source_serif'>Flavors at your Fingertips</h1>
          <p className='mt-3 mb-5'>Discover a world of personalized recipes, designed to perfectly match your tastes and dietary needs.</p>
          <Link to="/questions"><button className='hero_button mb-4'>Explore</button></Link>
        </div>
        <div className="col-xl-7 col-lg-8 col-md-8 col-sm-12">
          <img className="hero_img" src={HeroImg}/>
        </div>
        </div>
      <img className="hero_blob" src={Blob}/>
    </div>
  )
}

export default Home