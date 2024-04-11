import React, { useState, useEffect } from 'react';
import {Bookmark, BookmarkCheckFill } from 'react-bootstrap-icons';
import { useParams,useNavigate } from 'react-router-dom';
import Card from '../components/Card';
import { HTTP_METHODS, HttpRequest } from '../services/ApiService';
import ApiUrls from '../services/ApiUrls';
import { toast } from 'react-hot-toast';

function Dish() {
  const { id } = useParams(); 
  const navigate = useNavigate(); 
  const [wishlist, setWishlist]=useState(0)
  const [dishes, setDishes] = useState([]);
  const [currentDish, setCurrentDish]=useState({})

  function capitalizeWords(sentence) {
    return sentence.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
  }
  
  const toggleWishlist = () => {
    HttpRequest(ApiUrls.wishlistToggle, HTTP_METHODS.POST, {"id":currentDish?.index})
    .then((response) => {
        if (response.success == 1) {  
          setWishlist(response.is_in_wishlist)
          toast.success(response.message)
        }
    });
  }

  useEffect(()=>{
    HttpRequest(ApiUrls.getDishDetails+String(id), HTTP_METHODS.GET)
      .then((response) => {
          console.log(response);
          if (response.success == 1) {  
            setCurrentDish(response.currentdish)
            setDishes(response.dishes)
          }else{
            navigate('/')
          }
      });
  },[id])

  return (
    <div className="container">
      <div className="row mb-4">
        <div className="col-xl-8 px-0 pe-xl-4 mb-4">
          <div className="dish_panel rounded-4 p-4">
            <div className="dish_header">
              <h1>{currentDish?.name && capitalizeWords(String(currentDish.name))}</h1>
              <div className="dish_wishlist" onClick={toggleWishlist}>
                {wishlist ? <BookmarkCheckFill size={20}/> : <Bookmark size={20} />}
              </div>
            </div>
            <p className="mt-2 dish_body">
            {currentDish?.description}
            </p>
            <h2 className="pt-4">Ingredients</h2>
            <p className="mt-2 dish_body">
            {currentDish?.ingredients}
            </p>
            <h2 className="pt-4">Steps</h2>
            <p className="mt-2 mb-0 dish_body">
              Rosemary, Thyme, Sun dried tomatoes, onions, salad greens, garlic.
            </p>
          </div>
        </div>
        <div className="col-xl-4 px-0">
          <div className="dish_panel rounded-4 p-4">
            <h2>Nutritional Facts</h2>
            <div className="dish_nutrition_list d-flex">
              <p className="mt-2 mb-0 dish_body">Calories</p>
              <p className="mt-2 mb-0 dish_body text-black">50 cal</p>
            </div>
          </div>
          <div className="dish_panel rounded-4 p-4 mt-4">
            <h2 className="pb-2">Similar Dishes</h2>
            <div className="d-flex flex-column dish_similar_list">
              {dishes.map((dish,index)=>(
                <Card key={index} dish={dish}/>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Dish;