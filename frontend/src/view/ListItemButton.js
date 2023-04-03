import React from "react"
import { Link } from "react-router-dom";


export function ListButton (props) {
    let redirectUrl = "/playerPage/"
    if (props.isTeam === "true") {
        redirectUrl = "/teamPage/"
    }
    return ( 
        <Link to={redirectUrl + props.id}>
            <button className="listButton primaryColorClickable">
                <div className="listContainer">
                    <img src={props.img} className="listImage" alt={"Team Image"}></img>
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