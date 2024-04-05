import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { login } from "../auth";

type FormValues = {
  email: string;
  password: string;
};

const LoginPage = () => {
  // const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
  //   event.preventDefault();
  //   const data = new FormData(event.currentTarget);
  //   console.log({
  //     email: data.get("email"),
  //     password: data.get("password"),
  //   });

  const form = useForm<FormValues>({
    defaultValues: {
      email: "",
      password: "",
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
      email: data.email,
      password: data.password,
    };

    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    };

    fetch("http://127.0.0.1:5000/auth/login", requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log(data.access_token);
        login(data.access_token);

        navigate("/dashboard");
      })
      .catch((error) => console.log(error));

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
        <Avatar sx={{ m: 1, bgcolor: "blue" }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>
        <Box
          component="form"
          onSubmit={handleSubmit(submitForm)}
          noValidate
          sx={{ mt: 1 }}
        >
          <TextField
            margin="normal"
            fullWidth
            id="email"
            label="Email Address"
            type="email"
            autoComplete="email"
            {...register("email", {
              required: {
                value: true,
                message: "Email is required",
              },
              maxLength: {
                value: 25,
                message: "Characters over limit",
              },
              pattern: {
                value:
                  /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/,
                message: "Please enter a valid email address",
              },
            })}
            error={!!errors.email}
            helperText={errors.email?.message}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            label="Password"
            type="password"
            id="password"
            autoComplete="new-password"
            {...register("password", {
              required: "Password is required",
              minLength: {
                value: 4,
                message: "Must be at least 4 characters long",
              },
            })}
            error={!!errors.password}
            helperText={errors.password?.message}
          />
          <FormControlLabel
            control={<Checkbox value="remember" color="primary" />}
            label="Remember me"
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
          >
            Sign In
          </Button>
          <Grid container>
            <Grid item>
              <Link to={"/signup"}>Don't have an account? Sign Up</Link>
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Container>
  );
};

export default LoginPage;
