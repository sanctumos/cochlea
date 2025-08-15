# Stateful Voice Agents

This repository demonstrates how to use Letta and LiveKit to create low-latency voice agents with memory, tool execution, and persistence.

## 🚀 Quick Start

**For immediate setup instructions, see our [Quick Reference Card](docs/quick-reference.md)**

## 📚 Comprehensive Documentation

This project includes detailed documentation to help you get started:

- **[📖 Documentation Index](docs/index.md)** - Complete overview and navigation
- **[🔧 Basic Setup Guide](docs/setup.md)** - Initial installation and configuration
- **[🌐 VPS Connection Guide](docs/vps-connection.md)** - Connect to self-hosted Letta instances
- **[⚙️ Environment Configuration](docs/environment.md)** - All environment variables and options
- **[🆘 Troubleshooting Guide](docs/troubleshooting.md)** - Common issues and solutions

## 🎯 What This Project Does

Creates low-latency voice agents using:
- **Letta** - AI agent management and memory
- **LiveKit** - Real-time voice communication
- **Deepgram** - Speech-to-text conversion
- **Cartesia** - Text-to-speech conversion

## 🏗️ Architecture

```
User Voice → LiveKit → Letta Voice Agent → Letta Instance → AI Models
                ↓
            Speech Processing (STT/TTS)
```

## ⚡ Quick Setup (Minimal)

### Prerequisites
- Python 3.10+
- Accounts with [LiveKit](https://livekit.io/), [Deepgram](https://deepgram.com/), [Cartesia](https://cartesia.ai/), and [OpenAI](https://openai.com/)

### Installation
```bash
git clone git@github.com:letta-ai/letta-voice.git
cd letta-voice 
pip install -r requirements.txt
```

### Basic Configuration
Create a `.env` file:
```bash
# Letta Configuration
LETTA_API_KEY=your_letta_api_key

# LiveKit Configuration
LIVEKIT_URL=wss://<YOUR-ROOM>.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

# Speech Services
DEEPGRAM_API_KEY=your_deepgram_api_key
CARTESIA_API_KEY=your_cartesia_api_key

# OpenAI Configuration (required for Letta)
OPENAI_API_KEY=your_openai_api_key
```

### Run
```bash
python main.py dev
```

## 🔗 Connection Options

### Letta Cloud (Default)
- No additional configuration needed
- Uses hosted Letta service

### Self-Hosted Letta
- Set `LETTA_BASE_URL=http://YOUR_VPS_IP:8283/v1` in your `.env`
- **No code changes required** - fully configurable via environment variables
- See [VPS Connection Guide](docs/vps-connection.md) for detailed setup

## 🐳 Self-Hosting Letta

To run your own Letta instance:

```bash
docker run \
  -v ~/.letta/.persist/pgdata:/var/lib/postgresql/data \
  -p 8283:8283 \
  -e OPENAI_API_KEY=${OPENAI_API_KEY} \
  letta/letta:latest
```

### Using ngrok for Local Development

If your Letta server isn't exposed to the public internet, you can use ngrok:

1. **Install ngrok**
2. **Add your authtoken**: `ngrok config add-authtoken <YOUR-AUTHTOKEN>`
3. **Ensure Letta is running** at `http://localhost:8283`
4. **Set the base URL** to your ngrok URL:
   ```bash
   export LETTA_BASE_URL=https://xxxx.ngrok.app
   ```

## 🎮 Running a Voice Agent

### Prerequisites
1. **Letta server running** with IP set in `LETTA_BASE_URL`
2. **Agent created** in Letta (via ADE or REST API)
3. **Agent ID set** in environment:
   ```bash
   export LETTA_AGENT_ID=agent-xxxxxxx
   ```

### Start the Agent
```bash
python main.py dev
```

### Test Your Agent
1. Go to [LiveKit Agents Playground](https://agents-playground.livekit.io/)
2. Connect to your room
3. Chat with your agent

## 🔧 Advanced Configuration

The project is now **fully configurable through environment variables** without code changes:

- **Agent customization**: Model, embedding, sleep-time settings
- **Connection options**: Cloud vs self-hosted
- **Performance tuning**: Buffer sizes, memory management

See [Environment Configuration](docs/environment.md) for all available options.

## ⚡ Performance

*Performance notes and optimization tips will be added here.*

## 👁️ Viewing Agent Interactions

*Demo and monitoring information for agent interactions will be added here.*

## 🆘 Need Help?

1. **Start with**: [Quick Reference Card](docs/quick-reference.md)
2. **Setup issues**: [Basic Setup Guide](docs/setup.md)
3. **VPS connection**: [VPS Connection Guide](docs/vps-connection.md)
4. **Configuration**: [Environment Configuration](docs/environment.md)
5. **Problems**: [Troubleshooting Guide](docs/troubleshooting.md)

## 📖 Additional Resources

- **Letta Documentation**: [docs.letta.com](https://docs.letta.com)
- **LiveKit Documentation**: [docs.livekit.io](https://docs.livekit.io)
- **Deepgram Documentation**: [developers.deepgram.com](https://developers.deepgram.com)
- **Cartesia Documentation**: [docs.cartesia.ai](https://docs.cartesia.ai)

---

**Ready to get started?** Begin with our [Quick Reference Card](docs/quick-reference.md) or dive into the [Complete Documentation](docs/index.md).


