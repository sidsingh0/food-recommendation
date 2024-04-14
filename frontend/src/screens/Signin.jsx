import React, { useContext, useEffect } from 'react';
import { AuthContext } from '../services/AuthContext'; 
import FoodImg from '/food.png'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import { HttpRequest,HTTP_METHODS } from '../services/ApiService';
import ApiUrls from '../services/ApiUrls';
import InputBox from '../components/InputBox';

function Signin() {
  const [username, setUsername] = useState({ value: "", error: "" });
  const [password, setPassword] = useState({ value: "", error: "" });
  const [rusername, setRUsername] = useState({ value: "", error: "" });
  const [rpassword, setRPassword] = useState({ value: "", error: "" });
  const [remail, setREmail] = useState({ value: "", error: "" });
  const [rname, setRName] = useState({ value: "", error: "" });

  const [error,setError]=useState("");
  const navigate = useNavigate();
  const { isLoggedIn, handleLogin } = useContext(AuthContext);

  useEffect(() => {
    if (isLoggedIn) {
      navigate('/')
    }
  }, [])
  

  const handleSignin=(e)=>{
    if(username.error==="" && password.error===""){
      HttpRequest(ApiUrls.signin, HTTP_METHODS.POST,{"username":username.value,"password":password.value})
        .then((response) => {
            if (response?.success === 1) {    
              handleLogin(response.token); 
              setError(response?.message)
              navigate("/")
            }else{
              setError(response?.message)
            }
      });
    }
  }

  const handleRegister = () =>{

    if(rusername.error==="" && rpassword.error==="" && rname.error==="" && remail.error===""){
      HttpRequest(ApiUrls.register, HTTP_METHODS.POST,{"username":rusername.value,"password":rpassword.value,"name":rname.value, "email":remail.value})
        .then((response) => {
            console.log(response);
            if (response?.success === 1) {    
              handleLogin(response.token); 
              setError(response?.message);
              navigate("/");
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
  }
  return (
    <div className="container signin">
        <div className="row justify-content-center align-items-center signincontainer">
            <div className="signin_box mb-4 col-xl-4 col-lg-6 col-md-8 d-flex justify-content-center align-items-center flex-column rounded-4 p-4">
              <img className="signin_img mb-4" src={FoodImg} />
              {error && (<p>{error}</p>)}

              <div className="w-100">
                <ul className="nav nav-tabs align-items-center justify-content-center mb-2" id="myTab" role="tablist">
                  <li className="nav-item" role="presentation">
                    <button className="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Sign In</button>
                  </li>
                  <li className="nav-item" role="presentation">
                    <button className="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Register</button>
                  </li>
                </ul>
                <div className="tab-content" id="myTabContent">
                  <div className="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabIndex="0">
                    <div className="mb-3 w-100">
                      <InputBox details={username}
                      setDetails={setUsername} 
                      maxLen={50} 
                      regex={/^[a-zA-Z0-9]*$/} 
                      regexText={"Please only enter letters and numbers."}
                      inputName={"Username"}
                      id={"username"} />
                    </div>
                    <div className="mb-3 w-100">
                      <InputBox 
                      details={password} 
                      setDetails={setPassword} 
                      maxLen={50} 
                      inputType={"password"} 
                      regex={/^[a-zA-Z0-9]*$/} 
                      regexText={"Please only enter letters and numbers."}
                      inputName={"Password"}
                      id={"password"} />
                    </div>
                    <div className="d-flex justify-content-center"><button className='hero_button' onClick={handleSignin}>Sign in</button></div>
                  </div>
                  <div className="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabIndex="0">
                    <div className="mb-3 w-100">
                      <InputBox 
                        details={rname} 
                        setDetails={setRName} 
                        maxLen={50} 
                        regex={/^[a-zA-Z\s]*$/} 
                        regexText={"Please only enter letters."}
                        inputName={"Name"}
                        id={"rname"}
                      />
                    </div>
                    <div className="mb-3 w-100">
                      <InputBox 
                          details={remail} 
                          setDetails={setREmail} 
                          maxLen={100} 
                          regex={/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/} 
                          regexText={"Please enter a valid email."}
                          inputType={"email"}
                          inputName={"Email"}
                          id={"remail"}
                        />
                    </div>
                    <div className="mb-3 w-100">
                      <InputBox 
                          details={rusername} 
                          setDetails={setRUsername} 
                          maxLen={50} 
                          regex={/^[a-zA-Z0-9]*$/} 
                          regexText={"Please only enter letters and numbers."}
                          inputName={"Username"}
                          id={"rusername"}
                        />
                    </div>
                    <div className="mb-3 w-100">
                        <InputBox 
                          details={rpassword} 
                          setDetails={setRPassword} 
                          maxLen={50} 
                          regex={/^[a-zA-Z0-9]*$/} 
                          regexText={"Please enter a valid email."}
                          inputType={"password"}
                          inputName={"Password"}
                          id={"rpassword"}
                        />
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