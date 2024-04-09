import React, { useEffect, useState } from "react";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Divider from "@mui/material/Divider";
import ServerList from "./ServerList";
import Typography from "@mui/material/Typography";

const ListItems = () => {
  const [server, setServer] = useState([]);

  const token = JSON.parse(localStorage.getItem("REACT_TOKEN_AUTH_KEY")!);

  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  };

  useEffect(() => {
    fetch("http://127.0.0.1:5000/server/", requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setServer(data[0].title);
      })
      .catch((error) => console.log(error));
  }, []);

  return (
    <div>
      {server.map((server) => (
        <Typography>{server}</Typography>
      ))}
    </div>
  );
};

export default ListItems;
