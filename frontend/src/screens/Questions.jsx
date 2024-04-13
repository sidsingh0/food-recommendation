import React, {useRef, useState} from 'react'
import FoodImg from '/food.png'
import { useNavigate } from 'react-router-dom';
import {Trash} from 'react-bootstrap-icons';
import { HttpRequest,HTTP_METHODS } from '../services/ApiService';
import ApiUrls from '../services/ApiUrls';
import { toast } from 'react-hot-toast';

function Questions() {
  const [error,setError]=useState("")
  const [minutes, setMinutes]=useState("")
  const [ingredient, setIngredient] = useState('');
  const [ingredientList, setIngredientList] = useState([]);
  const navigate = useNavigate();

  const handleSubmit =()=>{
    if (ingredientList.length>1){
      HttpRequest(ApiUrls.promptDetails, HTTP_METHODS.POST,{"ingredients":ingredientList.join(","),minutes})
        .then((response) => {
          console.log(response);
          if (response.success==1){
            setError("")
            const dish_list=response.dishes
            const recommendation_list=response.recommendations
            localStorage.setItem('dishes', JSON.stringify(dish_list));
            localStorage.setItem('recommendations', JSON.stringify(recommendation_list));
            navigate('/explore');
          }
          else{
            setError(response.message)
          }
      });
    }else{
      toast.error("Add atleast 2 ingredients")
    } 
  }

  const handleMinutesChange = (e) => {
    const value = e.target.value.replace(/\D/g, ''); //only accepting numbers
    setMinutes(value);
  }
  const handleNolimit = () =>{
    setMinutes("");
  }

  const handleIngredientChange = (e) =>{
    const value = e.target.value.replace(/[^A-Za-z,\s]/g, '');
    setIngredient(value);
  }
  const handleIngredientAdd = () =>{
    if (ingredient.trim() !== ""){
      if (!ingredientList.includes(ingredient)){
        setIngredientList(prevList => [...prevList,ingredient]);
      }else{
        toast.error("Ingredient already added")
      }
      setIngredient("")
    }
  }
  const handleEnterPress = (e) =>{
    if (e.key === 'Enter'){
      handleIngredientAdd();
    }
  }
  const handleIngredientRemove = (ingredientToRemove) =>{
    setIngredientList(prevList => prevList.filter(ingredient=>ingredient!==ingredientToRemove));
  }
  return (
    <div className="container">
        <div className="row justify-content-center align-items-center signincontainer">
            <div className="signin_box mb-4 col-xl-4 col-lg-6 col-md-8 d-flex justify-content-center align-items-center flex-column rounded-4 p-4">
              {/* <img className="signin_img" src={FoodImg} /> */}
              <h2 className="mb-3">Find Recipes</h2>
              {error && (<p className="error">{error}</p>)}
              <label htmlFor="ingredients" className="w-100 form-label">Ingredients</label>
              <div className="row w-100 questions_minutes_container">
                <div className="questions_minutes">
                  <input 
                    value={ingredient} 
                    onChange={(e) => handleIngredientChange(e)}
                    onKeyDown={(e) => handleEnterPress(e)}
                    type="text" className="form-control" id="ingredients" placeholder=""/>                
                </div>
                <button onClick={handleIngredientAdd} className="questions_ingredient_add">
                  <p>+ Add Item</p>
                </button>
              </div>
              {ingredientList.map((ingredient,index)=>(
                <div key={index} className="w-100 questions_ingredient_item">
                  <p>{ingredient}</p>
                  <Trash size={20} onClick={()=>handleIngredientRemove(ingredient)} />
                </div>
              ))}
              <label htmlFor="minutes" className="w-100 mt-3 form-label">Time you can spare for cooking (in minutes)</label>
              <div className="mb-3 row w-100 questions_minutes_container">
                <div className="questions_minutes">
                  <input 
                    value={minutes} 
                    onChange={(e) => handleMinutesChange(e)}
                    type="text" className="form-control" id="minutes" placeholder=""/>                
                </div>
                <button onClick={handleNolimit} className={minutes===""?("questions_limit_yes"):("questions_limit")}>
                  <p>No limit</p>
                </button>
              </div>

              <div className="d-flex justify-content-center"><button className='hero_button' onClick={handleSubmit}>Find Dishes</button></div>
            </div>
        </div>
    </div>
  )
}

export default Questions