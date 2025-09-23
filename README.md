<!--
Sanctum Cochlea - Audio Ingest System for Sanctum and Letta Installations
Copyright (C) 2025 Sanctum Cochlea Contributors

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/
-->

# Sanctum Cochlea

**🚧 Currently In Development Research Release**

*Sanctum Cochlea is a fork of the letta-voice experiment, audio ingest system for  Sanctum and Letta installations.*

This repository demonstrates how to use Letta and LiveKit to create low-latency voice agents with memory, tool execution, and persistence. This is a research implementation based on the original Letta Voice architecture, designed to be compatible with:

- **Direct Letta Integration** - Standard Letta Cloud or self-hosted instances
- **Broca Middleware** - Advanced routing and caching layer
- **Thalamus Refinement** - Transcript cleaning and structuring pipeline

*See [Audio Pipeline Architecture](docs/architecture/AUDIO_PIPELINE_ARCHITECTURE.md) for detailed information about the multi-layer approach.*

## 🚀 Quick Start

**For immediate setup instructions, see our [Quick Reference Card](docs/quick-reference.md)**

## 📚 Comprehensive Documentation

This project includes detailed documentation to help you get started:

- **[📖 Documentation Index](docs/index.md)** - Complete overview and navigation
- **[🔧 Basic Setup Guide](docs/setup.md)** - Initial installation and configuration
- **[🌐 API Endpoints Setup](docs/api-endpoints-setup.md)** - LiveKit, Deepgram, Cartesia, and Sanctum setup
- **[🌐 VPS Connection Guide](docs/vps-connection.md)** - Connect to self-hosted Sanctum instances
- **[⚙️ Environment Configuration](docs/environment.md)** - All environment variables and options
- **[🆘 Troubleshooting Guide](docs/troubleshooting.md)** - Common issues and solutions

## 🎯 What This Project Does

Creates low-latency voice agents using:
- **Sanctum Instance** - Your self-hosted AI agent platform (supports OpenAI, Anthropic, Ollama, and other LLM providers)
- **LiveKit** - Real-time voice communication
- **Deepgram** - Speech-to-text conversion
- **Cartesia** - Text-to-speech conversion

## 🏗️ Architecture

### Current Implementation
```
User Voice → LiveKit → Sanctum Cochlea Agent → Letta Instance → AI Models
                ↓
            Speech Processing (STT/TTS)
```

### Target Architecture: SanctumOS Integration

Sanctum Cochlea is designed to integrate with the broader **SanctumOS** modular architecture, functioning as a specialized sensory processing module within a larger agentic operating system.

#### SanctumOS Modular Framework
SanctumOS is a modular, self-hosted agentic operating system designed to run fully autonomous, context-rich AI agents. It emphasizes:
- **Modularity**: Clean, plugin-driven integration of specialized components
- **Privacy**: Complete self-hosting with no vendor lock-in
- **Autonomy**: Fully autonomous agents with infinite memory management
- **Real-time Processing**: Sensory filtering and event processing capabilities

#### Cochlea's Role in SanctumOS
Within the SanctumOS ecosystem, **Cochlea** serves as the **sensory input module**, responsible for:

- **Audio Capture**: Real-time audio stream processing via LiveKit
- **Speech-to-Text**: Converting audio to text using Deepgram
- **Sensory Filtering**: Preprocessing and filtering audio data
- **Data Preparation**: Formatting sensory input for downstream processing

#### Multi-Layer Audio Pipeline
The target architecture implements a sophisticated multi-layer pipeline:

```
Cochlea → Thalamus → Broca → Prime Agent → Voicebox
```

**Layer Breakdown:**
1. **Cochlea** (Audio Input): Raw audio capture and STT conversion
2. **Thalamus** (Refinement): Clean, structure, and refine transcripts
3. **Broca** (Routing): Route events with proper queue management
4. **Prime Agent** (Processing): Natural language processing via Letta
5. **Voicebox** (Audio Output): High-quality TTS conversion

#### Biological Inspiration
This architecture mirrors the human auditory system:
- **Cochlea**: Transduces sound waves into neural signals (audio → text)
- **Thalamus**: Relays and refines sensory information (transcript processing)
- **Broca**: Language production and routing (message management)
- **Cortex**: Higher-level processing (AI reasoning)

*For detailed technical specifications, see [Audio Pipeline Architecture](docs/architecture/AUDIO_PIPELINE_ARCHITECTURE.md)*

## ⚡ Quick Setup (Minimal)

