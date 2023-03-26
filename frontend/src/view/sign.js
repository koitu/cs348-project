import "./App.css"
import React from "react"
import { useState } from "react"
import { useNavigate, Link } from "react-router-dom"
import { proxyPrefix } from "./values"

export function SignInPageView() {
    const navigate = useNavigate()
    var [usernameTextState, setUserame] = useState("")
    var [passTextState, setPassword] = useState("")
    const handleSubmit = async event => {
        event.preventDefault();
        // const response = await fetch(proxyPrefix + "/api/users", {
        //     method: "GET",
        //     mode: "cors",
        //     cache: "no-cache",
        //     username: usernameTextState
        // })
        // .catch(err => {

        // })
        // const data = await response.json();

        // console.log(data)
        
        if (true) {
            navigate("/main")
        } else {
            alert(" Wrong Password or username")
        }
    }

    const handlePassChange = (event) => {
        setPassword(event.target.value)
    }

    const handleNameChange = (event) => {
        setUserame(event.target.value)
    }
    return (
        <div className="vbox secondaryColor signInBox">
            <form onSubmit={handleSubmit}>
                <input placeholder="User Name" className="signInItem" onChange={handleNameChange}/>
                <input placeholder="Password" className="signInItem" onChange={handlePassChange}/>
                <button type="submit" className="signInItem"> Sign in</button>
            </form>
                <label className="primaryColor signInItem"> Don't have a account  Yet? create one:</label>
            <Link to="/signup">
                <button className="signInItem">
                    Sign up
                </button>
            </Link>
        </div>
    )
}
