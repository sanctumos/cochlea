# Basic Setup Guide

*Sanctum Cochlea is a fork of the letta-voice experiment, evolved into a comprehensive voice agent platform.*

This guide covers the initial installation and basic configuration of Sanctum Cochlea.

## Prerequisites

- **Python 3.10 or higher**
- **Git** for cloning the repository
- **Virtual environment** (recommended)
- **Accounts with required services** (see below)

## Step 1: Clone and Install

```bash
# Clone the repository
git clone git@github.com:your-org/sanctum-cochlea.git
cd sanctum-cochlea

# Create and activate virtual environment
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Service Accounts Setup

You'll need accounts with these services:

### LiveKit
1. Go to [LiveKit Cloud](https://livekit.io/)
2. Create an account and get your API credentials
3. Note down your LiveKit URL, API key, and secret

### Deepgram
1. Visit [Deepgram](https://deepgram.com/)
2. Sign up and get your API key
3. This handles speech-to-text conversion

### Cartesia
1. Go to [Cartesia](https://cartesia.ai/)
2. Create an account and get your API key
3. This handles text-to-speech conversion

### Sanctum Instance (Required)
- **Self-Hosted Sanctum Instance** - You must have a working Sanctum instance configured with your preferred LLM provider
- See [VPS Connection Guide](vps-connection.md) for setup details

## Step 3: Environment Configuration

Create a `.env` file in your project root:

```bash
# Sanctum Instance Configuration
LETTA_API_KEY=your_sanctum_api_key_here
LETTA_BASE_URL=http://YOUR_SANCTUM_IP:8283/v1

# LiveKit Configuration
LIVEKIT_URL=wss://<YOUR-ROOM>.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

# Speech Services
DEEPGRAM_API_KEY=your_deepgram_api_key
CARTESIA_API_KEY=your_cartesia_api_key
```

## Step 4: Test the Setup

### Basic Test
```bash
# Run the development server
python main.py dev
```

You should see output indicating:
- Agent creation
- Agent ID assignment
- Worker app startup

### Common Issues
- **Import errors**: Ensure all dependencies are installed
- **Environment errors**: Check your `.env` file
- **API errors**: Verify your service credentials

## Step 5: Voice Testing

1. **Start the agent** (from previous step)
2. **Open LiveKit Agents Playground**: https://agents-playground.livekit.io/
3. **Connect to your room** using the credentials from your `.env`
4. **Test voice interaction**

## Project Structure

```
sanctum-cochlea/
├── main.py              # Main application entry point
├── function_call.py     # Example function calling implementation
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
└── docs/               # Documentation (this folder)
```

## Configuration Options

### Letta Agent Settings
The agent is created with these default settings:
- **Model**: GPT-4o-mini (for speed)
- **Embedding**: text-embedding-3-small
- **Memory**: Enabled with sleep-time management
- **Type**: voice_convo_agent

### Customization
You can modify these settings in `main.py`:
- Change the AI model
- Adjust memory settings
- Modify agent persona
- Configure sleep-time parameters

## Next Steps

After basic setup:
1. **Test voice interactions** in the playground
2. **Customize agent behavior** by modifying the code
3. **Set up self-hosting** (see [VPS Connection Guide](vps-connection.md))
4. **Deploy to production** with proper security

## Troubleshooting

### Common Setup Issues
- **Python version**: Ensure you're using Python 3.10+
- **Dependencies**: Run `pip install -r requirements.txt` again
- **Environment**: Check that `.env` file exists and has correct values
- **API keys**: Verify all service credentials are valid

### Getting Help
- Check the [troubleshooting guide](troubleshooting.md)
- Review [environment configuration](environment.md)
- Ensure proper [VPS setup](vps-connection.md) if self-hosting 