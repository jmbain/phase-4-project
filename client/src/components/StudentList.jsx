import Student from "./StudentCard"

import { useOutletContext } from "react-dom";

function StudentList() {
    
    const {students, currentUser} = useOutletContext() // This imports the list of components to be rendered, in this case should be students
    
    //This filters student list depending on who the logged in user is
    const myStudents = students.filter(student => {
        return student.user === currentUser
    })
    // This displays Application components via a map of the student list
    const studentComponents = myStudents.map(student => {
        
        return <Student key={student.id} student_fn={student.first_name} student_ln={student.last_name} />
    })
    
    return (
        <div>
             <ol className="student-list">{studentComponents}</ol>
        </div>
       
    )
}

export default StudentList;