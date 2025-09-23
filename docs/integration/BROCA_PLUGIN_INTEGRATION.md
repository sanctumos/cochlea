# Letta-Voice as a Broca Plugin Integration Guide

## Overview

This document outlines how to transform the `letta-voice` project into a Broca plugin, enabling voice-based communication through the Broca middleware system. The integration would allow Letta voice agents to communicate through Broca's plugin architecture, providing a standardized interface for voice interactions across different platforms.

## Current Architecture Analysis

### Letta-Voice Current Structure
- **Main Entry Point**: `main.py` - LiveKit-based voice agent using Letta client
- **Function Calls**: `function_call.py` - Example weather assistant with function calling
- **Dependencies**: LiveKit agents, Letta client, voice processing plugins (Deepgram, Cartesia, OpenAI)
- **Voice Pipeline**: Real-time voice processing with STT → LLM → TTS flow

### Broca Plugin System
- **Plugin Interface**: Abstract base class with required methods (`start`, `stop`, `get_name`, `get_platform`, `get_message_handler`)
- **Message Processing**: Queue-based system with platform-specific handlers
- **Multi-Agent Support**: Agent-specific configuration and isolation
- **Event System**: Plugin communication through events

## Integration Strategy

### 1. Plugin Architecture Design

The Letta-Voice plugin would serve as a **voice communication bridge** that:

- **Receives**: Text messages from Broca's message queue
- **Processes**: Converts text to speech and handles voice interactions
- **Sends**: Voice responses back through Broca's platform handlers
- **Manages**: LiveKit room connections and voice session lifecycle

### 2. Core Plugin Structure

```python
# plugins/letta_voice/plugin.py
from plugins import Plugin
from typing import Dict, Any, Optional, Callable
import asyncio
import logging

class LettaVoicePlugin(Plugin):
    def __init__(self, settings=None, agent_id=None):
        self.settings = settings
        self.agent_id = agent_id
        self.voice_session = None
        self.letta_client = None
        self.logger = logging.getLogger(f"LettaVoicePlugin.{agent_id or 'base'}")
    
    def get_name(self) -> str:
        return "letta_voice"
    
    def get_platform(self) -> str:
        return "voice"
    
    def get_message_handler(self) -> Callable:
        return self._handle_voice_message
    
    async def start(self) -> None:
        """Initialize voice session and Letta client"""
        # Initialize LiveKit voice session
        # Set up STT/TTS pipelines
        # Connect to Letta agent
        
    async def stop(self) -> None:
        """Clean up voice resources"""
        # Close LiveKit connections
        # Clean up voice pipelines
        
    async def _handle_voice_message(self, response: str, profile, message_id: int) -> None:
        """Convert text response to voice and send to user"""
        # Convert text to speech
        # Send voice response through appropriate channel
```

### 3. Message Flow Integration

```
Broca Message Queue → LettaVoice Plugin → Voice Processing → User
     ↑                                                      ↓
     ← Platform Handler ← Voice Response ← TTS Pipeline ←
```

#### Incoming Messages (Text → Voice)
1. **Broca receives text message** from platform (Telegram, CLI, etc.)
2. **Message queued** for processing
3. **LettaVoice plugin** receives text via `_handle_voice_message()`
4. **Text converted to speech** using TTS (Cartesia/OpenAI)
5. **Voice sent** to user through appropriate voice channel

#### Outgoing Messages (Voice → Text)
1. **User speaks** into voice interface
2. **Voice captured** and converted to text via STT (Deepgram)
3. **Text sent** to Broca message queue
4. **Broca processes** through agent API
5. **Response returned** as text for voice conversion

### 4. Configuration Management

#### Plugin Settings Schema
```json
{
  "plugins": {
    "letta_voice": {
      "enabled": true,
      "voice_settings": {
        "stt_provider": "deepgram",
        "tts_provider": "cartesia",
        "voice_model": "nova-2",
        "language": "en-US"
      },
      "letta_settings": {
        "agent_id": "agent-123",
        "base_url": "https://api.letta.ai",
        "model": "openai/gpt-4o-mini"
      },
      "livekit_settings": {
        "room_url": "wss://your-livekit-server.com",
        "api_key": "your-api-key",
        "api_secret": "your-api-secret"
      }
    }
  }
}
```

#### Agent-Specific Configuration
- Each agent instance can have different voice settings
- Voice personality and TTS voice selection per agent
- Different STT/TTS providers per agent
- Custom LiveKit room configurations

### 5. Implementation Components

#### A. Voice Session Manager
```python
class VoiceSessionManager:
    """Manages LiveKit voice sessions and audio pipelines"""
    
    async def create_session(self, room_url: str, token: str):
        """Create new voice session"""
        
    async def start_voice_pipeline(self, stt_config, tts_config):
        """Initialize STT and TTS pipelines"""
        
    async def process_voice_input(self, audio_data) -> str:
        """Convert voice to text"""
        
    async def generate_voice_response(self, text: str) -> bytes:
        """Convert text to voice"""
```

