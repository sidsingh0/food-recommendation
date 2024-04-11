import React, {useState, useEffect} from 'react'
import {Bookmark} from 'react-bootstrap-icons';
import {BookmarkCheckFill} from 'react-bootstrap-icons';
import { Link } from 'react-router-dom';
import { HTTP_METHODS, HttpRequest } from '../services/ApiService';
import ApiUrls from '../services/ApiUrls';
import { toast } from 'react-hot-toast';

function Card({dish,updateWishlist}) {

  const [wishlist, setWishlist]=useState(0)

  const capitalizeWords = (sentence) => {
    return sentence.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
  }

  const toggleWishlist = () => {
      HttpRequest(ApiUrls.wishlistToggle, HTTP_METHODS.POST, {"id":dish?.index})
      .then((response) => {
          if (response.success == 1) {  
            setWishlist(response.is_in_wishlist)
            toast.success(response.message)
            if (updateWishlist){
              updateWishlist()
            }
          }
      });
  }

  useEffect(()=>{
    HttpRequest(ApiUrls.checkWishlist+String(dish?.index), HTTP_METHODS.GET)
      .then((response) => {
          if (response.success == 1) {  
            setWishlist(response.is_in_wishlist)
          }
      });
  },[])
  
  return (
    <div className="card p-3">
      <div className="card_wishlist mb-2" onClick={toggleWishlist}>
        {wishlist ? <BookmarkCheckFill size={20}/> : <Bookmark size={20} />}
      </div>
      <Link to={`/dish/${dish?.index}`}>
        <h6>{dish?.name && capitalizeWords(String(dish.name))}</h6>
        <p className="m-0">{dish?.ingredients}</p>
      </Link>
    </div>
  )
}

export default Card