import React from "react";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Divider from "@mui/material/Divider";

const ListItems = () => {
  return (
    <>
      <List>
        <ListItem disablePadding>
          <ListItemButton>
            <ListItemText primary="NGINX Server" />
          </ListItemButton>
        </ListItem>
        <Divider />
        <ListItem disablePadding>
          <ListItemButton>
            <ListItemText primary="APACHE Server" />
          </ListItemButton>
        </ListItem>
      </List>
    </>
  );
};

export default ListItems;
