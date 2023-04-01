import React from "react"
import { Link } from "react-router-dom";
export const defaultImageAddress = "https://img.pixers.pics/pho_wat(s3:700/FO/64/21/20/79/700_FO64212079_8f6802066158ebb7b77002c063607ae6.jpg,700,700,cms:2018/10/5bd1b6b8d04b8_220x50-watermark.png,over,480,650,jpg)/posters-vector-football-soccer-player-silhouette-with-ball-isolated.jpg.jpg"


export function ListButton (props) {
    let redirectUrl = "/playerPage/"
    if (props.isTeam === "true") {
        redirectUrl = "/teamPage/"
    }
    return ( 
        <Link to={redirectUrl + props.id}>
            <button className="listButton primaryColorClickable">
                <div className="listContainer">
                    <img src={props.img} className="listImage" alt={defaultImageAddress}></img>
                    <div>
                    <h1>
                        {props.name}
                    </h1>
                    <p>details about the player</p>
                    </div>
                </div>
            </button>
        </Link>
        
    )
} 