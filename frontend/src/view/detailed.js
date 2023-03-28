import React, { useState, useEffect } from "react"
import { useParams, Link } from "react-router-dom"
import './App.css';
var proxyPrefix = "http://127.0.0.1:5000/"

function MatchPerformanceView(props) {
    return (
        <div className="hbox primaryColor last5Match">
            <div className="vbox matchResultLeft">
                <p className="matchLabels secondaryColor"> first team name</p>
                <img src="https://cdn.logojoy.com/wp-content/uploads/2018/05/30161636/1234-768x591.png" className="teamLogo"></img>
                <p className="matchLabels secondaryColor"> VS </p>
                <img src="https://cdn.dribbble.com/users/713893/screenshots/14307855/media/29fa5f962e03f9b4ae6f29d0bcbe5eb4.jpg?compress=1&resize=400x300" className="teamLogo"></img>
                <p className="matchLabels secondaryColor"> second team name</p>
            </div>
            
            <div className="vbox">
                <p className="matchLabels secondaryColor"> number of goals scored</p>
                <p className="matchLabels secondaryColor"> random stat 1 </p>
                <p className="matchLabels secondaryColor"> random stat 2 </p>
            </div>

        </div>
    )
}


export function PlayerDetailedPage() {
    let { id } = useParams()
    var [player, playerSet] = useState({})
    var [teams, teamsSet] = useState([])
    var [matches, matchesSet] = useState([])
    useEffect(() => {
        const fetchData = async () => {
            try {
                const playerResponse = await fetch(`${proxyPrefix}/api/players/${id}`);
                const playerData = await playerResponse.json();
                playerSet(playerData);
    
                const teamsResponse = await fetch(`${proxyPrefix}/api/teams/played?player_id=${id}`);
                const teamsData = await teamsResponse.json();
                teamsSet(teamsData["teams"]);
    
                const matchesResponse = await fetch(`${proxyPrefix}/api/players/${id}/recent/matches`);
                const matchesData = await matchesResponse.json();
    
                const matchPromises = matchesData["matches"].map(async (match) => {
                    const homeResponse = await fetch(`${proxyPrefix}/api/teams/${match["team_home_id"]}`);
                    const homeData = await homeResponse.json();
    
                    const awayResponse = await fetch(`${proxyPrefix}/api/teams/${match["team_away_id"]}`);
                    const awayData = await awayResponse.json();
    
                    return {
                        ...match,
                        home_logo: homeData["logo"],
                        home_team_name: homeData["team_name"],
                        away_logo: awayData["logo"],
                        away_team_name: awayData["team_name"],
                    };
                });
    
                const newData = await Promise.all(matchPromises);
                matchesSet(newData);
            } catch (err) {
                console.error(err);
            }
        };
    
        fetchData();
    }, []);
    console.log(matches)
    let redirectUrl = "/team/"
    return (
        <div className="fullWidth vbox">
            <div className="secondaryColor" id="detailedPage">
                <img src={player.picture } id="detailedImage"/>
                <p id="playerFullName" className="primaryColor gridText">
                    { player.player_name }
                </p>
                <p id="PlayerHeight" className="primaryColor gridText">
                    Height : {player.height}cm
                </p>
                <p id="PlayerAge" className="primaryColor gridText">
                    Born: {player.birthday}
                </p>
                <p id="Nationality" className="primaryColor gridText">
                    Nationality : {player.nationality}
                </p>
                <p id="Position" className="primaryColor gridText">
                    Position : {player.position}
                </p>
                <p id="PlayedTeams" className="primaryColor gridText">
                    { teams.map((obj, _) => (<Link to={redirectUrl + "t1"} key={obj.team_id}> {obj.team_name + ", "}</Link>))}
                </p>
            </div>
            <div id="last5Match" className='scrollable secondaryColor'> 
                { matches.map((obj, _) => (
                <div className="hbox primaryColor last5Match" key={obj["match_id"]}>
                        <p className="matchLabels secondaryColor"> {obj["home_team_name"]}</p>
                        <img src={obj["home_logo"]} className="teamLogo"></img>
                        <p className="matchLabels secondaryColor"> VS </p>
                        <img src={obj["away_logo"]} className="teamLogo"></img>
                        <p className="matchLabels secondaryColor"> {obj["away_team_name"]}</p>
                    
                    <div className="vbox">
                        <p className="matchLabels secondaryColor"> number of goals scored</p>
                        <p className="matchLabels secondaryColor"> season: {obj["season"]}</p>
                        <p className="matchLabels secondaryColor"> date: {obj["date"]}</p>
                    </div>
                </div>
                )) } 
            </div>
        </div>
    )
}

export function TeamDetailedPage() {
    let { id } = useParams()
    return (
        <p>
            this is detailed webpage for team with {id}
        </p>
    )
}