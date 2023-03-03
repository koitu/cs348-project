import './view/App.css';
import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { MainPage } from './view/main';
import { ProfilePage } from './view/prof';
import { TeamDetailedPage, PlayerDetailedPage } from "./view/detailed"
// var proxyPrefix = "http://127.0.0.1:5000/"

// App view which embodies the whole UI
function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                    {/* main page that you are confronted with when starting the project */}
                    <Route exact path="/" element={<MainPage/>} />
                    {/* Profile page for showing bookmarked players, teams and details about user */}
                    {/* later this should be changed such that it checks for user Auth */}
                    <Route path="/profile" element={<ProfilePage/>} />
                    {/* <Route path="/profile/:id" element={<ProfilePage/>}/>*/}

                    {/* to be implemented later, for showing detailed */}
                    <Route path="/playerDetailedPage/:id" element={<PlayerDetailedPage/>} />
                    <Route path="/teamDetailedPage/:id" element={<TeamDetailedPage/>} />
                </Routes>
            </Router>
        </div>
    );
}

export default App;
