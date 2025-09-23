# VPS Connection Guide

*Sanctum Cochlea is a fork of the letta-voice experiment, evolved into a comprehensive voice agent platform.*

This guide explains how to connect Sanctum Cochlea to a VPS-hosted Docker instance of Letta instead of using Letta Cloud.

## Overview

By default, the project connects to Letta Cloud. To use your self-hosted instance, you need to:
1. **Set the `LETTA_BASE_URL` environment variable** (no code changes required!)
2. Set up proper environment variables
3. Ensure your VPS is accessible and secure

## Step 1: Environment Variables (No Code Changes!)

**The code automatically detects your configuration through environment variables.** Simply set `LETTA_BASE_URL` in your `.env` file:

### For Letta Cloud (Default)
```bash
# .env file - Letta Cloud
LETTA_API_KEY=your_letta_api_key_here
# LETTA_BASE_URL is not set, defaults to Letta Cloud
```

### For Self-Hosted Letta
```bash
# .env file - Self-Hosted
LETTA_API_KEY=your_letta_api_key_here
LETTA_BASE_URL=http://YOUR_VPS_IP:8283/v1
```

## Step 2: Environment Variables

Create a `.env` file in your project root with these variables:

```bash
# Letta Self-Hosted Configuration
LETTA_API_KEY=your_letta_api_key_here
LETTA_BASE_URL=http://YOUR_VPS_IP:8283/v1

# LiveKit Configuration
LIVEKIT_URL=wss://<YOUR-ROOM>.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

# Speech Services
DEEPGRAM_API_KEY=your_deepgram_api_key
CARTESIA_API_KEY=your_cartesia_api_key
```

**Note:** The code automatically handles this configuration - no manual code changes are required!

## Step 3: VPS Docker Setup

Your VPS needs to run Letta in Docker with proper exposure:

```bash
docker run \
  -v ~/.letta/.persist/pgdata:/var/lib/postgresql/data \
  -p 8283:8283 \
  -e OPENAI_API_KEY=${OPENAI_API_KEY} \
  letta/letta:latest
```

### Key Requirements:
- **Port 8283** must be exposed and accessible
- **VPS must be reachable** from your development machine
- **Firewall rules** must allow connections to port 8283

## Step 4: Security Considerations

### Network Security
- Use a reverse proxy (nginx) for SSL termination
- Configure firewall to only allow necessary connections
- Consider using a VPN for secure access

### SSL/HTTPS Setup
If you want to use HTTPS (recommended for production):

```bash
# Using nginx as reverse proxy
server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://localhost:8283;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Then update your base URL to use HTTPS:
```bash
LETTA_BASE_URL=https://your-domain.com/v1
```

## Step 5: Testing the Connection

1. **Start your VPS Letta instance**
2. **Verify accessibility**:
   ```bash
   curl http://YOUR_VPS_IP:8283/health
   # or
   curl http://YOUR_VPS_IP:8283/v1/models
   ```

3. **Run the voice agent**:
   ```bash
   python main.py dev
   ```

4. **Check for connection errors** in the console output

## Troubleshooting

### Connection Refused
- Verify Docker container is running
- Check firewall settings
- Ensure port 8283 is exposed

### Authentication Errors
- Verify `LETTA_API_KEY` is correct
- Check if your VPS instance requires different authentication

### SSL/TLS Issues
- If using HTTPS, verify certificate validity
- Check reverse proxy configuration
- Ensure proper SSL termination

## Example Complete Setup

Here's a complete example of the modified `main.py`:

```python
import os
from dotenv import load_dotenv
from letta_client import Letta, VoiceSleeptimeManagerUpdate
from livekit import agents
from livekit.agents import AgentSession, Agent, AutoSubscribe
from livekit.plugins import openai, cartesia, deepgram

load_dotenv()

async def entrypoint(ctx: agents.JobContext):
    agent_id = os.environ.get('LETTA_AGENT_ID')
    print(f"Agent id: {agent_id}")
    
    session = AgentSession(
        llm=openai.LLM.with_letta(
            agent_id=agent_id,
            base_url=os.getenv('LETTA_BASE_URL'),  # Self-hosted URL
        ),
        stt=deepgram.STT(),
        tts=cartesia.TTS(),
    )
    
    # ... rest of the function
```

## Next Steps

After successful connection:
1. Test voice interactions
2. Monitor performance and latency
3. Consider production optimizations
4. Set up monitoring and logging

See the [troubleshooting guide](troubleshooting.md) for common issues and solutions. 