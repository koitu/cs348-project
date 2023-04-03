import "./profilePage.css";
import React, { useState, useEffect} from "react"
import { Link } from "react-router-dom"
import { proxyPrefix, userCookieName } from "./constant";

const ProfileTeamCard = ({ teamName, logoUrl, teamId }) => {
    async function handleDelete(e) {
        const deleteData = async () => {
            try {
                const userId = sessionStorage.getItem(userCookieName)
                const deleteResponse = await fetch(`${proxyPrefix}api/users/${userId}/teams`, {
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        title: 'deleting tean from user favourite list',
                        team_id: teamId
                    })
                })
                const deleteData = await deleteResponse.json()
                console.log(deleteData)
            } catch(error) {
                console.log(error)
            }
        }
        deleteData()
    }
    return (
      <div className="player-card primaryColor">
        <img src={logoUrl} alt={`${teamName}'s logo`} className="player-logo" />
        <div className="player-details">
            <Link to={`/teamPage/${teamId}`}> <h4>{teamName}</h4> </Link>
        </div>
        <form onSubmit={handleDelete}><button className="remove-button">Remove</button></form>
      </div>
    );
};

const ProfilePlayerCard = ({ playerName, logoUrl, playerId }) => {
    async function handleDelete(e) {
        const deleteData = async () => {
            try {
                const userId = sessionStorage.getItem(userCookieName)
                const deleteResponse = await fetch(`${proxyPrefix}api/users/${userId}/players`, {
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        title: 'deleting player from user favourite list',
                        player_id: playerId
                    })
                })
                const deleteData = await deleteResponse.json()
                console.log(deleteData)
            } catch(error) {
                console.log(error)
            }
        }
        deleteData()
    }
    return (
      <div className="player-card primaryColor">
        <img src={logoUrl} alt={`${playerName}'s logo`} className="player-logo" />
        <div className="player-details">
            <Link to={`/playerPage/${playerId}`}> <h4>{playerName}</h4> </Link>
        </div>
        <form onSubmit={handleDelete}><button className="remove-button">Remove</button></form>
      </div>
    );
};


export function ProfilePage() {
    let [ user, setUser ] = useState({})
    let [ followedPlayers, setFollowedPlayers ] = useState([])
    let [ followedTeams, setFollowedTeams ] = useState([])
    useEffect(()=> {
        const fetchData = async () => {
            try {
                const userId = sessionStorage.getItem(userCookieName)
                const userResponse = await fetch(`${proxyPrefix}api/users/${userId}`)
                const userData = await userResponse.json()
                setUser(userData)

                const playersResponse = await fetch(`${proxyPrefix}api/users/${userId}/players`)
                const playerData = await playersResponse.json()
                setFollowedPlayers(playerData["players"])

                const teamsResponse = await fetch(`${proxyPrefix}api/users/${userId}/teams`)
                const teamsData = await teamsResponse.json()
                setFollowedTeams(teamsData["teams"])

            } catch(error) {
                console.error(error)
            }
        }
        fetchData()
    }, [])
    return (
        <div className="user-profile">
            <Link to="/search-menu" className="home-button">Home</Link>
            <div className="profile-section primaryColor">
                <img src={user["profile_pic"]} alt={`${user["username"]}'s profile`} className="profile-picture" />
                <div className="user-details">
                    <h2>{user["username"]}</h2>
                    <h4>{user["fullname"]}</h4>
                    {/* <button className="profile-button">Customize</button> */}
                </div>
            </div>
            <div className="followed-section secondaryColor">
                <h2 style={{background: "white"}}>Followed Players</h2>
                <div className="followed-players">
                {followedPlayers.map((player, index) => (
                    <ProfilePlayerCard key={index}  playerName={player["player_name"]} position={player["position"]} logoUrl={player["picture"]} playerId={player["player_id"]}/>
                ))}
                </div>
            </div>
            <div className="followed-section secondaryColor">
                <h2 style={{background: "white"}}>Followed teams</h2>
                <div className="followed-teams">
                {followedTeams.map((team, index) => (
                    <ProfileTeamCard key={index}  teamName={team["team_name"]} logoUrl={team["logo_url"]} teamId={team["team_id"]}/>
                ))}
                </div>
            </div>
        </div>  
    )
}
