import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import Dish from './screens/Dish';
import Explore from './screens/Explore';
import Home from "./screens/Home"
import Signin from './screens/Signin';
import Wishlist from './screens/Wishlist';
import Navbar from "./components/Navbar";

function App() {
  return (
    <div className="App">
        <Router>
            <Navbar/>
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route exact path="dish" element={<Dish />} />
                <Route exact path="explore" element={<Explore />} />
                <Route exact path="wishlist" element={<Wishlist />} />
                <Route exact path="signin" element={<Signin />}></Route>
            </Routes>
        </Router>
    </div>
  )
}

export default App
