import './playerPage.css';
import React, { useState, useEffect } from "react"
import { useParams, Link } from "react-router-dom"
import { proxyPrefix, userCookieName } from "./constant"

export function PlayerDetailedPage() {
    let { id } = useParams()
    var [player, playerSet] = useState({})
    var [teams, teamsSet] = useState([])
    var [matches, matchesSet] = useState([])
    var currentUser = ""
    useEffect(() => {
        const fetchData = async () => {
            try {
                const playerResponse = await fetch(`${proxyPrefix}/api/players/${id}`);
                const playerData = await playerResponse.json();
                playerSet(playerData);
    
                const teamsResponse = await fetch(`${proxyPrefix}/api/teams/played?player_id=${id}`);
                const teamsData = await teamsResponse.json();

                teamsSet(teamsData["teams"]);
    
                const matchesResponse = await fetch(`${proxyPrefix}/api/matches/recent/player?player_id=${id}`);
                const matchesData = await matchesResponse.json();
    
                const matchPromises = matchesData["matches"].map(async (match) => {
                    const homeResponse = await fetch(`${proxyPrefix}/api/teams/${match["team_home_id"]}`);
                    const homeData = await homeResponse.json();
    
                    const awayResponse = await fetch(`${proxyPrefix}/api/teams/${match["team_away_id"]}`);
                    const awayData = await awayResponse.json();
    
                    return {
                        ...match,
                        home_logo: homeData["logo_url"],
                        home_team_name: homeData["team_name"],
                        away_logo: awayData["logo_url"],
                        away_team_name: awayData["team_name"]
                    };
                });
    
                const newData = await Promise.all(matchPromises);
                matchesSet(newData);
            } catch (err) {
                console.error(err);
            }
        };
        fetchData();
        currentUser = sessionStorage.getItem(userCookieName)
        console.log(currentUser)
    }, []);

    function handleFavButton(e) {
        e.preventDefault();
        fetch(`${proxyPrefix}/api/users/favPlayer`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                title: 'add player to favourite players of the user',
                user_id: currentUser,
                player_id: id
            })
        })
    }
    
    return (
        <div className="fullWidth vbox">
            <div className="secondaryColor" id="detailedPage">
                <form onSubmit={handleFavButton}>
                    <button>
                        <img src="../pngwing.com.png" className="favButton"/>
                    </button>
                </form>
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
                    { teams.map((obj, _) => (<Link to={`/team/${obj.team_id}`} key={obj.team_id}> {obj.team_name + ", "}</Link>))}
                </p>
            </div>
            <div id="last5Match" className='secondaryColor'> 
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

