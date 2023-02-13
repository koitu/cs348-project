import '../App.css';
import React, { useState } from "react"
import {Link} from "react-router-dom"
var proxyPrefix = "http://127.0.0.1:5000/"

const TopCorner = () => {
    return (
        <Link to="/profile">
            <button className='topCorner paddedButton'>
                <img src='defaultProfile.jpg' className='normalImage' alt=""/>
            </button>
        </Link>
    )
}

export const MainPage = () => {
    const [value, setValue] = useState([]);
    var [textState, setText] = useState("")

    const handleChange = (event) => {
        setText(event.target.value)
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch(proxyPrefix + "keyword/"+ textState);
            const data = await response.json();
            setValue(data)
        } catch (error) {
        }
    };

    return (
        <header className="App-header">
            <TopCorner/>
            <div className="vbox">
                <div>
                    <form onSubmit={handleSubmit}>
                        <input id="textSearchInput" type="text" value={textState} onChange={handleChange} />
                        <button id="textSearchButton" type="submit"> Submit </button>
                    </form>
                </div>
                <div className='scrollable'> 
                    { value.map((obj, index) => <p className="paddedText">{obj}</p> ) }  
                </div>
            </div>
        </header>
    );
};
