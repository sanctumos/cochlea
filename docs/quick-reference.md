# Quick Reference Card

## Connect to VPS-Hosted Letta in 3 Steps

### 1. Set Environment Variable (No Code Changes!)
```bash
# Add to your .env file
LETTA_BASE_URL=http://YOUR_VPS_IP:8283/v1
```

**The code automatically detects this and connects to your VPS!**

### 2. Create .env file
```bash
# Required for VPS connection
LETTA_API_KEY=your_letta_api_key
LETTA_BASE_URL=http://YOUR_VPS_IP:8283/v1

# Other required services
LIVEKIT_URL=wss://<ROOM>.livekit.cloud
LIVEKIT_API_KEY=your_livekit_key
LIVEKIT_API_SECRET=your_livekit_secret
DEEPGRAM_API_KEY=your_deepgram_key
CARTESIA_API_KEY=your_cartesia_key
```

### 3. Ensure VPS is accessible
```bash
# Test connection
curl http://YOUR_VPS_IP:8283/health

# Check if port is open
telnet YOUR_VPS_IP 8283
```

## Common Issues

| Problem | Solution |
|---------|----------|
| Connection refused | Check Docker container is running on VPS |
| Invalid API key | Verify LETTA_API_KEY in .env |
| SSL errors | Use HTTP for dev, HTTPS for production |
| High latency | Check network latency to VPS |

## Quick Commands

```bash
# Start the voice agent
python main.py dev

# Check environment
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API Key:', 'SET' if os.getenv('LETTA_API_KEY') else 'NOT SET')"

# Test VPS connectivity
curl -v http://YOUR_VPS_IP:8283/v1/models
```

## VPS Docker Command
```bash
docker run \
  -v ~/.letta/.persist/pgdata:/var/lib/postgresql/data \
  -p 8283:8283 \
  -e OPENAI_API_KEY=${OPENAI_API_KEY} \
  letta/letta:latest
```

## Advanced Configuration Options

You can now customize your agent without code changes:

```bash
# Agent customization (for new agents)
LETTA_AGENT_NAME=my_custom_assistant
LETTA_MODEL=anthropic/claude-3-sonnet
LETTA_ENABLE_SLEEPTIME=false
LETTA_MAX_MESSAGE_BUFFER=15
LETTA_MIN_MESSAGE_BUFFER=5

# Agent reuse (for existing agents)
LETTA_AGENT_ID=agent_abc123...
```

## Agent Workflow

1. **First run**: Set `LETTA_AGENT_NAME` → Code creates agent → Copy agent ID from console
2. **Future runs**: Set `LETTA_AGENT_ID` → Code reuses existing agent with memory

## Need Help?
- **Setup**: [Basic Setup Guide](setup.md)
- **VPS Connection**: [VPS Connection Guide](vps-connection.md)
- **Environment**: [Environment Configuration](environment.md)
- **Troubleshooting**: [Troubleshooting Guide](troubleshooting.md) 