#### B. Letta Integration Layer
```python
class LettaVoiceBridge:
    """Bridges Letta agent with voice processing"""
    
    async def send_voice_message(self, text: str, agent_id: str) -> str:
        """Send text to Letta agent and get response"""
        
    async def handle_function_calls(self, function_data):
        """Process function calls from Letta agent"""
        
    async def manage_conversation_context(self, messages):
        """Maintain conversation context for voice interactions"""
```

#### C. Platform-Specific Voice Handlers
```python
class VoicePlatformHandler:
    """Handles voice communication for different platforms"""
    
    async def send_voice_to_telegram(self, voice_data, chat_id):
        """Send voice message to Telegram"""
        
    async def send_voice_to_web(self, voice_data, session_id):
        """Send voice message to web interface"""
        
    async def send_voice_to_api(self, voice_data, endpoint):
        """Send voice message to custom API endpoint"""
```

### 6. Multi-Agent Voice Support

#### Agent Isolation
- **Separate voice sessions** per agent instance
- **Agent-specific voice personalities** (different TTS voices)
- **Isolated conversation contexts** per agent
- **Independent voice settings** per agent

#### Configuration Hierarchy
1. **Agent-specific voice settings** (highest priority)
2. **Base voice configuration** (fallback)
3. **Default voice settings** (lowest priority)

### 7. Event System Integration

#### Voice Events
```python
class VoiceEvent(Event):
    """Voice-specific events"""
    VOICE_SESSION_STARTED = "voice_session_started"
    VOICE_SESSION_ENDED = "voice_session_ended"
    VOICE_MESSAGE_RECEIVED = "voice_message_received"
    VOICE_MESSAGE_SENT = "voice_message_sent"
    VOICE_ERROR = "voice_error"
```

#### Event Handling
- **Session lifecycle events** for monitoring voice connections
- **Message events** for tracking voice interactions
- **Error events** for voice processing failures
- **Metrics events** for voice quality and latency tracking

### 8. Error Handling and Recovery

#### Voice-Specific Error Handling
- **STT failures**: Fallback to text input
- **TTS failures**: Fallback to text output
- **LiveKit disconnections**: Automatic reconnection
- **Letta API failures**: Graceful degradation

#### Recovery Strategies
- **Automatic retry** for transient failures
- **Fallback modes** when voice processing fails
- **Health checks** for voice pipeline components
- **Graceful degradation** to text-only mode

### 9. Performance Considerations

#### Voice Processing Optimization
- **Audio buffering** for smooth voice playback
- **Streaming TTS** for real-time responses
- **Connection pooling** for LiveKit sessions
- **Caching** for frequently used voice responses

#### Resource Management
- **Memory management** for audio data
- **CPU optimization** for voice processing
- **Network optimization** for voice streaming
- **Cleanup** of voice resources

### 10. Testing Strategy

#### Unit Testing
- **Plugin lifecycle** testing
- **Voice processing** component testing
- **Configuration** validation testing
- **Error handling** testing

#### Integration Testing
- **End-to-end voice flow** testing
- **Multi-agent voice** testing
- **Platform integration** testing
- **Performance** testing

#### Voice Quality Testing
- **Audio quality** validation
- **Latency measurement** testing
- **Voice recognition accuracy** testing
- **TTS quality** assessment

## Implementation Phases

### Phase 1: Core Plugin Structure
1. Create basic plugin class with required methods
2. Implement voice session management
3. Add basic text-to-voice conversion
4. Integrate with Broca message queue

### Phase 2: Letta Integration
1. Connect to Letta agent API
2. Implement voice message processing
3. Add function call support
4. Handle conversation context

### Phase 3: Platform Integration
1. Add platform-specific voice handlers
2. Implement voice message routing
3. Add voice event system
4. Integrate with existing Broca plugins

### Phase 4: Multi-Agent Support
1. Add agent-specific voice configurations
2. Implement voice session isolation
3. Add agent-specific voice personalities
4. Test multi-agent voice scenarios

### Phase 5: Advanced Features
1. Add voice quality monitoring
2. Implement voice analytics
3. Add voice customization options
4. Optimize performance and reliability

## Benefits of Integration

### For Broca
- **Voice communication** capability across all platforms
- **Unified voice interface** for different communication channels
- **Extensible voice system** through plugin architecture
- **Multi-agent voice support** with isolation

### For Letta-Voice
- **Standardized integration** with message processing systems
- **Multi-platform voice support** through Broca's plugin system
- **Centralized configuration** and management
- **Scalable architecture** for multiple voice agents

### For Users
- **Consistent voice experience** across platforms
- **Seamless voice interactions** with AI agents
- **Multi-channel voice support** (Telegram, web, API)
- **Reliable voice processing** with error handling

## Conclusion

Transforming Letta-Voice into a Broca plugin would create a powerful voice communication bridge that leverages Broca's robust message processing system while providing advanced voice capabilities. The integration would enable voice interactions across multiple platforms while maintaining the flexibility and extensibility of both systems.

The key to successful integration lies in:
1. **Proper abstraction** of voice processing components
2. **Seamless integration** with Broca's message queue system
3. **Robust error handling** for voice-specific failures
4. **Multi-agent support** with proper isolation
5. **Performance optimization** for real-time voice processing

This integration would significantly enhance both systems' capabilities and provide users with a comprehensive voice-enabled AI communication platform.
