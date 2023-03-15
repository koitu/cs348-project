import "./App.css"
import React from "react"
import { useNavigate, Link } from "react-router-dom"

export function SignInPageView() {
    const navigate = useNavigate()

    const handleSubmit = event => {
        event.preventDefault();

        navigate("/main")
    }
    return (
        <div className="vbox secondaryColor signInBox">
            <form onSubmit={handleSubmit}>
                <input placeholder="User Name" className="signInItem" />
                <input placeholder="Password" className="signInItem"/>
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
