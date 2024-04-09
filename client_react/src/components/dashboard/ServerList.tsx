import Divider from "@mui/material/Divider";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import React from "react";

const ServerList = ({ title: any }) => {
  return (
    <>
      <List>
        <ListItem disablePadding>
          <ListItemButton>
            <ListItemText primary={title} />
          </ListItemButton>
        </ListItem>
      </List>
      <Divider />
    </>
  );
};

export default ServerList;
