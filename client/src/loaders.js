async function userLoader({ request, params }) {
    const res = await fetch('/api/check_session', {
        method: 'GET',
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
async function applicationListLoader({ request, params }) {
    const res = await fetch("/api/applications")
        .then(resp => resp.json())
    return res
  }

async function studentListLoader({ request, params }) {
    const res = await fetch("/api/students")
        .then(resp => resp.json())
    return res
  }

async function applicationDetailLoader({ request, params }) {
    const res = await fetch("/api/applications/${params.id}")
        .then(resp => resp.json())
    return res
  }

async function studentDetailLoader({ request, params }) {
    const res = await fetch("/api/students/${params.id}")
        .then(resp => resp.json())
    return res
  }

async function schoolListLoader({ request, params }) {
    const res = await fetch("/api/schools")
        .then(resp => resp.json())
    return res
  }

async function schoolDetailLoader({ request, params }) {
    const res = await fetch("/api/schools/${params.id}")
        .then(resp => resp.json())
    return res
  }

export {
    applicationDetailLoader,
    applicationListLoader,
    studentDetailLoader,
    studentListLoader,
    userLoader,
    schoolListLoader
}