import { StrictMode } from 'react'
import { createRoot, ReactDOM } from 'react-router-dom'
import App from './App.jsx'
import './index.css'
import {userLoader, applicationListLoader, studentListLoader, schoolListLoader} from './Loaders.js'
import {createBrowserRouter, RouterProvider} from 'react-dom'
import ErrorPage from './components/ErrorPage.jsx'
import Home from './components/Home.jsx'
// import Login from './components/Login.jsx'
// import Logout from './components/Logout.jsx'

import ApplicationList from './components/ApplicationList.jsx'
import StudentList from './components/StudentList.jsx'
import SchoolList from './components/SchoolList.jsx'

//___REVISIT___
// import ApplicationEdit from './components/ApplicationEdit.jsx'
// import ApplicationReview from './components/ApplicationReview.jsx'

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement: <ErrorPage />,
    loader: userLoader,
    children: [
      {
        path:'/',
        element: <Home />
      },
      // {
      //   path: '/login',
      //   element: <Login />
      // },
      // {
      //   path: '/logout',
      //   element: <Logout />
      // },
      {
        path: '/applications',
        element: <ApplicationList />,
        loader: applicationListLoader
      },
      {
        path: '/students',
        element: <StudentList />,
        loader: studentListLoader
      },
      {
        path: '/schools',
        element: <SchoolList />,
        loader: schoolListLoader
      },
      
      //_____REVISIT______ Note still need to finish SchoolList component and loader thinking
      // {
      //   path: '/edit/applications/:id',
      //   element: <ApplicationEdit />,
      //   loader: applicationsLoader
      // },
      // {
      //   path: '/review/applications/:id',
      //   element: <ApplicationReview />,
      //   loader: applicationsLoader
      // },
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
