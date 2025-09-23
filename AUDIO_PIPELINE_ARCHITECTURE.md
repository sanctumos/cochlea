# Audio Pipeline Architecture: Cochlea → Thalamus → Broca → Prime Agent

## Overview

This document outlines a multi-layer audio processing pipeline architecture designed to solve the fundamental issues with real-time voice agent interactions. The current direct pipeline approach leads to cutting off, interruptions, inconsistent detection, and timeout issues.

## Current Problem

```
Your Mic → LiveKit → Raw STT → VPS Letta → Raw TTS → LiveKit → Your Speakers
```

**Issues:**
- Raw, unfiltered audio processing
- No sentence completion logic
- VAD conflicts with TTS
- Network timeout vulnerabilities
- Inconsistent voice detection

## Proposed Architecture

### Digital Audio Conversations
```
Cochlea → Thalamus → Broca → Prime Agent → Voicebox
```

### Ambient/Ear Devices
```
Cochlea → Thalamus → Cerebellum → Prime Agent
```

## Layer Definitions

### 1. Cochlea (Audio Input Layer)
**Role:** Raw audio capture and initial speech-to-text conversion

**Responsibilities:**
- Audio stream capture via LiveKit
- Real-time STT processing (Deepgram)
- Raw transcript segment generation
- Audio quality monitoring

**Current Implementation:**
- LiveKit WebRTC audio streaming
- Deepgram STT with interim results
- Basic audio preprocessing

**Output:** Raw transcript segments with timing metadata

### 2. Thalamus (Refinement Layer)
**Role:** Clean, structure, and refine raw transcripts before processing

**Key Functions:**
- **Segment Grouping:** Combine consecutive segments from same speaker
- **Sentence Completion:** Wait for complete thoughts before processing
- **Noise Filtering:** Remove false triggers and TTS feedback
- **Speaker Diarization:** Handle multiple speakers intelligently
- **Context Preservation:** Maintain conversation flow

**Methodology (from sanctum-thalamus):**
- Session-based state management
- Speaker-aware grouping with inactivity timeouts
- Intelligent batching of segments
- Real-time refinement with cleanup

**Output:** Clean, structured text events ready for processing

### 3. Broca (Routing Layer)
**Role:** Route refined text events across Sanctum with proper management

**Key Functions:**
- **Message Deduplication:** Prevent duplicate processing
- **Queue Management:** Handle concurrent requests safely
- **User Context:** Manage core blocks and user state
- **Platform Routing:** Route responses to appropriate channels
- **Retry Logic:** Handle network failures gracefully

**Methodology (from broca):**
- In-memory caching with cleanup
- Database-backed queue processing
- Core block attach/detach management
- Platform-specific response routing

**Output:** Properly queued and routed text events

### 4. Prime Agent (Processing Layer)
**Role:** Consume refined text as if it were natural chat input

**Responsibilities:**
- Process clean, structured text events
- Generate contextual responses
- Maintain conversation state
- Apply business logic and reasoning

**Current Implementation:**
- VPS Letta instance
- Custom LLM wrapper for VPS integration
- Message formatting and identification

**Output:** Structured response text

### 5. Voicebox (Audio Output Layer)
**Role:** Convert responses back to high-quality audio

**Responsibilities:**
- Text-to-speech conversion
- Audio quality optimization
- Response timing management
- Audio feedback prevention

**Current Implementation:**
- Cartesia TTS
- LiveKit audio streaming
- Basic audio routing

**Output:** Natural-sounding audio responses

## Implementation Strategy

### Phase 1: Thalamus Integration
**Goal:** Implement transcript refinement to solve voice detection issues

**Tasks:**
1. Extract refinement logic from sanctum-thalamus
2. Adapt for real-time voice agent processing
3. Implement session-based state management
4. Add speaker-aware segment grouping
5. Integrate with existing STT pipeline

