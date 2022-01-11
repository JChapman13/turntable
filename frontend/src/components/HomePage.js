import React, { Component } from "react";
import ChannelJoinPage from "./ChannelJoinPage";
import ChannelCreatePage from "./ChannelCreatePage";
import Channel from "./Channel";
import { Grid, Button, ButtonGroup, Typography } from "@material-ui/core";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }
  renderHomePage() {
    return (
      <Grid container spacing={3}>
        <Grid item xs={12} align="center">
          <Typography variant="h3" compact="h3">
            House Party
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <ButtonGroup disableElevation variant="contained" color="primary">
            <Button color="primary" to="/join" component={Link}>
              Join a Channel
            </Button>
            <Button color="secondary" to="/create" component={Link}>
              Create a Channel
            </Button>
          </ButtonGroup>
        </Grid>
      </Grid>
    );
  }
  render() {
    return (
      <>
        <Router>
          <Routes>
            <Route path="/" element={this.renderHomePage()} />
            <Route path="/join" element={<ChannelJoinPage />} />
            <Route path="/create" element={<ChannelCreatePage />} />
            <Route path="/channel/:channelCode" element={<Channel />} />
          </Routes>
        </Router>
      </>
    );
  }
}
