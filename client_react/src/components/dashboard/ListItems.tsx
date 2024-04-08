import React from "react";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";

const ListItems = () => {
  return (
    <List>
      <ListItem disablePadding>
        <ListItemButton>
          <ListItemText primary="NGINX Server" />
        </ListItemButton>
      </ListItem>
    </List>
  );
};

export default ListItems;
