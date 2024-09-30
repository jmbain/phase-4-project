import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ApplicantNavBar from './components/ApplicantNavbar'
import { Outlet } from 'react-dom'

function App() {
  //Initial app-level states
  const [count, setCount] = useState(0) // Came with vite set up
  const [searchText, setSearchText] = useState("")
  const [selectedFilter, setSelectedFilter] = useState("All")
  const [applications, setApplications] = useState([])
  const [schools, setSchools] = useState([])
  const [students, setStudents] = useState([])
  const [currentUser, setCurrentUser] = useState("")

  //Initial filter logic using applications as an example
  const filteredApplications = applications.filter(application => {
    if(selectedFilter=="All") {
      return application
    }
    return application.filter === selectedFilter
  })

  //Initial search logic using schools and applications as an example
  const searchedSchools = schools.filter(school => {
    return school.school_name.toUpperCase().includes(searchText.toUpperCase())
  })

  const searchedApplications = applications.filter(application => {
    return application.school.school_name.toUpperCase().includes(searchText.toUpperCase())
  })

  // Not sure if still need, but assuming for now this will be replaced by the loaders...
  useEffect(() => {
    fetch("http://localhost:4242/schools")
    .then(r = r.json())
    .then(schoolData => setSchools(schoolData))
    }
    ,[]
  )

  useEffect(() => {
    fetch("http://localhost:4242/students")
    .then(r = r.json())
    .then(studentData => setStudents(studentData))
    }
    ,[]
  )

  useEffect(() => {
    fetch("http://localhost:4242/applications")
    .then(r = r.json())
    .then(applicationData => setApplications(applicationData))
    }
    ,[]
  )

  //Front End CRUD Operations
  function addStudent() {

  }

  function updateStudent() {

  }

  function addApplication() {

  }

  function deleteApplication() {

  }

  return (
    <>
      <div>
        <Header />
        <ApplicantNavBar />
        <Outlet />
      </div>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
