# Stateful Voice Agents

**🚧 Currently In Development Research Release**

This repository demonstrates how to use Letta and LiveKit to create low-latency voice agents with memory, tool execution, and persistence. This is a research implementation based on the original Letta Voice architecture, designed to be compatible with:

- **Direct Letta Integration** - Standard Letta Cloud or self-hosted instances
- **Broca Middleware** - Advanced routing and caching layer
- **Thalamus Refinement** - Transcript cleaning and structuring pipeline

*See [Audio Pipeline Architecture](AUDIO_PIPELINE_ARCHITECTURE.md) for detailed information about the multi-layer approach.*

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
- **Custom LLM Wrapper Required** - See technical details below
- See [VPS Connection Guide](docs/vps-connection.md) for detailed setup

## 🔧 Technical Implementation Details

### Custom LLM Wrapper for VPS Integration

This implementation includes a custom `VPSLettaLLM` class that bypasses LiveKit's `openai.LLM.with_letta()` method, which is hardcoded to use the `/voice-beta` endpoint that only exists in Letta Cloud.

**Why This Was Necessary:**
- LiveKit's `openai.LLM.with_letta()` only works with Letta Cloud
- Self-hosted Letta instances use standard `/messages` endpoints
- The `/voice-beta` endpoint doesn't exist on VPS installations

**How It Works:**
```python
class VPSLettaLLM(LLM):
    def __init__(self, agent_id: str, base_url: str, api_key: str):
        # Direct integration with Letta's standard message API
        # Bypasses LiveKit's cloud-only voice-beta endpoint
```

**Benefits:**
- ✅ Works with any Letta instance (cloud or self-hosted)
- ✅ Uses standard Letta message API endpoints
- ✅ Maintains full compatibility with LiveKit's async context manager protocol
- ✅ Provides better error handling and debugging capabilities

**Current Implementation:**
- Direct `requests.post` calls to `/agents/{agent_id}/messages`
- Proper `ChatContext` to `letta_messages` conversion
- Async context manager compatibility for LiveKit integration
- Comprehensive error handling and retry logic

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

## 🗺️ Development Roadmap

### Phase 1: Broca Plugin Compatibility
- **Status**: In Development
- **Goal**: Full integration with Broca middleware for advanced routing and caching
- **Features**:
  - Message deduplication and queue management
  - User context and core block management
  - Platform-specific response routing
  - Retry logic and error handling

### Phase 2: Thalamus Protocol Compatibility
- **Status**: Research Phase
- **Goal**: Extensive testing and integration of Thalamus refinement pipeline
- **Features**:
  - Real-time transcript cleaning and structuring
  - Speaker-aware segment grouping
  - Sentence completion logic
  - Noise filtering and TTS feedback prevention
  - Session-based state management

### Phase 3: Thalamus-Cochlea Joint Development
- **Status**: Planning Phase
- **Goal**: Optimized integration between audio input (Cochlea) and refinement (Thalamus)
- **Features**:
  - Seamless audio-to-text pipeline
  - Intelligent batching and processing
  - Performance optimization
  - Comprehensive monitoring and logging

### Phase 4: Full Whitepaper
- **Status**: Pending
- **Goal**: Complete technical documentation and research findings
- **Deliverables**:
  - Comprehensive architecture documentation
  - Performance benchmarks and analysis
  - Integration guides for all supported platforms
  - Best practices and implementation recommendations

## 📖 Additional Resources

- **Letta Documentation**: [docs.letta.com](https://docs.letta.com)
- **LiveKit Documentation**: [docs.livekit.io](https://docs.livekit.io)
- **Deepgram Documentation**: [developers.deepgram.com](https://developers.deepgram.com)
- **Cartesia Documentation**: [docs.cartesia.ai](https://docs.cartesia.ai)

---

**Ready to get started?** Begin with our [Quick Reference Card](docs/quick-reference.md) or dive into the [Complete Documentation](docs/index.md).


