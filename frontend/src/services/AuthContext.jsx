import React, { createContext, useState, useEffect } from 'react';

const AuthContext = createContext({
    isLoggedIn: false,
    setIsLoggedIn: () => {},
    user: null,
    setUser: () => {},
});

const AuthProvider = ({ children }) => {
    const [isLoggedIn, setIsLoggedIn] = useState(
        () => localStorage.getItem('token') !== null
    );

    const handleLogin = (token) => {  
        setIsLoggedIn(true);
        localStorage.setItem("token",token)
    };

    const handleLogout = () => {
        console.log("Logged out");
        setIsLoggedIn(false);
        localStorage.removeItem('token');
    };

    return (
        <AuthContext.Provider value={{ isLoggedIn, setIsLoggedIn, handleLogin, handleLogout }}>
            {children}
        </AuthContext.Provider>
    );
};

export { AuthContext, AuthProvider };
