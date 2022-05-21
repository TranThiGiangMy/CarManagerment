import axios from "axios"

export let endpoints = {
    "categories": "/catogories/",
    "routes" : "/routes/"
}

export default axios.create({
    baseURL : "http://127.0.0.1:8000/"
})