import React, {useState, useEffect, useContext} from 'react'
import { AuthContext } from '../services/AuthContext'; 
import {Bookmark, BookmarkCheckFill} from 'react-bootstrap-icons';
import { Link } from 'react-router-dom';
import { HTTP_METHODS, HttpRequest } from '../services/ApiService';
import ApiUrls from '../services/ApiUrls';
import { toast } from 'react-hot-toast';

function Card({dish,updateWishlist}) {
  const { handleLogout } = useContext(AuthContext);
  const [wishlist, setWishlist]=useState(0)

  const capitalizeWords = (sentence) => {
    return sentence.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
  }
  function convertMinutesToHoursAndMinutes(minutes) {
    var hours = Math.floor(minutes / 60);
    var remainingMinutes = minutes % 60;
    if (hours===0){
      return remainingMinutes + " m";
    }else{
      return hours + " hr " + remainingMinutes + " m";
    }
  }
  const toggleWishlist = () => {
      HttpRequest(ApiUrls.wishlistToggle, HTTP_METHODS.POST, {"id":dish?.index},handleLogout)
      .then((response) => {
          if (response.success == 1) {  
            setWishlist(response.is_in_wishlist)
            toast.success(response.message)
            if (updateWishlist){
              updateWishlist()
            }
          }else{
            if(response.success==0){
              toast.error(response.message)
            }
          }
      });
  }

  useEffect(()=>{
    HttpRequest(ApiUrls.checkWishlist+String(dish?.index), HTTP_METHODS.GET, null, handleLogout)
      .then((response) => {
          if (response.success == 1) {  
            setWishlist(response.is_in_wishlist)
          }
      });
  },[])
  
  return (
    <div className="card p-3">
      <div className="d-flex" style={{gap:"10px"}}>
        <div className="card_wishlist mb-2" onClick={toggleWishlist}>
          {wishlist ? <BookmarkCheckFill size={20}/> : <Bookmark size={20} />}
        </div>
        <div className="card_time mb-2" onClick={toggleWishlist}>
          {dish?.minutes && convertMinutesToHoursAndMinutes(dish?.minutes)}
        </div>
      </div>
      <Link to={`/dish/${dish?.index}`}>
        <h6>{dish?.name && capitalizeWords(String(dish.name))}</h6>
        {dish?.difference && <p className="m-0 mb-1"><span className="card_bold">Needs: {dish?.difference}</span></p>}
        {dish?.ingredients && <p className="m-0">Ingredients: {dish?.ingredients}</p>}
      </Link>
    </div>
  )
}

export default Card