### Prerequisites
- Python 3.10+
- **Working Sanctum Instance** - Self-hosted AI agent platform (configured with your preferred LLM provider)
- **API Accounts** - [LiveKit](https://cloud.livekit.io/), [Deepgram](https://deepgram.com/), and [Cartesia](https://cartesia.ai/)

**📋 Detailed API setup instructions:** See [API Endpoints Setup Guide](docs/api-endpoints-setup.md)

### Installation
```bash
git clone git@github.com:your-org/sanctum-cochlea.git
cd sanctum-cochlea 
pip install -r requirements.txt
```

### Basic Configuration
Create a `.env` file:
```bash
# Sanctum Instance Configuration
LETTA_API_KEY=your_sanctum_api_key
LETTA_BASE_URL=http://YOUR_SANCTUM_IP:8283/v1

# LiveKit Configuration
LIVEKIT_URL=wss://<YOUR-ROOM>.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

# Speech Services
DEEPGRAM_API_KEY=your_deepgram_api_key
CARTESIA_API_KEY=your_cartesia_api_key
```

### Run
```bash
python main.py dev
```

## 🔗 Sanctum Instance Requirements

### Required: Working Sanctum Instance
Sanctum Cochlea requires a **working Sanctum instance** (self-hosted AI agent platform) configured with your preferred LLM provider:

- **OpenAI** - GPT-4, GPT-3.5, etc.
- **Anthropic** - Claude Sonnet, Claude Haiku, etc.
- **Ollama** - Local models like Llama, Mistral, etc.
- **Other Providers** - Any LLM provider supported by Sanctum

### Easy Installation
**🚀 Bootstrap Installer (Recommended):** Use the [sanctumos/installer](https://github.com/sanctumos/installer) repository for automated setup.

### Configuration
- Set `LETTA_BASE_URL=http://YOUR_SANCTUM_IP:8283/v1` in your `.env`
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

## ⚡ Performance & Benefits

### SanctumOS Integration Benefits
- **Modular Architecture**: Clean separation of concerns with pluggable components
- **Privacy-First**: Complete self-hosting with no external dependencies
- **Scalability**: Independent scaling of sensory, processing, and routing layers
- **Fault Tolerance**: Isolated failures don't cascade through the system
- **Real-time Processing**: Optimized for low-latency voice interactions

### Current Performance Targets
- **End-to-End Latency**: <2 seconds from speech to response
- **Voice Detection**: >95% sentence completion rate
- **Error Handling**: <1% message processing failures
- **Audio Quality**: Natural, interruption-free conversations

*Detailed performance metrics and optimization strategies will be documented as the pipeline evolves.*

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

### Phase 3: SanctumOS Integration
- **Status**: Planning Phase
- **Goal**: Full integration with SanctumOS modular architecture
- **Features**:
  - Complete Cochlea-Thalamus-Broca pipeline implementation
  - SanctumOS plugin architecture compatibility
  - Modular component deployment and management
  - Cross-platform sensory processing capabilities
  - Real-time event processing and memory management

### Phase 4: Full Whitepaper
- **Status**: Pending
- **Goal**: Complete technical documentation and research findings
- **Deliverables**:
  - Comprehensive architecture documentation
  - Performance benchmarks and analysis
  - Integration guides for all supported platforms
  - Best practices and implementation recommendations

## 📖 Additional Resources

### Core Technologies
- **Letta Documentation**: [docs.letta.com](https://docs.letta.com)
- **LiveKit Documentation**: [docs.livekit.io](https://docs.livekit.io)
- **Deepgram Documentation**: [developers.deepgram.com](https://developers.deepgram.com)
- **Cartesia Documentation**: [docs.cartesia.ai](https://docs.cartesia.ai)

### SanctumOS Ecosystem
- **SanctumOS Overview**: [sanctumos.org](https://sanctumos.org) - Modular agentic operating system
- **Sanctum Installer**: [sanctumos/installer](https://github.com/sanctumos/installer) - Bootstrap installer for easy setup
- **Thalamus Project**: Real-time event processing and sensory refinement
- **Broca Middleware**: Message routing and queue management
- **Audio Pipeline Architecture**: [docs/architecture/AUDIO_PIPELINE_ARCHITECTURE.md](docs/architecture/AUDIO_PIPELINE_ARCHITECTURE.md) - Detailed technical specifications

## 📄 License

**Code**: This project is licensed under the GNU Affero General Public License v3.0 (AGPLv3). See [LICENSE](LICENSE) for details.

**Documentation**: All non-code content (documentation, README files, etc.) is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC-BY-SA 4.0). See [LICENSE-DOCS](LICENSE-DOCS) for details.

---

**Ready to get started?** Begin with our [Quick Reference Card](docs/quick-reference.md) or dive into the [Complete Documentation](docs/index.md).


