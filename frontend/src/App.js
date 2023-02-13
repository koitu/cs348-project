import './App.css';
import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { MainPage } from './view/main';
import { ProfilePage } from './view/prof';
// var proxyPrefix = "http://127.0.0.1:5000/"


function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                    <Route exact path="/" element={<MainPage/>} />
                    <Route path="/profile" element={<ProfilePage/>} />
                </Routes>
            </Router>
        </div>
    );
}

export default App;
