import React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

type FormValues = {
  title: string;
  hostname: string;
  server_username: string;
  server_password: string;
  port: string;
};

const CreateServer = () => {
  const form = useForm<FormValues>({
    defaultValues: {
      title: "",
      hostname: "",
      server_username: "",
      server_password: "",
      port: "",
    },
  });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = form;

  const navigate = useNavigate();

  const submitForm = (data: FormValues) => {
    const body = {
      title: data.title,
      hostname: data.hostname,
      username: data.server_username,
      password: data.server_password,
      port: data.port,
    };

    const token = JSON.parse(localStorage.getItem("REACT_TOKEN_AUTH_KEY")!);

    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(body),
    };

    fetch("http://127.0.0.1:5000/server/", requestOptions)
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.log(error));

    navigate("/Dashboard");
    reset();
  };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Add Remote-Server credentials
        </Typography>
        <Box
          component="form"
          noValidate
          onSubmit={handleSubmit(submitForm)}
          sx={{ mt: 3 }}
        >
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <TextField
                autoComplete="title"
                fullWidth
                id="title"
                label="Server Name"
                autoFocus
                {...register("title", {
                  required: {
                    value: true,
                    message: "Server name is required",
                  },
                })}
                error={!!errors.title}
                helperText={errors.title?.message}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                autoComplete="hostname"
                fullWidth
                id="hostname"
                label="Server Hostname"
                autoFocus
                {...register("hostname", {
                  required: {
                    value: true,
                    message: "Server Hostname is required",
                  },
                })}
                error={!!errors.hostname}
                helperText={errors.hostname?.message}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                autoComplete="server_username"
                fullWidth
                id="server_username"
                label="Server Username"
                autoFocus
                {...register("server_username", {
                  required: {
                    value: true,
                    message: "Server Username is required",
                  },
                })}
                error={!!errors.server_username}
                helperText={errors.server_username?.message}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                required
                fullWidth
                label="Server Password"
                type="password"
                id="password"
                autoComplete="password"
                {...register("server_password", {
                  required: "Server Password is required",
                })}
                error={!!errors.server_password}
                helperText={errors.server_password?.message}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                required
                fullWidth
                label="Serve Port Number"
                type="port"
                id="port"
                autoComplete="server_port"
                {...register("port", {
                  required: "Server Port Number is required",
                })}
                error={!!errors.port}
                helperText={errors.port?.message}
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
          >
            Create Server
          </Button>
          <Grid container justifyContent="flex-end">
            <Grid item>
              <Link to={"/Dashboard"}>Return back to dashboard</Link>
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Container>
  );
};

export default CreateServer;
