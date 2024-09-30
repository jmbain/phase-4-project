import { NavLink } from "react-router-dom";

function NavBar() {
    return (
        <nav className="navbar">
            <NavLink to="/home">Home</NavLink>
            <NavLink to="/applications">Applications</NavLink>
            <NavLink to="/forms">Forms</NavLink>
            <NavLink to="/login">Login</NavLink>
            <NavLink to="/">Logout</NavLink>
        </nav>
    )
}

export default NavBar;