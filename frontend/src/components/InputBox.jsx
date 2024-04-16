import React, {useState} from 'react'

function InputBox({details, setDetails, maxLen, regex, regexText, inputType="text", inputName, id}) {
  
  const handleChange = (e) =>{
    const value = e.target.value.substring(0,maxLen);
    if (value!==""){
      if (regex.test(value)){
        setDetails({error:"" ,value})
      }else{
        setDetails({error:regexText ,value})
      }
    }else{
      setDetails(({error:"This field shouldn't be empty." ,value}))
    }
  }

  return (
    <>
        <label htmlFor="username" className="form-label">{inputName}</label>
        <input  onChange={(e) => handleChange(e)} value={details.value} type={inputType} className="form-control" id={id} placeholder=""/>
        {details.error && <p id="error-message" className="text-danger">{details.error}</p>}
    </>
  )
}

export default InputBox
