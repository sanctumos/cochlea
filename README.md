# Stateful Voice Agents  
This repo show how to use Letta and Livekit to create low-latency voice agents with memory, tool execution, and persistence. 

## Installation
First install the basic requirements in a virtual enviornment (Python >= 3.10): 
```
git clone git@github.com:letta-ai/letta-voice.git
cd letta-voice 
pip install -r requirements.txt
```
You also will need to setup Livekit, Letta, and ngrok, and set the following env vars: 
```
LIVEKIT_URL=wss://letta-h884jw2p.livekit.cloud
LIVEKIT_API_KEY=...
LIVEKIT_API_SECRET=...

DEEPGRAM_API_KEY=...
CARTESIA_API_KEY=...
OPENAI_API_KEY=...
```

### Livekit
Create an account with LiveKit and set `LIVEKIT_API_SECRET`: 
```
export LIVEKIT_API_SECRET=gsk_....
```

### Letta 
To run Letta, you can either install and run [Letta Desktop](https://docs.letta.com/install) or run a Letta service with Docker: 
```
docker run \
  -v ~/.letta/.persist/pgdata:/var/lib/postgresql/data \
  -p 8283:8283 \
  -e OPENAI_API_KEY="your_openai_api_key" \
  letta/letta:latest
```
See Letta's full quickstart and installation instructions [here](https://docs.letta.com/quickstart). 


### ngrok 
1. Install ngrok
2. Add your ngrok authtoken with `ngrok config <YOUR-AUTHTOKEN>`
3. Make sure you have a Letta server running at `http://localhost:8283`.
4. Set `NGROK_URL=http://...`  to your ngrok URL. For example:
```
export NGROK_ENDPOINT=https://xxxx.ngrok.app
```


## Running a Voice Agent  
1. Create an agent with Letta. You can do this in the ADE or via a REST API call. 
2. Set the `LETTA_AGENT_ID=agent-....`, for example: 
```
export LETTA_AGENT_ID=agent-xxxxxxx
```
3. Run `python main.py dev`
4. Go to the Livekit Agents Playground: https://agents-playground.livekit.io/
5. Chat with your agent

## Performance 
TODO: notes on performance

## Viewing Agent Interactions 
TODO: ADE demo 
