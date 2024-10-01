import { Link } from "react-dom";

function SchoolCard({school}) {
    
    
    return (
        <li className="school">
            <Link to={`schools/${school.id}`} replace>{school.school_name} </Link>
        </li>
    )
}

export default SchoolCard;