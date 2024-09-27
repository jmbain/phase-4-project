async function userLoader({ request, params }) {
    const res = await fetch('/api/check_session', {
        method: 'GET',
        // credentials: 'include'
      })
      .then(resp => {
        if (resp.ok) {
          return resp.json()
        } else {
          return {}
        }
      })
    return res
  }
  
  //starting point for other loaders...
  async function applicationsLoader({ request, params }) {
    const res = await fetch("/api/applications")
      .then(resp => resp.json())
    return res
  }

  async function studentsLoader({ request, params }) {
    const res = await fetch("/api/students")
      .then(resp => resp.json())
    return res
  }