import { BrowserRouter as Router, Route, Link, Routes,useParams  } from "react-router-dom";
import { Toaster } from 'react-hot-toast';
import Dish from './screens/Dish';
import Questions from './screens/Questions';
import Home from "./screens/Home"
import Signin from './screens/Signin';
import Wishlist from './screens/Wishlist';
import Navbar from "./components/Navbar";
import Explore from "./screens/Explore";
import ProtectedRoute from './services/ProtectedRoute';
import { AuthContext, AuthProvider } from './services/AuthContext';

function App() {
  return (
    <AuthProvider>
      <div className="App">
        <Router>
            <Navbar/>
            <Toaster />
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route exact path="signin" element={<Signin />}></Route>
                <Route exact path="wishlist" element={<ProtectedRoute><Wishlist /></ProtectedRoute>}/>
                <Route exact path="dish/:id" element={<ProtectedRoute><Dish /></ProtectedRoute>}/>
                <Route exact path="questions" element={<ProtectedRoute><Questions /></ProtectedRoute>} />
                <Route exact path="explore" element={<ProtectedRoute><Explore/></ProtectedRoute>}/>
            </Routes>
        </Router>
      </div>
    </AuthProvider>
  )
}

export default App
