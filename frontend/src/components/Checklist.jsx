import React, { useState, useEffect } from "react";
import { toast } from "react-hot-toast";

function Checklist({ steps }) {
    const [instructions, setInstructions] = useState([]);
    useEffect(() => {
        if (steps) {
            steps = steps.slice(1,-1).replace(/['"]/g, '');
            const stepsArray = steps.split(",").map((step) => step.trim().charAt(0).toUpperCase() + step.trim().slice(1));
            const stepsObject = stepsArray.map((step, index) => ({
                index,
                step,
                completed: false,
            }));
            setInstructions(stepsObject);
        }
    }, [steps]);
    
    const handleToggleCompleted = (index) => {
        let prevDone=true;
        //checking if previous steps, so the steps aren't skipped
        instructions.forEach(instruction => {
            if (instruction.index<index && !instruction.completed){
                prevDone=false;
            }
        });
        if(prevDone){
            setInstructions(prevInstructions =>
                prevInstructions.map((item, itemIndex) =>
                  itemIndex === index ? { ...item, completed: !item.completed } : item
                )
            );
        }else{
            toast.error("Complete the pending steps first!");
        }
    };

    useEffect(()=>{
        const areAllStepsCompleted = instructions.every(instruction => instruction.completed);
        if (areAllStepsCompleted && instructions.length > 0){
            toast.success("Recipe Completed! Enjoy your meal!");
        }
    },[instructions])

    return (
        <>
            {instructions.map((instruction) => (
                <div key={instruction.index} className="d-flex gap-2 align-items-center">
                    <label className="checkboxlabelcontainer">
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
