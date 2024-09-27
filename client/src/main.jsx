import { StrictMode } from 'react'
import { createRoot, ReactDOM } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import {userLoader, applicationsLoader} from './Loaders.js'
import {createBrowserRouter, RouterProvider} from 'react-router-dom'
import ErrorPage from './components/ErrorPage.jsx'
import Home from './components/Home.jsx'
import Login from './components/Login.jsx'
import Logout from './components/Logout.jsx'
import ApplicationEdit from './components/ApplicationEdit.jsx'
import ApplicationReview from './components/ApplicationReview.jsx'


const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement: <ErrorPage />,
    loarder: userLoader,
    children: [
      {
        path:'/',
        element: <Home />
      },
      {
        path: '/login',
        element: <Login />
      },
      {
        path: '/logout',
        element: <Logout />
      },
      {
        path: '/edit/applications/:id',
        element: <ApplicationEdit />,
        loader: applicationsLoader
      },
      {
        path: '/review/applications/:id',
        element: <ApplicationReview />,
        loader: applicationsLoader
      },
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
