import { Link } from "react-dom";

function Application({application}) {
    
    
    return (
        <li className="application">
            <Link to={`applications/${application.id}`} replace>{application.student} {application.school} </Link>
        </li>
    )
}

export default Application;