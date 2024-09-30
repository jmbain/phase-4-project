import Application from "./ApplicationCard"

import { useOutletContext } from "react-router-dom";

function ApplicationList() {
    
    const {quickFilterSearchTopics} = useOutletContext() // This imports the list of components to be rendered, in this case should be applications
    
    // This displays Application components via a map of the application list
    const quickTopicComponents = quickFilterSearchTopics.map(application => {
        
        return <Application key={application.id} school={application.school.school_name} student_fn={application.student.first_name} student_ln={application.student.last_name} />
    })
    
    return (
        <div>
             <ol className="application=list">{quickTopicComponents}</ol>
        </div>
       
    )
}

export default QuickTopicList;