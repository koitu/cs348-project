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
            const response = await fetch(proxyPrefix + "/api/players/")
            .then ({ 

            })
            .catch (error => {
                // Handle any errors
            })
            // const data = await response.json();
            setPValue([ 
                {
                    "player_id" : "p123",
                    "player_name" : "Christiano Ronaldo",
                    "picture" : "https://b.fssta.com/uploads/application/soccer/headshots/885.vresize.350.350.medium.14.png"
                },
                {
                    "player_id" : "p230",
                    "player_name" : "Arvin Asgharin",
                    "picture" : null
                },
                {
                    "player_id" : "P450",
                    "player_name" : "Neymar da Silva Santos",
                    "picture" : "https://upload.wikimedia.org/wikipedia/commons/6/65/20180610_FIFA_Friendly_Match_Austria_vs._Brazil_Neymar_850_1705.jpg"
                },
                {
                    "player_id" : "p650",
                    "player_name" : "Lionel Messi",
                    "picture" : "https://cdn.britannica.com/35/238335-050-2CB2EB8A/Lionel-Messi-Argentina-Netherlands-World-Cup-Qatar-2022.jpg"
                },
                {
                    "player_id" : "p546",
                    "player_name" : "Shayan Mohamadi Kubji",
                    "picture" : null
                }
            ])
            setTValue([
                {
                    "team_id" : "t123",
                    "team_name" : "FC Barcelona",
                    "logo" : "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/1200px-FC_Barcelona_%28crest%29.svg.png"
                },
                {
                    "team_id" : "t340",
                    "team_name" : "Real Madrid",
                    "logo" : "https://cdn-icons-png.flaticon.com/512/5042/5042057.png"
                }
            ])
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
