import { NavLink } from "react-dom";

function ApplicantNavBar() {
    return (
        <nav className="navbar">
            <NavLink to="/home">Home</NavLink>
            <NavLink to="/students">My Students</NavLink>
            <NavLink to="/applications">My Applications</NavLink>
            <NavLink to="/login">Login</NavLink>
            <NavLink to="/">Logout</NavLink>
        </nav>
    )
}

export default ApplicantNavBar;