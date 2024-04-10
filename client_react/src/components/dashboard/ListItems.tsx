import React, { useEffect, useState } from "react";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Divider from "@mui/material/Divider";
import ServerList from "./ServerList";
import Typography from "@mui/material/Typography";

const ListItems = ({ title: any }) => {
  return (
    <div>
      <h2>{title}</h2>
    </div>
  );
};

export default ListItems;
