# Stateful Voice Agents  
This repo show how to use Letta and Livekit to create low-latency voice agents with memory, tool execution, and persistence. 

## Installation 

1. Clone this repository `git@github.com:letta-ai/letta-voice.git`
2. Install requirements 
```
cd letta-voice 
pip install -r requirements.txt
```
3. Install ngrok 
4. Add your ngrok authtoken with `ngrok config <YOUR-AUTHTOKEN>`


## Setup 

### Creating an agent
1. Install Letta
2. Configure ngrok with `ngrok http http://localhost:8283`
3. Run letta `letta server` 
4. Create an agent 

### Voice Demo 
1. Run `python main.py dev`
2. Go to the Livekit agents platform https://agents-playground.livekit.io


## Performance 
TODO: notes on performance

## Viewing Agent Interactions 
TODO: ADE demo 

