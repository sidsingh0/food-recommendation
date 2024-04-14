import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import { AuthContext } from './AuthContext';

const ProtectedRoute = ({ children }) => {
    const { isLoggedIn } = useContext(AuthContext);

    if (!isLoggedIn) {
        return <Navigate to="/signin" replace />;
    }

    return children;
};

export default ProtectedRoute;
