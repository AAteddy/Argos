import * as React from "react";
import Navbar from "./components/landing_page/Navbar";

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Home } from "@mui/icons-material";
import Login from "./pages/LoginPage";
import Signup from "./pages/SignupPage";

const App = () => {
  return (
    <Router>
      <div>
        <Navbar />
        <Switch>
          <Route path="/Login">
            <Login />
          </Route>
          <Route path="/Signup">
            <Signup />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

export default App;
