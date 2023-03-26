import './view/App.css';
import './view/sign.css';
import './view/general.css'
import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { MainPage } from './view/main';
import { ProfilePage } from './view/prof';
import { TeamDetailedPage, PlayerDetailedPage } from "./view/detailed"
import { SignInPageView } from './view/sign';
import { SingUpPage } from './view/singup';
// var proxyPrefix = "http://127.0.0.1:5000/"

// App view which embodies the whole UI
function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                    {/* this is the sign in page that you will be shown when you enter the site */}
                    <Route exact path="/" element={<SignInPageView/>} />


                    {/* this is the sign up page*/}
                    <Route exact path="/signup" element={<SingUpPage/>} />



                    {/* main page that you are confronted with when starting the project */}
                    <Route exact path="/main" element={<MainPage/>} />
                
                    {/* Profile page for showing bookmarked players, teams and details about user */}
                    {/* later this should be changed such that it checks for user Auth */}
                    <Route path="/profile" element={<ProfilePage/>} />
                    {/* <Route path="/profile/:id" element={<ProfilePage/>}/>*/}

                    {/* to be implemented later, for showing detailed */}
                    <Route path="/playerPage/:id" element={<PlayerDetailedPage/>} />
                    <Route path="/teamPage/:id" element={<TeamDetailedPage/>} />
                </Routes>
            </Router>
        </div>
    );
}

export default App;
