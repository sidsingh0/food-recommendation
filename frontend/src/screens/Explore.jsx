import React, {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom';
import Card from '../components/Card';

function Explore() {
    const [dishes, setDishes] = useState([]);
    const [recommendations, setRecommendations] = useState([]);
    const navigate = useNavigate(); 

    useEffect(() => {
        const storedData = localStorage.getItem('dishes');
        if (storedData) {
            setDishes(JSON.parse(storedData));
        }
        const storedRec = localStorage.getItem('recommendations')
        if (storedRec) {
            setRecommendations(JSON.parse(storedRec));
        }
    }, [ navigate]);

    return (
        <div className="container">
            <h1 className="mb-2">Search Results</h1>
            <div className="row mb-4">
                {dishes.map((dish, index) => (
                    <div className="col-xl-3 col-lg-6 align-items-stretch mb-3">
                        <Card  key={dish.index} dish={dish}/>
                    </div>
                ))}
            </div>
            <h1 className="mb-2">Also consider</h1>
            <div className="row mb-4">
                {recommendations.map((dish, index) => (
                    <div className="col-xl-3 col-lg-6 align-items-stretch mb-3">
                        <Card key={dish.index} dish={dish}/>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Explore