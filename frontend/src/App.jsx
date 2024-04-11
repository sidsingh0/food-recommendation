import { BrowserRouter as Router, Route, Link, Routes,useParams  } from "react-router-dom";
import { Toaster } from 'react-hot-toast';
import Dish from './screens/Dish';
import Questions from './screens/Questions';
import Home from "./screens/Home"
import Signin from './screens/Signin';
import Wishlist from './screens/Wishlist';
import Navbar from "./components/Navbar";
import Explore from "./screens/Explore";

function App() {
  return (
    <div className="App">
        <Router>
            <Navbar/>
            <Toaster />
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route exact path="questions" element={<Questions />} />
                <Route exact path="explore" element={<Explore/>}/>
                <Route exact path="wishlist" element={<Wishlist />} />
                <Route exact path="signin" element={<Signin />}></Route>
                <Route exact path="dish/:id" element={<Dish />}></Route>
            </Routes>
        </Router>
    </div>
  )
}

export default App
