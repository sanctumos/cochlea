# Sanctum Cochlea Documentation

*Sanctum Cochlea is a fork of the letta-voice experiment, evolved into a comprehensive voice agent platform.*

This documentation explains how to set up and configure Sanctum Cochlea to work with both Letta Cloud and self-hosted Letta instances.

## Quick Start

- **[Basic Setup](setup.md)** - Initial installation and configuration
- **[VPS Connection Guide](vps-connection.md)** - How to connect to a VPS-hosted Letta Docker instance
- **[Environment Configuration](environment.md)** - Environment variables and configuration options
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions

## Documentation Structure

- **[Architecture](architecture/)** - Technical architecture and design documents
- **[Integration](integration/)** - Integration guides and middleware documentation
- **[Development](development/)** - Development resources, changelog, and project history

## Overview

Sanctum Cochlea creates low-latency voice agents using:
- **Letta** - For AI agent management and memory
- **LiveKit** - For real-time voice communication
- **Deepgram** - For speech-to-text
- **Cartesia** - For text-to-speech

## Architecture

```
User Voice → LiveKit → Sanctum Cochlea Agent → Letta Instance → AI Models
                ↓
            Speech Processing (STT/TTS)
```

## Prerequisites

- Python 3.10+
- Docker (for self-hosting Letta)
- Accounts with LiveKit, Deepgram, and Cartesia
- VPS or cloud server (for self-hosting)

## Getting Help

If you encounter issues:
1. Check the [troubleshooting guide](troubleshooting.md)
2. Review the [environment configuration](environment.md)
3. Ensure your VPS setup follows the [VPS connection guide](vps-connection.md) 