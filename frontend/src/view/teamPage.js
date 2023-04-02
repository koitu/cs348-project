import "./general.css";
import "./teamPage.css";
import "./profilePage.css";
import React, { useEffect , useState } from "react"
import { useParams, Link } from "react-router-dom"
import { proxyPrefix, userCookieName } from "./constant";

const PlayerCard = ({ playerName, position, logoUrl, playerId }) => {
    return (
      <div className="player-card primaryColor">
        <img src={logoUrl} alt={`${playerName}'s logo`} className="player-logo" />
        <div className="player-details">
            <Link to={`/playerPage/${playerId}`}> <h4>{playerName}</h4> </Link>
            <p>Position: {position}</p>
        </div>
      </div>
    );
};


export function TeamDetailedPage() {
    let { id } = useParams()
    let [ team, setTeam ] = useState({})
    let [ players, setPlayers ] = useState([])
    let [ addedToFav, setAdded ] = useState(false)

    useEffect(() => {
        const fetchData = async () => {
            try {
                const teamResponse = await fetch(`${proxyPrefix}api/teams/${id}`)
                const teamData = await teamResponse.json()
                setTeam(teamData)

                let currentUser = sessionStorage.getItem(userCookieName)
                const favResponse = await fetch(`${proxyPrefix}/api/teams/${id}/check-follower?account_id=${currentUser}`)
                const favData = await favResponse.json()
                if (favData["status"] === "OK") {
                    setAdded(true)
                } else {
                    setAdded(false)
                }

                const playerResponse = await fetch(`${proxyPrefix}/api/teams/${id}/players`)
                const playerData = await playerResponse.json()
                console.log(playerData)
                setPlayers(playerData["players"])

            } catch(err) {
                console.error(err);
            }
        }
        fetchData()
    }, [])

    async function handleFavButton(event) {
        event.preventDefault();
        if (addedToFav) {
            alert("this team has already been added to your favourite list of teams")
            return
        }
        let currentUser = sessionStorage.getItem(userCookieName)
        const response = await fetch(`${proxyPrefix}/api/teams/${id}/followers?account_id=${currentUser}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                title: 'add tean to favourite teams of the user',
                account_id: currentUser
            })
        })
        const data = await response.json()
        if ('status' in data) {
            if (data['status'] === "OK") {
                setAdded(true)
            }
        } else {
            console.error(data)
        }
    }
    
    return (
        <div className="team-card-container">
            <Link to="/search-menu" className="home-button">Home</Link>
            <div className="team-card primaryColor">
                <img src={team["logo_url"]} alt={`${id} logo`} className="team-logo" />
                <div className="team-details">
                    <h3>{team["team_name"]} [ {team["abbrv"]} ]</h3>
                    <p><b>Time Created:</b> {team["since"]}  </p>
                    <p><b>Location:</b> {team["location"]}</p>
                </div>
                <form onSubmit={handleFavButton}>
                    <button className='fav-button'>
                        {!addedToFav ? "add team to favourite list" : "Added!"}
                    </button>
                </form>
            </div>
            <div className="player-list secondaryColor">
                <h1 style={{background: "white"}}>Players List:</h1> <br></br>
                {players.map((player, index) => (
                    <PlayerCard key={index} playerName={player["player_name"]} position={player["position"]} logoUrl={player["picture"]} playerId={player["player_id"]}/>
                ))}
            </div>
        </div>
    )
}