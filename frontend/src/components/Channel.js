import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const Channel = (props) => {
  let params = useParams();
  const [channelCode, setChannelCode] = useState(params.channelCode);

  const initialState = {
    votesSKip: 2,
    guestPause: false,
    isHost: false,
  };
  const [channelData, setChannelData] = useState(initialState);

  useEffect(() => {
    fetch("/api/get-channel" + "?code=" + channelCode)
      .then((res) => res.json())
      .then((data) => {
        setChannelData({
          ...channelData,
          votesSKip: data.votes_skip,
          guestPause: data.guest_pause,
          isHost: data.is_host,
        });
      });
  }, [channelCode, setChannelData]);
  return (
    <div>
      <h3>{channelCode}</h3>
      <p>Votes: {channelData.votesSKip}</p>
      <p>Guest Can Pause: {channelData.guestPause.toString()}</p>
      <p>Host: {channelData.isHost.toString()}</p>
    </div>
  );
};

export default Channel;
