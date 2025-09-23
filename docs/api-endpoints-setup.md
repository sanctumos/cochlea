<!--
Sanctum Cochlea - Audio Ingest System for Sanctum and Letta Installations
Copyright (C) 2025 Sanctum Cochlea Contributors

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/
-->

# 🌐 API Endpoints Setup & Access Guide

This guide provides comprehensive instructions for setting up and accessing all required API endpoints for Sanctum Cochlea.

## 🔹 LiveKit Setup

### LiveKit Cloud (Recommended for Development)

**Easiest path for getting started:**

1. **Sign up** at [cloud.livekit.io](https://cloud.livekit.io)
2. **Create a new project** (free tier available)
3. **Get your credentials:**
   - Go to **Project Settings**
   - Copy your `LIVEKIT_URL` (format: `wss://<your-project>.livekit.cloud`)
   - Go to **API Keys** section
   - Generate new API key and secret
   - **Important**: The secret is shown only once - copy it immediately!

**Configuration:**
```bash
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_api_key_here
LIVEKIT_API_SECRET=your_api_secret_here
```

### Self-Hosted LiveKit

**For production or privacy requirements:**

1. **Install LiveKit Server:**
   ```bash
   # Using Docker (recommended)
   docker run -p 7880:7880 livekit/livekit-server
   
   # Or download binary from GitHub releases
   ```

2. **Configure server** (`livekit.yaml`):
   ```yaml
   rtc:
     port: 7880
     use_tls: true  # Use wss:// for secure connections
   
   keys:
     your_api_key: your_api_secret
   ```

3. **Configuration:**
   ```bash
   LIVEKIT_URL=ws://your-server-ip:7880    # HTTP
   LIVEKIT_URL=wss://your-server-ip:7880   # HTTPS
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret
   ```

### LiveKit Sandbox Access

**For testing and development:**
- **LiveKit Cloud** provides the easiest sandbox environment
- Free tier includes sufficient resources for development
- No additional configuration needed beyond the cloud setup above
- Use the `wss://...livekit.cloud` URL + API keys for immediate access

## 🔹 Deepgram Setup

### Cloud Service (Recommended)

**Deepgram is cloud-only with no open self-hosting:**

1. **Sign up** at [deepgram.com](https://deepgram.com)
2. **Generate API Key** in the dashboard
3. **Choose your integration:**
   - **REST API** for batch processing
   - **WebSocket** for real-time streaming (used by Sanctum Cochlea)

**Configuration:**
```bash
DEEPGRAM_API_KEY=your_deepgram_api_key_here
```

### Self-Hosted STT Alternatives

**If you need local/self-hosted STT:**

- **Faster-Whisper** (CTranslate2 optimized Whisper)
- **NVIDIA Riva ASR** (GPU-accelerated)
- **Whisper.cpp** (CPU-optimized)

**Requirements:** ≥16 GB VRAM GPU for near-real-time quality

## 🔹 Cartesia Setup

### Cloud Service

**Cartesia provides cloud-based TTS:**

1. **Sign up** at [cartesia.ai](https://cartesia.ai)
2. **Generate API Key** from dashboard
3. **Use REST API** endpoint: `https://api.cartesia.ai`

**Configuration:**
```bash
CARTESIA_API_KEY=your_cartesia_api_key_here
```

### Self-Hosted TTS Alternatives

**Cartesia on-premise is enterprise-only. For local control, consider:**

- **Dia-1.6B** (expressive, open weights)
- **XTTS-v2** (efficient voice cloning)
- **Piper/MeloTTS** (lightweight)
- **NVIDIA Riva TTS** (GPU-accelerated)

**Voice Cloning Options:**
- **OpenVoice** (open-source voice cloning)
- **Real-Time Voice Cloning** (SV2TTS)
- **RVC** (voice conversion)

**Requirements:** ≥16 GB VRAM GPU for production quality

## 🔹 Sanctum Instance Setup

### Required: Working Sanctum Instance

Sanctum Cochlea requires a **working Sanctum instance** configured with your preferred LLM provider:

**Supported Providers:**
- **OpenAI** - GPT-4, GPT-3.5, etc.
- **Anthropic** - Claude Sonnet, Claude Haiku, etc.
- **Ollama** - Local models like Llama, Mistral, etc.
- **Other Providers** - Any LLM provider supported by Sanctum

**Configuration:**
```bash
LETTA_API_KEY=your_sanctum_api_key_here
LETTA_BASE_URL=http://your-sanctum-ip:8283/v1
```

## 🔧 Complete Configuration Example

**Full `.env` file setup:**

```bash
# Sanctum Instance Configuration
LETTA_API_KEY=your_sanctum_api_key_here
LETTA_BASE_URL=http://your-sanctum-ip:8283/v1

# LiveKit Configuration (Cloud)
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

# Speech Services
DEEPGRAM_API_KEY=your_deepgram_api_key
CARTESIA_API_KEY=your_cartesia_api_key

# Optional: Agent Configuration
LETTA_AGENT_NAME=my_voice_assistant
LETTA_MODEL=anthropic/claude-3-sonnet
LETTA_ENABLE_SLEEPTIME=true
```

## 🚀 Quick Start Sandbox Setup

**For immediate testing:**

1. **LiveKit Cloud** - Create free project at [cloud.livekit.io](https://cloud.livekit.io)
2. **Deepgram** - Sign up for free tier at [deepgram.com](https://deepgram.com)
3. **Cartesia** - Get free API key at [cartesia.ai](https://cartesia.ai)
4. **Sanctum Instance** - Deploy your preferred LLM provider

**All services offer free tiers sufficient for development and testing.**

## 🔧 Troubleshooting & Routing Notes

### Audio Pipeline Architecture

**Broca stays text-only. All audio endpoints need a shim:**

```
Cochlea (STT) → Thalamus (refine) → Broca (text)
Broca (text) → Voicebox (TTS) → LiveKit (audio)
```

### Sandboxing Strategy

**For development and testing:**
- **LiveKit Cloud** = sandbox for audio transport
- **Deepgram/Cartesia free tiers** = sandbox for STT/TTS
- **Local testing**: Run Faster-Whisper + XTTS in Docker as your own sandbox stack

### Common Issues

1. **API Key Security**: Never commit API keys to version control
2. **Rate Limits**: Free tiers have usage limits - monitor your usage
3. **Network Access**: Ensure your Sanctum instance is accessible from your development machine
4. **SSL/TLS**: Use `wss://` URLs for secure WebSocket connections

## 📚 Additional Resources

- **LiveKit Documentation**: [docs.livekit.io](https://docs.livekit.io)
- **Deepgram Documentation**: [developers.deepgram.com](https://developers.deepgram.com)
- **Cartesia Documentation**: [docs.cartesia.ai](https://docs.cartesia.ai)
- **SanctumOS Documentation**: [sanctumos.org](https://sanctumos.org)

---

**Need help?** Check the [Troubleshooting Guide](troubleshooting.md) or [Environment Configuration](environment.md) for more details.
