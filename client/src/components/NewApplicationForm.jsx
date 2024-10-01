import { useState } from "react";
import { useOutletContext } from "react-dom";

// NOTE: Ideal state is that instead of form inputs below, each form field is effectively a component that renders options based on what is in the db...
// NOTE cont... in other words, <option value=student.id name=student.first_name>, <option value=school.id, name=school.school_name)

function NewApplicationForm() {
    
    //Revisit, need to build the equivalent addApplication function on app or main.jsx; note already referenced below in row 25
    const {addFunTopic} = useOutletContext()

    // Form data reflects...
    const [formData, setFormData] = useState({
        student: "",
        school: "",
        user: "",
        user_signature:""
    })
    
    function handleSubmit(event) {
        event.preventDefault()

        const newApplication = {
            ...formData
        }

        addApplication(newApplication)

        setFormData({
            student: "",
            school: "",
            user: "",
            user_signature:""
        })
    }

    function updateApplication(event) {
        setFormData({...formData, [event.target.name]: event.target.value})
    }

    return (
        <div className="addFunTopicContainer">
            <h1 className="formheader">Submit an application!</h1>
            <form className="newApplication" onSubmit={handleSubmit} >
                <input onChange={updateApplication} value={formData.student} className="forminput" type="text" name="student" placeholder="Student"/>
                <input onChange={updateApplication} value={formData.school} className="forminput" type="text" name="school" placeholder="School"/>
                <input onChange={updateApplication} value={formData.user} className="forminput" type="text" name="user" placeholder="User"/>
                <input onChange={updateApplication} value={formData.user_signature} className="forminput" type="text" name="user_signature" placeholder="Signature"/>
  
                <button type="submit">Submit Application</button>
            </form>
        </div>
    )
}

export default NewApplicationForm;