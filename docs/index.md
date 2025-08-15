# Letta Voice Documentation Index

Welcome to the Letta Voice project documentation. This guide will help you set up and configure voice agents using Letta, LiveKit, and speech services.

## 🚀 Quick Start

**[Quick Reference Card](quick-reference.md)** - Get connected to your VPS-hosted Letta in 3 steps

## 📚 Complete Guides

### [Basic Setup Guide](setup.md)
- Initial installation and configuration
- Service account setup (LiveKit, Deepgram, Cartesia)
- Environment configuration
- Testing your setup

### [VPS Connection Guide](vps-connection.md)
- **Main guide for connecting to VPS-hosted Letta**
- Code modifications required
- Environment variable setup
- Security considerations
- Testing connectivity

### [Environment Configuration](environment.md)
- Complete environment variable reference
- Configuration examples for different environments
- Security best practices
- Validation and testing

### [Troubleshooting Guide](troubleshooting.md)
- Common issues and solutions
- Debug mode and diagnostics
- Network troubleshooting
- Docker troubleshooting

## 🔧 Key Concepts

### Architecture Overview
```
User Voice → LiveKit → Letta Voice Agent → Letta Instance → AI Models
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
- **Letta** - AI agent management and memory
- **LiveKit** - Real-time voice communication
- **Deepgram** - Speech-to-text conversion
- **Cartesia** - Text-to-speech conversion

## 🎯 Common Use Cases

### Development
- Local testing with Letta Cloud
- Voice agent development and testing
- Integration testing

### Production
- Self-hosted Letta on VPS
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
letta-voice/
├── main.py              # Main application entry point
├── function_call.py     # Example function calling implementation
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
├── docs/               # This documentation folder
│   ├── index.md        # This file
│   ├── quick-reference.md
│   ├── setup.md
│   ├── vps-connection.md
│   ├── environment.md
│   └── troubleshooting.md
└── README.md           # Project overview
```

---

**Need to connect to a VPS-hosted Letta instance?** Start with the [Quick Reference Card](quick-reference.md) or go directly to the [VPS Connection Guide](vps-connection.md). 