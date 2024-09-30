import { useState } from "react";
import { useOutletContext } from "react-router-dom";


function NewStudentForm() {
    
    //Revisit, need to build the equivalent addStudent function on app or main.jsx; note already referenced below in row 25
    const {addFunTopic} = useOutletContext()

    // Form data reflects...
    const [formData, setFormData] = useState({
        first_name: "",
        last_name: "",
        dob: "",
        age: "",
        expected_grade_level: "",
        user_relationship: ""
    })
    
    function handleSubmit(event) {
        event.preventDefault()

        const newStudent = {
            ...formData
        }

        addStudent(newStudent)

        setFormData({
            first_name: "",
            last_name: "",
            dob: "",
            age: "",
            expected_grade_level: "",
            user_relationship: ""
        })
    }

    function updateStudent(event) {
        setFormData({...formData, [event.target.name]: event.target.value})
    }

    return (
        <div className="addStudentContainer">
            <h1 className="formheader">Create a New Topic!</h1>
            <form className="newStudent" onSubmit={handleSubmit} >
                <input onChange={updateStudent} value={formData.first_name} className="forminput" type="text" name="first_name" placeholder="First Name"/>
                <input onChange={updateStudent} value={formData.last_name} className="forminput" type="text" name="last_name" placeholder="Last Name"/>
                <input onChange={updateStudent} value={formData.dob} className="forminput" type="date" name="dob" placeholder="Date of Birth"/>
                <input onChange={updateStudent} value={formData.age} className="forminput" type="text" name="age" placeholder="Age"/>
                <input onChange={updateStudent} value={formData.expected_grade_level} className="forminput" type="text" name="expected_grade_level" placeholder="Expected Grade Level"/>
                <input onChange={updateStudent} value={formData.user_relationship} className="forminput" type="text" name="user_relationship" placeholder="E.g. I am this student's mother/father/etc."/> 
                <button type="submit">Add Student</button>
            </form>
        </div>
    )
}

export default NewStudentForm;