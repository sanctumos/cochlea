# Stateful Voice Agents  
This repo show how to use Letta and Livekit to create low-latency voice agents with memory, tool execution, and persistence. 

## Installation
This repository depends on Letta, ngrok, and Livekit. 

### Livekit 
1. Clone this repository `git@github.com:letta-ai/letta-voice.git`
2. Install requirements 
```
cd letta-voice 
pip install -r requirements.txt
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
3. Make sure you have a Letta server running at `http://localhost:8283`. Set `NGROK_URL=http://...`  to your ngrok URL. 


## Running a Voice Agent  
1. Create an agent with Letta. You can do this in the ADE or via a REST API call. 
2. Set the `LETTA_AGENT_ID=agent-....`
3. Run `python main.py dev`
4. Go to the Livekit Agents Playground: https://agents-playground.livekit.io/
5. Chat with your agent

## Performance 
TODO: notes on performance

## Viewing Agent Interactions 
TODO: ADE demo 