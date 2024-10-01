import { useOutletContext } from "react-dom";
import NewApplicationForm from "./NewApplicationForm";
import NewStudentForm from "./NewStudentForm";

function Home() {
    
    // const {topics, funTopics} = useOutletContext()
    // console.log(topics)
    // console.log((topics.length)-1)
    // console.log(topics[182].resolution)
    
    // let mostRecentTopicIndex = topics.length-1
    // const currentTopic = topics[mostRecentTopicIndex]

    // console.log(funTopics)
    // let mostRecentFunTopicIndex = funTopics.length-1
    // const currentFunTopic = funTopics[mostRecentFunTopicIndex]
    // console.log(mostRecentFunTopicIndex)
    // console.log(currentFunTopic)

    
    if(true) {
        return (
            <div className="home">
                <NewApplicationForm />
                <NewStudentForm/>
            </div>
            

        )}
}

export default Home;