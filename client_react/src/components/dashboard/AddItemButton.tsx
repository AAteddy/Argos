import React from "react";
//import AddCircleIcon from '@mui/icons-material/AddCircle';
import { AddCircle } from "@mui/icons-material";
import { Button } from "@mui/material";
import { Link } from "react-router-dom";

const AddItemButton = () => {
  return (
    <Button variant="contained" startIcon={<AddCircle />}>
      <Link to={"/server"}></Link>
      Add Server
    </Button>
  );
};

export default AddItemButton;
