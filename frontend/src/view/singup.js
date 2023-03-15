import "./App.css"
import React from "react"
import { useNavigate, Link } from "react-router-dom"

export function SingUpPage() {
    const navigate = useNavigate()

    const handleSubmit = event => {
        event.preventDefault();

        navigate("/")
    }
    return (
        <div className="vbox secondaryColor signInBox">
            <form onSubmit={handleSubmit}>
                <input placeholder="User Name" className="signInItem"/>
                <input placeholder="Password" className="signInItem"/>
                <input placeholder="repeat Password" className="signInItem"/>
                <button type="submit" className="signInItem"> Sign in</button>
            </form>
        </div>
    )
}