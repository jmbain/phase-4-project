import SchoolCard from "./SchoolCard";
import { useOutletContext } from "react-dom";

function SchoolList() {
    
    const {schools} = useOutletContext() // This imports the list of components to be rendered, in this case should be schools
    
    // This displays Application components via a map of the application list
    const schoolComponents = schools.map(school => {
        
        return <SchoolCard key={school.id} />
    })
    
    return (
        <div>
             <ol className="school-list">{schoolComponents}</ol>
        </div>
       
    )
}

export default SchoolList;