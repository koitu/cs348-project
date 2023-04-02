import './general.css';
import './searchWindow.css';
import './playerPage.css';
import React, { useState, useEffect } from "react"
import {Link} from "react-router-dom"
import { ListButton } from "./ListItemButton"
import 'react-tabs/style/react-tabs.css';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import { SideBar } from "./sideBar"
import { proxyPrefix, userCookieName } from "./constant"



const TopCorner = () => {
    let [ userId, setUser] = useState("")
    useEffect(() => {
        const currentUser = sessionStorage.getItem(userCookieName)
        setUser(currentUser)
    }, [])
    return (
        <Link to={`/profile/${userId}`}>
            <button className='topCorner paddedButton primaryColor' id='profileButton'>
                <img src='defaultProfile.jpg' className='normalImage' alt="defaultProfile.jpg"/>
            </button>
        </Link>
    )
}



export const SearchView = () => {
    const [playervalues, setPValue] = useState([]);
    const [teamValues, setTValue] = useState([]);
    var [textState, setText] = useState("")

    const handleChange = (event) => {
        setText(event.target.value)
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        fetch(`${proxyPrefix}api/players?name=${textState}`)
        .then(response => response.json())
        .then(data => setPValue(data["players"]))
        .catch (error => {
            console.error(error)
        })
        fetch(`${proxyPrefix}api/teams?name=${textState}`)
        .then(response => response.json())
        .then(data => {
            setTValue(data["teams"])
            console.log(data)
        })
        .catch (error => {
            console.error(error)
        })
    };

    return (
        <header id="mainPage">
            <TopCorner/>    
            <SideBar/>
            <div className="vbox scrollable" id="searchBar">
                <div>
                    <form onSubmit={handleSubmit}>
                        <input className='primaryColor' id="textSearchInput" autoComplete="off" type="text" value={textState} onChange={handleChange} />
                        <button className='primaryColor' id="textSearchButton" type="submit"> Submit </button>
                    </form>
                </div>
                <div className='secondaryColor' id='searchResultScroll'> 
                    <Tabs>
                        <TabList>
                            <Tab>Players</Tab>
                            <Tab>Teams</Tab>
                        </TabList>
                        <TabPanel>
                            { playervalues.map((obj, _) => (<ListButton key={obj.player_id} name={obj.player_name} img={obj.picture} id={obj.player_id} isTeam="false"/>)) } 
                        </TabPanel>
                        <TabPanel>
                            { teamValues.map((obj, _) => (<ListButton key={obj.team_id} name={obj.team_name} img={obj.logo_url} id={obj.team_id} isTeam="true"/>)) }
                        </TabPanel>
                    </Tabs>
                </div>
            </div>
        </header>
    );
};

