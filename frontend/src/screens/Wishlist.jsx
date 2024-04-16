import React, { useState, useEffect, useContext } from 'react';
import { AuthContext } from '../services/AuthContext'; 
import Card from '../components/Card';
import { HTTP_METHODS, HttpRequest } from '../services/ApiService';
import ApiUrls from '../services/ApiUrls';
import { toast } from 'react-hot-toast';

function Wishlist() {

  const [wishlist, setWishlist]=useState([]);
  const [recommendation, setRecommendation]=useState([]);
  const { handleLogout } = useContext(AuthContext);

  // Api call to get recommendations and wishlist details
  const fetchWishlistData = () => {
    HttpRequest(ApiUrls.getWishlist, HTTP_METHODS.GET, null, handleLogout)
      .then((response) => {
        if (response.success === 1) {  
          setRecommendation(response.dishes);
          setWishlist(response.wishlist);
        } else {
          if (response.message) {
            toast.error(response.message);
          }
        }
      });
  };

  useEffect(() => {
    fetchWishlistData();
  }, []);

  const updateWishlist = () => {
    fetchWishlistData();
  };

  return (
    <div className="container">
      <h1 className="mb-2">
        Your Wishlist
      </h1>
      <div className="row mb-4">
        {wishlist.length > 0 ? (
          wishlist.map((dish) => (
            <div className="col-xl-3 col-lg-6 align-items-stretch mb-3" key={dish.index}>
              <Card dish={dish} updateWishlist={updateWishlist} />
            </div>
          ))
        ) : (
          <p>No items in your wishlist yet!</p>
        )}
      </div>
      <h1 className="mb-2">You'll also like</h1>
      <div className="row mb-4">
        {recommendation.length > 0 ? (
          recommendation.map((dish) => (
            <div className="col-xl-3 col-lg-6 align-items-stretch mb-3" key={dish.index}>
              <Card dish={dish} updateWishlist={updateWishlist} />
            </div>
          ))
        ) : (
          <p>Start wishlisting to receive recommendations!</p>
        )}
      </div>
    </div>
  )
}

export default Wishlist;
