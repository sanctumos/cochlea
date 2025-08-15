# Letta Voice Documentation

This documentation explains how to set up and configure the Letta Voice project to work with both Letta Cloud and self-hosted Letta instances.

## Quick Start

- **[Basic Setup](setup.md)** - Initial installation and configuration
- **[VPS Connection Guide](vps-connection.md)** - How to connect to a VPS-hosted Letta Docker instance
- **[Environment Configuration](environment.md)** - Environment variables and configuration options
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions

## Overview

The Letta Voice project creates low-latency voice agents using:
- **Letta** - For AI agent management and memory
- **LiveKit** - For real-time voice communication
- **Deepgram** - For speech-to-text
- **Cartesia** - For text-to-speech

## Architecture

```
User Voice → LiveKit → Letta Voice Agent → Letta Instance → AI Models
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