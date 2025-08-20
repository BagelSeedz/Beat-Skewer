var token = ''
const doyouevenmissmeatallid = "1AHf5FSofKcUw8tyKkccKF"

async function updateToken() {
    const res = await fetch("http://127.0.0.1:5000/spotify-token", {
        headers: {"Content-Type": "application/json"},
        method: 'GET',
    });

    const json = await res.json();
    token = json.access_token;
}

async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body:JSON.stringify(body)
  });
  return await res.json();
}

async function getTrack(id) {
    return await fetchWebApi("v1/tracks/"+id, 'GET');
}

async function getTempo(id) {
    const res = await fetch("http://127.0.0.1:5000/audio-features?track_id="+id, {
        headers: {"Content-Type": "application/json"},
        method: 'GET'
    });
    const json = await res.json();
    return json.tempo;
}

async function Beat() {
    await updateToken();
    const track = await getTrack(doyouevenmissmeatallid);
    const tempo = await getTempo(doyouevenmissmeatallid);

    console.log(track);

    return (
        <>
            <h1>{track.name}</h1>
            <h2>{"Tempo (BPM): "}{tempo}</h2>
        </>
    );
}


export default Beat;