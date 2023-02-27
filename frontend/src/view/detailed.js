import React from "react"
import { useParams } from "react-router-dom"
import './App.css';

function MatchPerformanceView(props) {

    return (
        <div className="hbox primaryColor">
            <div className="vbox">
            </div>
            <div>

            </div>
        </div>
    )
}

export function PlayerDetailedPage() {
    let { id } = useParams()
    var player = {
        "player_name": "Cristiano Ronaldo dos Santos Aveiro",
        "picture" : "https://b.fssta.com/uploads/application/soccer/headshots/885.vresize.350.350.medium.14.png",
        "height" : "1.87m",
        "weight" : "85kg",
        "nationality" : "Portugal",
        "position" : "Forward",
        "birthday": "February 5, 1985"
        
    }
    var teams = ["Manchester United	", "Real Madrid", "Juventus", "Al Nassr"]
    const mathces = {
        "matches" : [
            { "first_team": "TeamA",
              "second_team": "TeamB",
              "Goals" : "34",
              "img" : "https://cdn-icons-png.flaticon.com/512/5900/5900536.png"},
            { "first_team": "TeamB",
              "second_team": "TeamC",
              "Goals" : "34",
              "img" : "https://cdn-icons-png.flaticon.com/512/5900/5900536.png"},
              
        ]
    }

    return (
        <div className="fullWidth vbox">
            <div className="secondaryColor" id="detailedPage">
                <img src={player.picture } id="detailedImage"/>
                <p id="playerFullName" className="primaryColor gridText">
                    { player.player_name }
                </p>
                <p id="PlayerHeight" className="primaryColor gridText">
                    Height : {player.height}
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
                    { teams.map((obj, _) => (obj + ", "))}
                </p>
            </div>
            <div id="last5Match" className='scrollable secondaryColor'> 
                { mathces.matches.map((obj, _) => (<p>{obj.first_team}</p>)) } 
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