**Expected Outcomes:**
- ✅ Eliminate "getting cut off" issues
- ✅ Prevent TTS interruption problems
- ✅ Consistent voice detection
- ✅ Better sentence completion

### Phase 2: Broca Integration
**Goal:** Implement robust message routing and caching

**Tasks:**
1. Extract queue management from broca
2. Implement message deduplication caching
3. Add user context management
4. Integrate retry logic and error handling
5. Connect to existing VPS Letta integration

**Expected Outcomes:**
- ✅ Eliminate VPS timeout issues
- ✅ Prevent duplicate message processing
- ✅ Robust error handling and recovery
- ✅ Proper user context management

### Phase 3: Pipeline Integration
**Goal:** Connect all layers into cohesive audio processing pipeline

**Tasks:**
1. Integrate Thalamus with Broca
2. Optimize data flow between layers
3. Add comprehensive logging and monitoring
4. Implement performance tuning
5. Add configuration management

**Expected Outcomes:**
- ✅ Complete audio processing pipeline
- ✅ Production-ready voice agent
- ✅ Scalable architecture
- ✅ Comprehensive monitoring

## Benefits of This Architecture

### Technical Benefits
- **Separation of Concerns:** Each layer handles specific responsibilities
- **Fault Tolerance:** Failures in one layer don't crash the entire system
- **Scalability:** Layers can be optimized and scaled independently
- **Maintainability:** Clear boundaries make debugging and updates easier

### User Experience Benefits
- **Natural Conversations:** No more cutting off or interruptions
- **Consistent Performance:** Reliable voice detection and processing
- **Fast Responses:** Optimized pipeline reduces latency
- **High Quality:** Refined audio processing improves accuracy

### Development Benefits
- **Modular Design:** Easy to test and modify individual components
- **Reusable Components:** Layers can be used in other audio applications
- **Clear Interfaces:** Well-defined data flow between layers
- **Extensible:** Easy to add new features or modify existing ones

## Configuration Requirements

### Thalamus Configuration
```python
THALAMUS_CONFIG = {
    "min_segments_for_grouping": 2,
    "inactivity_timeout_seconds": 1.5,
    "sentence_completion_threshold": 0.8,
    "noise_filtering_enabled": True,
    "speaker_diarization_enabled": True
}
```

### Broca Configuration
```python
BROCA_CONFIG = {
    "max_cache_size": 1000,
    "queue_retry_attempts": 3,
    "queue_retry_delay": 2.0,
    "user_context_timeout": 300,
    "platform_routing_enabled": True
}
```

### Pipeline Configuration
```python
PIPELINE_CONFIG = {
    "thalamus_enabled": True,
    "broca_enabled": True,
    "voicebox_enabled": True,
    "debug_logging": True,
    "performance_monitoring": True
}
```

## Success Metrics

### Voice Detection Quality
- **Sentence Completion Rate:** >95% of sentences captured completely
- **False Trigger Rate:** <5% of TTS responses trigger new input
- **Detection Consistency:** <100ms variance in detection timing

### System Performance
- **End-to-End Latency:** <2 seconds from speech to response
- **Error Rate:** <1% of messages fail processing
- **Timeout Rate:** <0.1% of requests timeout

### User Experience
- **Conversation Flow:** Natural, uninterrupted conversations
- **Response Quality:** Contextually appropriate responses
- **Audio Quality:** Clear, natural-sounding TTS output

## Next Steps

1. **Review and Approve:** Validate this architecture approach
2. **Phase 1 Planning:** Detailed implementation plan for Thalamus integration
3. **Resource Allocation:** Determine development timeline and resources
4. **Prototype Development:** Build proof-of-concept implementation
5. **Testing and Validation:** Comprehensive testing of each layer
6. **Production Deployment:** Roll out to production voice agent

---

*This architecture represents a fundamental shift from direct audio processing to a sophisticated, multi-layer pipeline that addresses the core issues with real-time voice agent interactions.*
