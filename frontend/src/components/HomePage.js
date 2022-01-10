import React, { Component } from "react";
import ChannelJoinPage from "./ChannelJoinPage";
import ChannelCreatePage from "./ChannelCreatePage";
import Channel from "./Channel";
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
  render() {
    return (
      <>
        <Router>
          <Routes>
            <Route path="/" element={<p>This is the homepage</p>} />
            <Route path="/join" element={<ChannelJoinPage />} />
            <Route path="/create" element={<ChannelCreatePage />} />
            <Route path="/channel/:channelCode" element={<Channel />} />
          </Routes>
        </Router>
      </>
    );
  }
}
