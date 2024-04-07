import React from "react";
//import AddCircleIcon from '@mui/icons-material/AddCircle';
import { AddCircle } from "@mui/icons-material";
import { Button } from "@mui/material";

const AddItemButton = () => {
  return (
    <Button variant="contained" startIcon={<AddCircle />}>
      Add Server
    </Button>
  );
};

export default AddItemButton;
