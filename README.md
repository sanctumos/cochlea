# Stateful Voice Agents  
This repo show how to use Letta and Livekit to create low-latency voice agents with memory, tool execution, and persistence. 

## Installation & Setup 
First install the basic requirements in a virtual enviornment (Python >= 3.10): 
```
git clone git@github.com:letta-ai/letta-voice.git
cd letta-voice 
pip install -r requirements.txt
```
For this example, you will need accounts with the following providers: 
* [Livekit](https://livekit.io/) for handling the voice connection
* [Deepgram](https://deepgram.com/) for speech-to-text
* [Cartesia](https://cartesia.ai/) for text-to-speech

You will also need to set up the following environment variables (or create a `.env` file):
```sh 
LETTA_API_KEY=... # Letta Cloud API key (if using cloud)

LIVEKIT_URL=wss://<YOUR-ROOM>.livekit.cloud # Livekit URL
LIVEKIT_API_KEY=... # Livekit API key
LIVEKIT_API_SECRET=... # Livekit API secret

DEEPGRAM_API_KEY=... # Deepgram API key
CARTESIA_API_KEY=... # Cartesia API key
```

## Connecting Letta to Voice
1. Run `python main.py dev`
2. Go to the Livekit Agents Playground: https://agents-playground.livekit.io/
3. Chat with your agent

## Running with a self-hosted Letta Server

### Running Letta 
To run Letta, you can either install and run [Letta Desktop](https://docs.letta.com/install) or run a Letta service with Docker: 
```
docker run \
  -v ~/.letta/.persist/pgdata:/var/lib/postgresql/data \
  -p 8283:8283 \
  -e OPENAI_API_KEY=${OPENAI_API_KEY} \
  letta/letta:latest
```
See Letta's full quickstart and installation instructions [here](https://docs.letta.com/quickstart). 


### Running ngrok 
If you are self-hosting the Letta server locally (at `localhost`), you will need to use `ngrok` to expose your Letta server to the internet: 
1. Create an account on [ngrok](https://ngrok.com/)
2. Create an auth token and add it into your CLI 
```
ngrok config add-authtoken <YOUR_AUTH_TOKEN> 
```
3. Point your ngrok server to your Letta server: 
```
ngrok http http://localhost:8283
```
Now, you should have a forwarding URL like `https://<YOUR_FORWARDING_URL>.ngrok.app`, which you can pass in as the `base_url` to `openai.LLM.with_letta(...)`. 


