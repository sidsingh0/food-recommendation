import React, { useState, useEffect } from 'react';
import axios from "axios";
import Card from '../components/Card';
import { HTTP_METHODS, HttpRequest } from '../services/ApiService';
import ApiUrls from '../services/ApiUrls';
import { toast } from 'react-hot-toast';

function Wishlist() {
  const [wishlist, setWishlist]=useState([]);
  const [reccommendation, setReccommendation]=useState([]);

  useEffect(()=>{
    HttpRequest(ApiUrls.getWishlist, HTTP_METHODS.GET)
      .then((response) => {
          if (response.success == 1) {  
            setReccommendation(response.dishes)
            setWishlist(response.wishlist)
          }else{
            // toast.error(response.message)
          }
      });
  },[])
  
  const updateWishlist = () =>{
    HttpRequest(ApiUrls.getWishlist, HTTP_METHODS.GET)
      .then((response) => {
          console.log(response);
          if (response.success == 1) {  
            setReccommendation(response.dishes)
            setWishlist(response.wishlist)
          }else{
            if (response.wishlist_count==0){
              setReccommendation([])
              setWishlist([])
            }
          }
      });
  }

  return (
    <div className="container">
      <h1 className="mb-2">
        Your Wishlist
      </h1>
      <div className="row mb-4">
      {wishlist.length>0 && wishlist.map((dish,index)=>(
        <div className="col-xl-3 col-lg-6 align-items-stretch mb-3">
          <Card key={dish.index} dish={dish} updateWishlist={updateWishlist}></Card>
        </div>
      ))}
      {wishlist.length<1 && (<p>No items in your wishlist yet!</p>)}
      </div>
      <h1 className="mb-2">
        You'll also like
      </h1>
      <div className="row mb-4">
      {reccommendation.length>0 && reccommendation.map((dish,index)=>(
        <div className="col-xl-3 col-lg-6 align-items-stretch mb-3">
          <Card key={dish.index} dish={dish} updateWishlist={updateWishlist}></Card>
        </div>
      ))}
      {reccommendation.length<1 && (<p>Start wishlisting to recieve reccommendations!</p>)}
      </div>
    </div>
  )
}

export default Wishlist;