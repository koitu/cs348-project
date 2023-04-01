import "./signUp.css"
import "./signIn.css"
import React, { useState } from "react"
import { useNavigate } from "react-router-dom"
import { proxyPrefix } from "./constant"

export function SignUpPageView() {
    let navigate  = useNavigate()
    let [usernameTextState, setUserame] = useState("")
    let [passTextState, setPassword] = useState("")
    let [passRepeatTextState, setPasswordRepeat] = useState("")
    let [emailTextState, setEmail] = useState("")
    let [fullnameState, setFullname] = useState("")
    const handleSubmit = event => {
        event.preventDefault();
        if (passRepeatTextState !== passTextState) {
            alert("Please Repeat your password correctly")
        } else {
            fetch(`${proxyPrefix}/api/users/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    title: 'new User sign up',
                    username: usernameTextState,
                    password: passTextState,
                    fullname: fullnameState,
                    email: emailTextState
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data['status'] === "OK") {
                    navigate("/")
                } else {
                    switch(data['error']) {
                        case 'username':
                            alert("a user with this username already exists")
                            break;
                        case 'email':
                            alert("a user with this email already exits")
                            break;
                        default:
                            alert("there was a problem trying to create your account")
                            break;
                    }
                }
            })
        }
    }
    const handlePassChange = (event) => { setPassword(event.target.value) }
    const handlePassRepeatChange = (event) => { setPasswordRepeat(event.target.value) }
    const handleUsernameChange = (event) => { setUserame(event.target.value) }
    const handleFullnameChange = (event) => { setFullname(event.target.value) }
    const handleEmailChange = (event) => { setEmail(event.target.value) }

    return (
        <div className="secondaryColor" id="signUpBox">
            <form onSubmit={handleSubmit}>
                <input  placeholder="User Name" className="signInItem signUpItem1" onChange={handleUsernameChange}/>
                <input placeholder="Fullname" className="signInItem signUpItem2" onChange={handleFullnameChange}/>
                <input placeholder="Email" className="signInItem signUpItem13" onChange={handleEmailChange}/>
                <input type='password' placeholder="Password" className="signInItem signUpItem4" onChange={handlePassChange}/>
                <input type='password' placeholder="repeat Password" className="signInItem signUpItem5" onChange={handlePassRepeatChange}/>
                <button type="submit" className="signInItem signUpItem6"> Sign Up</button>
            </form>
        </div>
    )
}