import React from "react"
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
              "match_id" : "m123",
              "Goals" : "34",
              "img" : "https://cdn-icons-png.flaticon.com/512/5900/5900536.png"},
            { "first_team": "TeamB",
              "second_team": "TeamC",
              "match_id" : "m124",
              "Goals" : "34",
              "img" : "https://cdn-icons-png.flaticon.com/512/5900/5900536.png"},
              
        ]
    }

    const response =  fetch(proxyPrefix + "/api/players/" + id)
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        // Handle any errors
    });
    let redirectUrl = "/team/"
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
                    { teams.map((obj, _) => (<Link to={redirectUrl + "t1"}> {obj + ", "}</Link>))}
                </p>
            </div>
            <div id="last5Match" className='scrollable secondaryColor'> 
                { mathces.matches.map((obj, _) => (<div key={obj.match_id}> <MatchPerformanceView/></div>)) } 
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