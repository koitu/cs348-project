import React from "react";
import "./App.css";
import "./sideBar.css";

export function SideBar() {

    return (
        <div className="primaryColor" id="sideBar">
            <input type="checkbox" id="pastGameCheck"/>
            <label className="sideBarText"> Have played a game in the past 365 days</label> <br></br>
            <p> Rating range </p>
            <input type="range" id="sideBarSlider"/>
            <p> Position </p>
            <select name="cars" id="cars">
                <option value="l1">L1</option>
                <option value="l2">L2</option>
                <option value="l3">L3</option>
                <option value="l4">L4</option>
            </select>
        </div>
    )
}