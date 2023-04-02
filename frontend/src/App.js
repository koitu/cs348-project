import './App.css';
import './view/signIn.css';
import './view/general.css'
import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { SearchView } from './view/searchWindow';
import { ProfilePage } from './view/profilePage';
import { PlayerDetailedPage } from './view/playerPage';
import { TeamDetailedPage } from './view/teamPage';
import { SignInPageView } from './view/signIn';
import { SignUpPageView } from './view/signUp';

// App view which embodies the whole UI
function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                    {/* this is the sign in page that you will be shown when you enter the site */}
                    <Route exact path="/" element={<SignInPageView/>} />
                    {/* this is the sign up page*/}
                    <Route exact path="/signup" element={<SignUpPageView/>} />
                    {/* main page that you are confronted with when starting the project */}
                    <Route exact path="/search-menu/" element={<SearchView/>} />
                    {/* Profile page for showing bookmarked players, teams and details about user */}
                    <Route path="/profile/:id" element={<ProfilePage/>} />
                    {/* <Route path="/profile/:id" element={<ProfilePage/>}/>*/}
                    <Route path="/playerPage/:id" element={<PlayerDetailedPage/>} />
                    <Route path="/teamPage/:id" element={<TeamDetailedPage/>} />
                </Routes>
            </Router>
        </div>
    );
}

export default App;
