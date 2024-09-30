import { Link } from "react-dom";

function Student({student}) {
    
    
    return (
        <li className="student">
            <Link to={`students/${student.id}`} replace>{student.first_name} {student.last_name} </Link>
        </li>
    )
}

export default Student;