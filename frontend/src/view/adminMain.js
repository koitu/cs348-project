import "./adminMain.css";
import React, { useState, useEffect } from "react"
import { DataGrid } from "@material-ui/data-grid";
import { TextField } from "@material-ui/core";
import { Link } from "react-router-dom"
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import { proxyPrefix, adminCookieName } from "./constant"

function CustomDataGrid({ rows, columns }) {
    const [searchText, setSearchText] = useState("");

    const handleSearchTextChange = (event) => {
        setSearchText(event.target.value);
    };

    const filteredRows = rows.filter((row) => {
        return row.id.toString()
        .includes(searchText.toLowerCase());
    });

    return (
        <div>
        <TextField
            label="Search"
            variant="outlined"
            value={searchText}
            onChange={handleSearchTextChange}
        />
        <div style={{ height: 500, width: "100%" }}>
            <DataGrid rows={filteredRows} columns={columns} />
        </div>
        </div>
    );
}

export function AdminPage() {
    const [players, setPlayers] = useState([]);
    const [teams, setTeams] = useState([]);
    const [users, setUsers] = useState([]);
    const [matches, setMatches] = useState([])

    const playerColumns = [
        { field: "player_id", headerName: "ID", width: 100 },
        { field: "player_name", headerName: "Name", width: 150 },
        { field: "nationality", headerName: "Nationality", width: 150 },
        { field: "position", headerName: "Position", width: 150 },
        { field: "height", headerName: "Height", width: 150 },
        { field: "weight", headerName: "Weight", width: 150 },
        { field: "birthday", headerName: "Birthday", width: 150 },
        {
            field: 'zzzz',
            headerName: ' ',
            width: 150,
            renderCell: (params) => (
              <button variant="contained" onClick={async () => {
                const data = params.row
                const deleteResponse = await fetch(`${proxyPrefix}/api/players/${data.id}` ,{
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        title: 'deleting team from database'
                    })
                });
                const deleteData = await deleteResponse.json();
                console.log(deleteData)
                const adminId = sessionStorage.getItem(adminCookieName)
                const Getresponse = await fetch(`${proxyPrefix}/api/players/all?id=${adminId}`);
                const Getdata = await Getresponse.json();
                const playersWithIds = Getdata.players.map((player) => ({ ...player, id: player.player_id }));
                setPlayers(playersWithIds);
              } }>
                Delete
              </button>
            ),
        },
    ];
      
    const teamColumns = [
        { field: "team_id", headerName: "ID", width: 100 },
        { field: "team_name", headerName: "Name", width: 200, flex: 1},
        { field: "logo_url", headerName: "Logo", width: 200 },
        { field: "since", headerName: "Founded", width: 150 },
        { field: "abbrv", headerName: "Abbrv", width: 150 },
        {
            field: 'zzzz',
            headerName: ' ',
            width: 150,
            renderCell: (params) => (
                
              <button variant="contained" onClick={async () => {
                const data = params.row
                const deleteResponse = await fetch(`${proxyPrefix}/api/teams/${data.id}` ,{
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        title: 'deleting team from database'
                    })
                });
                const deleteData = await deleteResponse.json();
                console.log(deleteData)
                const adminId = sessionStorage.getItem(adminCookieName)
                const Getresponse = await fetch(`${proxyPrefix}/api/teams/all?id=${adminId}`);
                const Getdata = await Getresponse.json();
                const teamsWithIds = Getdata.teams.map((team) => ({ ...team, id: team.team_id }));
                setTeams(teamsWithIds);
              }}>
                Delete
              </button> 
            ),
        },
    ];
      
    const userColumns = [
        { field: "account_id", headerName: "ID", width: 100 },
        { field: "username", headerName: "Username", width: 200, flex: 1 },
        { field: "email", headerName: "Email", width: 250 },
        { field: "profile_pic", headerName: "logo_url", width: 200 },
        {
            field: 'user_id',
            headerName: ' ',
            width: 150,
            renderCell: (params) => (
                !params.row.is_admin ?
              <button variant="contained" onClick={async () => {
                const data = params.row
                const userResponse = await fetch(`${proxyPrefix}/api/users/${data.id}` ,{
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        title: 'deleting user from database'
                    })
                });
                const deleteData = await userResponse.json();
                console.log(deleteData)
                const adminId = sessionStorage.getItem(adminCookieName)
                const Getresponse = await fetch(`${proxyPrefix}/api/users/all?id=${adminId}`);
                const Getdata = await Getresponse.json();
                const usersWithIds = Getdata.users.map((user) => ({ ...user, id: user.account_id }));
                setUsers(usersWithIds);

              }}>
                Delete
              </button> : null
            ),
        },
        {
            field: 'zz',
            headerName: ' ',
            width: 150,
            renderCell: (params) => (
                !params.row.is_admin ?
              <button variant="contained" onClick={async () => {
                console.log("started request for promotion")
                const data = params.row
                const response = await fetch(`${proxyPrefix}/api/users/${data.id}/promote`);
                const promoteData = await response.json();
                console.log(promoteData)
                const adminId = sessionStorage.getItem(adminCookieName)
                const Getresponse = await fetch(`${proxyPrefix}/api/users/all?id=${adminId}`);
                const Getdata = await Getresponse.json();
                const usersWithIds = Getdata.users.map((user) => ({ ...user, id: user.account_id }));
                setUsers(usersWithIds);
              }}>
                Promote To admin
              </button> : null
            ),
        },
    ];
    
    useEffect(() => {
        const fetchPlayers = async () => {
            const adminId = sessionStorage.getItem(adminCookieName)
            const response = await fetch(`${proxyPrefix}/api/players/all?id=${adminId}`);
            const data = await response.json();
            const playersWithIds = data.players.map((player) => ({ ...player, id: player.player_id }));
            setPlayers(playersWithIds);
        };

        const fetchTeams = async () => {
            const adminId = sessionStorage.getItem(adminCookieName)
            const response = await fetch(`${proxyPrefix}/api/teams/all?id=${adminId}`);
            const data = await response.json();
            const teamsWithIds = data.teams.map((team) => ({ ...team, id: team.team_id }));
            setTeams(teamsWithIds);
        };

        const fetchUsers = async () => {
            const adminId = sessionStorage.getItem(adminCookieName)
            const response = await fetch(`${proxyPrefix}/api/users/all?id=${adminId}`);
            const data = await response.json();
            console.log(data)
            const usersWithIds = data.users.map((user) => ({ ...user, id: user.account_id }));
            setUsers(usersWithIds);
        };

        const fetchMatches = async () => {
            const adminId = sessionStorage.getItem(adminCookieName)
            const response = await fetch(`${proxyPrefix}/api/users/all?id=${adminId}`);
            const data = await response.json();
            setMatches(data["matches"]);
        }

        fetchPlayers();
        fetchTeams();
        fetchUsers();
        fetchMatches();
    }, []);
    return (
        <div className="secondaryColor">
            <Link to="/search-menu" className="home-button">Home</Link>
            <Tabs>
                <TabList>
                    <Tab>Players</Tab>
                    <Tab>Teams</Tab>
                    <Tab>Users</Tab>
                </TabList>
                <TabPanel>
                    <div className="primaryColor" style={{ height: 600, width: "100%" }}>
                        <CustomDataGrid rows={players} columns={playerColumns} />
                    </div> 
                </TabPanel>
                <TabPanel>
                    <div className="primaryColor" style={{ height: 600, width: "100%" }}>
                        <CustomDataGrid rows={teams} columns={teamColumns} />
                    </div>    
                </TabPanel>
                <TabPanel>
                    <div className="primaryColor" style={{ height: 600, width: "100%" }}>
                        <CustomDataGrid rows={users} columns={userColumns} />
                    </div>    
                </TabPanel>
            </Tabs>
        </div>
    )
}
