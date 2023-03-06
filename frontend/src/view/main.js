import './App.css';
import React, { useState } from "react"
import {Link} from "react-router-dom"
import { ListButton } from "./clickable"
import 'react-tabs/style/react-tabs.css';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import { SideBar } from "./sideBar"
var proxyPrefix = "http://127.0.0.1:5000/"



const TopCorner = () => {
    return (
        <Link to="/profile">
            <button className='topCorner paddedButton primaryColor'>
                <img src='defaultProfile.jpg' className='normalImage' alt="defaultProfile.jpg"/>
            </button>
        </Link>
    )
}



export const MainPage = () => {
    const [playervalues, setPValue] = useState([]);
    const [teamValues, setTValue] = useState([]);
    var [textState, setText] = useState("")

    const handleChange = (event) => {
        setText(event.target.value)
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch(proxyPrefix + "/api/players/");
            const data = await response.json();
            setPValue(data)
            setTValue()
            console.log(data)
        } catch (error) {
            
        }
    };

    return (
        <header className="App-header">
            <TopCorner/>    
            <SideBar></SideBar>
            <div className="vbox">
                <div>
                    <form onSubmit={handleSubmit}>
                        <input className='primaryColor' id="textSearchInput" type="text" value={textState} onChange={handleChange} />
                        <button className='primaryColor' id="textSearchButton" type="submit"> Submit </button>
                    </form>
                </div>
                <div className='scrollable secondaryColor' id='searchResultScroll'> 
                    <Tabs>
                        <TabList>
                            <Tab>Players</Tab>
                            <Tab>Teams</Tab>
                        </TabList>
                        
                        <TabPanel>
                            { playervalues.map((obj, _) => (<ListButton name={obj.player_name} img={obj.picture} id={obj.player_id} isTeam="false"/>)) } 
                        </TabPanel>
                        <TabPanel>
                            { teamValues.map((obj, _) => (<ListButton name={obj.team_name} img={obj.logo} id={obj.team_id} isTeam="true"/>)) }
                        </TabPanel>
                    </Tabs>
                </div>
            </div>
        </header>
    );
};
