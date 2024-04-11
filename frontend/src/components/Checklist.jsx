import React, { useState, useEffect } from "react";
import { toast } from "react-hot-toast";

function Checklist({ steps }) {
    const [instructions, setInstructions] = useState([]); // empty array
    useEffect(() => {
        if (steps) {
            steps = steps.replace(/'/g, '"');
            const stepsArray = JSON.parse(steps).map((step) => step.trim().charAt(0).toUpperCase() + step.trim().slice(1));
            const stepsObject = stepsArray.map((step, index) => ({
                index,
                step,
                completed: false,
            }));
            setInstructions(stepsObject);
        }
    }, [steps]);
    
    const handleToggleCompleted = (index) => {
        const prevDone=true;
        instructions.forEach(instruction => {
            if (instruction.index<index && !instruction.completed){
                toast.error("Complete the pending steps first!");
                prevDone=false
            }
        });
        if(prevDone){
            setInstructions(prevInstructions =>
                prevInstructions.map((item, itemIndex) =>
                  itemIndex === index ? { ...item, completed: !item.completed } : item
                )
            );
            
        }
    };

    useEffect(()=>{
        const areAllStepsCompleted = instructions.every(instruction => instruction.completed);
        if (areAllStepsCompleted){
            toast.success("Recipe Completed! Enjoy your meal!");
        }
    },[instructions])

    return (
        <>
            {instructions.map((instruction) => (
                <div className="d-flex gap-2 align-items-center">
                    <label>
                        <input type="checkbox" className="input"
                            id={"checkbox"+String(instruction.index)}
                            checked={instruction.completed}
                            onChange={()=>{handleToggleCompleted(instruction.index)}}
                        />
                        <span className="custom-checkbox"></span>
                    </label>
                    <label className={`dish_body mb-0 ${instruction.completed ? 'strikethrough' : ''}`} htmlFor={"checkbox"+String(instruction.index)}>{instruction.step}</label>
                </div>
            ))}
        </>
    );
}

export default Checklist;
