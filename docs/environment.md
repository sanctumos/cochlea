<!--
Sanctum Cochlea - Audio Ingest System for Sanctum and Letta Installations
Copyright (C) 2025 Sanctum Cochlea Contributors

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/
-->

# Environment Configuration Guide

*Sanctum Cochlea is a fork of the letta-voice experiment, evolved into a comprehensive voice agent platform.*

This guide explains all the environment variables and configuration options available for Sanctum Cochlea.

## Environment File Setup

Create a `.env` file in your project root directory. This file should **never be committed to version control** as it contains sensitive information.

```bash
# .env file example
LETTA_API_KEY=your_sanctum_api_key_here
LETTA_BASE_URL=http://YOUR_SANCTUM_IP:8283/v1
LIVEKIT_URL=wss://<YOUR-ROOM>.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
DEEPGRAM_API_KEY=your_deepgram_api_key
CARTESIA_API_KEY=your_cartesia_api_key
```

## Required Environment Variables

### Sanctum Instance Configuration

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `LETTA_API_KEY` | Your Sanctum instance API key for authentication | Yes | `sk-...` |
| `LETTA_BASE_URL` | Base URL for your Sanctum instance | Yes | `http://192.168.1.100:8283/v1` |

**Note:** Sanctum Cochlea requires a working Sanctum instance. The `LETTA_BASE_URL` must point to your self-hosted Sanctum instance.

### LiveKit Configuration

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `LIVEKIT_URL` | WebSocket URL for your LiveKit room | Yes | `wss://room-name.livekit.cloud` |
| `LIVEKIT_API_KEY` | LiveKit API key for authentication | Yes | `API...` |
| `LIVEKIT_API_SECRET` | LiveKit API secret for authentication | Yes | `secret...` |

### Speech Services

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `DEEPGRAM_API_KEY` | Deepgram API key for speech-to-text | Yes | `...` |
| `CARTESIA_API_KEY` | Cartesia API key for text-to-speech | Yes | `...` |

## Optional Environment Variables

### Letta Agent Configuration

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `LETTA_AGENT_ID` | **Existing agent ID to reuse** (if set, skips agent creation) | Auto-created | `agent_123...` |
| `LETTA_AGENT_NAME` | **Human-readable name** for new agent creation | `low_latency_voice_agent_demo` | `my_voice_assistant` |
| `LETTA_AGENT_TYPE` | Type of agent to create | `voice_convo_agent` | `conversation_agent` |
| `LETTA_MODEL` | AI model to use | `openai/gpt-4o-mini` | `anthropic/claude-3-sonnet` |
| `LETTA_EMBEDDING` | Embedding model | `openai/text-embedding-3-small` | `openai/text-embedding-ada-002` |
| `LETTA_ENABLE_SLEEPTIME` | Enable sleep-time management | `true` | `false` |
| `LETTA_MAX_MESSAGE_BUFFER` | Max messages before sleep | `10` | `20` |
| `LETTA_MIN_MESSAGE_BUFFER` | Min messages before wake | `6` | `3` |
| `LETTA_SLEEPTIME_MODEL` | Model for sleep-time agent | `anthropic/claude-sonnet-4-20250514` | `openai/gpt-4o-mini` |

**Note:** 
- **`LETTA_AGENT_ID`**: If you set this, the code will reuse the existing agent instead of creating a new one
- **`LETTA_AGENT_NAME`**: Only used when creating a new agent (when `LETTA_AGENT_ID` is not set)
- **First run**: Code creates agent and you can copy the agent ID to your `.env` for future runs

### Development and Debugging

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `DEBUG` | Enable debug logging | `False` | `True` |
| `LOG_LEVEL` | Logging level | `INFO` | `DEBUG`, `WARNING`, `ERROR` |
| `ENVIRONMENT` | Environment name | `development` | `production`, `staging` |

## Configuration Examples

### Sanctum Instance Setup
```bash
# .env for Sanctum instance
LETTA_API_KEY=sk-your-sanctum-api-key
LETTA_BASE_URL=http://192.168.1.100:8283/v1
LIVEKIT_URL=wss://myroom.livekit.cloud
LIVEKIT_API_KEY=APIkey123
LIVEKIT_API_SECRET=secret456
DEEPGRAM_API_KEY=dg_key_789
CARTESIA_API_KEY=cart_key_012
```

### Production Sanctum Setup
```bash
# .env for production Sanctum instance
LETTA_API_KEY=sk-your-production-sanctum-key
LETTA_BASE_URL=https://sanctum.yourdomain.com/v1
LIVEKIT_URL=wss://myroom.livekit.cloud
LIVEKIT_API_KEY=APIkey123
LIVEKIT_API_SECRET=secret456
DEEPGRAM_API_KEY=dg_key_789
CARTESIA_API_KEY=cart_key_012
```

