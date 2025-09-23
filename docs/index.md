<!--
Sanctum Cochlea - Audio Ingest System for Sanctum and Letta Installations
Copyright (C) 2025 Sanctum Cochlea Contributors

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/
-->

# Sanctum Cochlea Documentation Index

*Sanctum Cochlea is a fork of the letta-voice experiment, evolved into a comprehensive voice agent platform.*

Welcome to the Sanctum Cochlea documentation. This guide will help you set up and configure voice agents using Letta, LiveKit, and speech services.

## 🚀 Quick Start

**[Quick Reference Card](quick-reference.md)** - Get connected to your VPS-hosted Letta in 3 steps

## 📚 Complete Guides

### Setup & Configuration
- **[Basic Setup Guide](setup.md)** - Initial installation and configuration
- **[API Endpoints Setup](api-endpoints-setup.md)** - LiveKit, Deepgram, Cartesia, and Sanctum setup
- **[VPS Connection Guide](vps-connection.md)** - Connect to VPS-hosted Sanctum instances
- **[Environment Configuration](environment.md)** - Complete environment variable reference
- **[Quick Reference Card](quick-reference.md)** - Get connected in 3 steps

### Architecture & Integration
- **[Audio Pipeline Architecture](../architecture/AUDIO_PIPELINE_ARCHITECTURE.md)** - Multi-layer pipeline design
- **[Broca Plugin Integration](../integration/BROCA_PLUGIN_INTEGRATION.md)** - Middleware integration details

### Development & Support
- **[Troubleshooting Guide](troubleshooting.md)** - Common issues and solutions
- **[Changelog](../development/CHANGELOG.md)** - Project history and updates

## 🔧 Key Concepts

### Architecture Overview
```
User Voice → LiveKit → Sanctum Cochlea Agent → Letta Instance → AI Models
                ↓
            Speech Processing (STT/TTS)
```

### Connection Options
1. **Letta Cloud** (default) - Hosted service
2. **Self-Hosted** - Your own VPS with Docker

### Configuration Approach
- **Environment Variables** - Fully configurable without code changes
- **Automatic Detection** - Code automatically adapts to your settings
- **Flexible Deployment** - Easy switching between environments

### Required Services
- **Sanctum Instance** - Self-hosted AI agent platform (supports OpenAI, Anthropic, Ollama, and other LLM providers)
- **LiveKit** - Real-time voice communication
- **Deepgram** - Speech-to-text conversion
- **Cartesia** - Text-to-speech conversion

## 🎯 Common Use Cases

### Development
- Local testing with Sanctum instance
- Voice agent development and testing
- Integration testing

### Production
- Self-hosted Sanctum instance on VPS
- Custom voice agent deployment
- Production voice applications

## 🔒 Security Considerations

- **API Key Management** - Never commit sensitive data
- **Network Security** - Use HTTPS in production
- **Access Control** - Limit who has access to keys
- **Monitoring** - Track usage and access

## 📖 Additional Resources

- **Letta Documentation**: [docs.letta.com](https://docs.letta.com)
- **LiveKit Documentation**: [docs.livekit.io](https://docs.livekit.io)
- **Deepgram Documentation**: [developers.deepgram.com](https://developers.deepgram.com)
- **Cartesia Documentation**: [docs.cartesia.ai](https://docs.cartesia.ai)

## 🆘 Getting Help

1. **Check the troubleshooting guide** first
2. **Enable debug logging** for detailed error information
3. **Test with minimal setup** to isolate issues
4. **Check service status** - external services might be down

## 📝 Project Structure

```
sanctum-cochlea/
├── main.py              # Main application entry point
├── function_call.py     # Example function calling implementation
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
├── LICENSE              # AGPLv3 license for code
├── LICENSE-DOCS         # CC-BY-SA 4.0 license for documentation
├── README.md            # Project overview
└── docs/                # Documentation folder
    ├── index.md         # This file - documentation index
    ├── quick-reference.md
    ├── setup.md
    ├── vps-connection.md
    ├── environment.md
    ├── troubleshooting.md
    ├── architecture/    # Architecture documentation
    │   └── AUDIO_PIPELINE_ARCHITECTURE.md
    ├── integration/     # Integration guides
    │   └── BROCA_PLUGIN_INTEGRATION.md
    └── development/     # Development resources
        ├── CHANGELOG.md
        └── PR_DESCRIPTION.md
```

---

**Need to connect to a VPS-hosted Letta instance?** Start with the [Quick Reference Card](quick-reference.md) or go directly to the [VPS Connection Guide](vps-connection.md). 