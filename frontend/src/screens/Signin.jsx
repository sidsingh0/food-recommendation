import React from 'react'
import FoodImg from '/food.png'
import { useRef,useState } from 'react'
import axios from "axios";
import { useNavigate } from 'react-router-dom';
import { HttpRequest,HTTP_METHODS } from '../services/ApiService';
import ApiUrls from '../services/ApiUrls';

function Signin() {
  const [error,setError]=useState("")
  const navigate = useNavigate();

  const usernameRef=useRef(null)
  const passwordRef=useRef(null)
  const registerNameRef=useRef(null)
  const registerEmailRef=useRef(null)
  const registerPasswordRef=useRef(null)
  const registerUsernameRef=useRef(null)

  const handleSignin=(e)=>{
    const username=usernameRef.current.value
    const password=passwordRef.current.value
    HttpRequest(ApiUrls.signin, HTTP_METHODS.POST,{username,password})
        .then((response) => {
            console.log(response);
            if (response?.success === 1) {    
                localStorage.setItem("token",response.token)
                setError(response?.message)
                navigate("/")
            }else{
              setError(response?.message)
            }
      });
  }

  const handleRegister = () =>{
    const username=registerUsernameRef.current.value
    const password=registerPasswordRef.current.value
    const email=registerEmailRef.current.value
    const name=registerNameRef.current.value
    HttpRequest(ApiUrls.register, HTTP_METHODS.POST,{name,email,username,password})
        .then((response) => {
            console.log(response);
            if (response?.success === 1) {    
                localStorage.setItem("token",response.token)
                setError(response?.message)
                navigate("/")
            }else{
              if(Array.isArray(response?.message)){
                const arrayError=response?.message?.join(", ")
                setError(arrayError);
              }else{
                setError(response?.message)
              }
            }
      });
  }
  return (
    <div className="container">
        <div className="row justify-content-center align-items-center signincontainer">
            <div className="signin_box mb-4 col-xl-4 col-lg-6 col-md-8 d-flex justify-content-center align-items-center flex-column rounded-4 p-4">
              <img className="signin_img mb-4" src={FoodImg} />
              {error && (<p>{error}</p>)}

              <div className="w-100">
                <ul class="nav nav-tabs align-items-center justify-content-center mb-2" id="myTab" role="tablist">
                  <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Sign In</button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Register</button>
                  </li>
                </ul>
                <div class="tab-content" id="myTabContent">
                  <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
                    <div className="mb-3 w-100">
                      <label htmlFor="username" className="form-label">Username</label>
                      <input ref={usernameRef} type="text" className="form-control" id="username" placeholder=""/>
                    </div>
                    <div className="mb-3 w-100">
                      <label htmlFor="password" className="form-label">Password</label>
                      <input ref={passwordRef} type="password" className="form-control" id="password" placeholder=""/>
                    </div>
                    <div className="d-flex justify-content-center"><button className='hero_button' onClick={handleSignin}>Sign in</button></div>
                  </div>
                  <div class="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">
                    <div className="mb-3 w-100">
                      <label htmlFor="registername" className="form-label">Name</label>
                      <input ref={registerNameRef} type="text" className="form-control" id="registername" placeholder=""/>
                    </div>
                    <div className="mb-3 w-100">
                      <label htmlFor="registeremail" className="form-label">Email</label>
                      <input ref={registerEmailRef} type="email" className="form-control" id="registeremail" placeholder=""/>
                    </div>
                    <div className="mb-3 w-100">
                      <label htmlFor="registerusername" className="form-label">Username</label>
                      <input ref={registerUsernameRef} type="text" className="form-control" id="registerusername" placeholder=""/>
                    </div>
                    <div className="mb-3 w-100">
                      <label htmlFor="registerpassword" className="form-label">Password</label>
                      <input ref={registerPasswordRef} type="password" className="form-control" id="registerpassword" placeholder=""/>
                    </div>
                    <div className="d-flex justify-content-center"><button className='hero_button' onClick={handleRegister}>Register</button></div>
                  </div>
                </div>
              </div>
            </div>
        </div>
    </div>
  )
}

export default Signin