### Production Setup with HTTPS
```bash
# .env for production with HTTPS
LETTA_API_KEY=sk-your-production-key
LETTA_BASE_URL=https://letta.yourdomain.com/v1
LIVEKIT_URL=wss://myroom.livekit.cloud
LIVEKIT_API_KEY=APIkey123
LIVEKIT_API_SECRET=secret456
DEEPGRAM_API_KEY=dg_key_789
CARTESIA_API_KEY=cart_key_012
ENVIRONMENT=production
LOG_LEVEL=WARNING
```

### Advanced Agent Configuration
```bash
# .env for custom agent configuration
LETTA_API_KEY=sk-your-key
LETTA_BASE_URL=http://192.168.1.100:8283/v1
LETTA_AGENT_NAME=my_custom_assistant
LETTA_MODEL=anthropic/claude-3-sonnet
LETTA_EMBEDDING=openai/text-embedding-ada-002
LETTA_ENABLE_SLEEPTIME=false
LETTA_MAX_MESSAGE_BUFFER=15
LETTA_MIN_MESSAGE_BUFFER=5
LETTA_SLEEPTIME_MODEL=openai/gpt-4o-mini

# Other services
LIVEKIT_URL=wss://myroom.livekit.cloud
LIVEKIT_API_KEY=APIkey123
LIVEKIT_API_SECRET=secret456
DEEPGRAM_API_KEY=dg_key_789
CARTESIA_API_KEY=cart_key_012
```

## Environment-Specific Configurations

### Development
```bash
ENVIRONMENT=development
DEBUG=True
LOG_LEVEL=DEBUG
```

### Staging
```bash
ENVIRONMENT=staging
DEBUG=False
LOG_LEVEL=INFO
```

### Production
```bash
ENVIRONMENT=production
DEBUG=False
LOG_LEVEL=WARNING
```

## Security Best Practices

### 1. Never Commit Sensitive Data
```bash
# Add to .gitignore
.env
.env.local
.env.production
*.key
*.pem
```

### 2. Use Different Keys for Different Environments
```bash
# Development
LETTA_API_KEY=sk-dev-key

# Production  
LETTA_API_KEY=sk-prod-key
```

### 3. Rotate Keys Regularly
- Set up a schedule for API key rotation
- Use environment-specific keys
- Monitor key usage and access

### 4. Restrict Access
- Limit who has access to production keys
- Use least-privilege access principles
- Monitor and log access to sensitive configurations

## Validation and Testing

### Environment Validation
The application will validate required environment variables on startup:

```python
# Example validation check
required_vars = ['LETTA_API_KEY', 'LIVEKIT_URL', 'LIVEKIT_API_KEY']
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    raise ValueError(f"Missing required environment variables: {missing_vars}")
```

### Testing Configuration
Test your configuration before running:

```bash
# Test environment loading
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Environment loaded successfully')"

# Test specific variables
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(f'Letta URL: {os.getenv(\"LETTA_BASE_URL\", \"Cloud\")}')"
```

## Troubleshooting Environment Issues

### Common Problems

1. **Variables Not Loading**
   - Ensure `.env` file is in the project root
   - Check file permissions
   - Verify no syntax errors in `.env`

2. **Wrong Values**
   - Double-check API keys and URLs
   - Ensure no extra spaces or quotes
   - Verify service account status

3. **Permission Denied**
   - Check file ownership and permissions
   - Ensure user has read access to `.env`

### Debug Commands
```bash
# Check if .env is loaded
python -c "import os; print('LETTA_API_KEY:', 'SET' if os.getenv('LETTA_API_KEY') else 'NOT SET')"

# List all environment variables
python -c "import os; [print(f'{k}: {v}') for k, v in os.environ.items() if 'LETTA' in k or 'LIVEKIT' in k]"
```

## Next Steps

After configuring your environment:
1. **Test the configuration** with the validation commands
2. **Run the application** to verify everything works
3. **Set up monitoring** for production environments
4. **Document your configuration** for team members

See the [VPS Connection Guide](vps-connection.md) for self-hosting setup or the [Troubleshooting Guide](troubleshooting.md) for common issues. 

## Agent Creation and Reuse Workflow

### First Run (Agent Creation)
```bash
# .env file - First run
LETTA_API_KEY=your_key
LETTA_AGENT_NAME=my_custom_assistant
LETTA_MODEL=anthropic/claude-3-sonnet
# LETTA_AGENT_ID is not set
```

**What happens:**
1. Code creates a new agent with name "my_custom_assistant"
2. Console shows: `Created new agent: my_custom_assistant (ID: agent_abc123...)`
3. **Copy this agent ID for future runs**

### Subsequent Runs (Agent Reuse)
```bash
# .env file - Reuse existing agent
LETTA_API_KEY=your_key
LETTA_AGENT_ID=agent_abc123...
# LETTA_AGENT_NAME is ignored when LETTA_AGENT_ID is set
```

**What happens:**
1. Code finds existing agent ID
2. Console shows: `Using existing agent ID: agent_abc123...`
3. **No new agent is created** - reuses existing one with all its memory

### Benefits of This Approach
- **Persistent memory**: Agent remembers conversations across runs
- **Cost efficient**: No need to recreate agents
- **Production ready**: Same agent serves multiple sessions
- **Easy switching**: Change `.env` to use different agents 