import React, { Component, useState } from "react";
import { Button, Grid, Typography, TextField } from "@material-ui/core";
import { Link, useNavigate } from "react-router-dom";

function ChannelJoinPage() {
  let navigate = useNavigate();
  const [channelCode, setChannelCode] = useState("");
  const [error, setError] = useState("");

  const channelButtonClicked = () => {
    console.log(channelCode);
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        code: channelCode,
      }),
    };
    fetch("/api/join-channel/", requestOptions)
      .then((response) => {
        if (response.ok) {
          console.log("working");
          navigate("/channel" + channelCode);
        } else {
          console.log("working123");
          setError("Channel not found");
        }
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <Grid container spacing={1} align="center">
      <Grid item xs={12}>
        <Typography variant="h4" component="h4">
          Join a Channel
        </Typography>
      </Grid>
      <Grid item xs={12}>
        <TextField
          label="Code"
          placeholder="Enter a Channel Code"
          helperText={error}
          errormsg={error}
          value={channelCode}
          variant="outlined"
          onChange={(e) => setChannelCode(e.target.value)}
        />
      </Grid>
      <Grid item xs={12}>
        <Button
          variant="contained"
          color="primary"
          onClick={() => channelButtonClicked()}
        >
          Enter Channel
        </Button>
        <Grid item xs={12}>
          <Button variant="contained" color="secondary" to="/" component={Link}>
            Back
          </Button>
        </Grid>
      </Grid>
    </Grid>
  );
}

export default ChannelJoinPage;
