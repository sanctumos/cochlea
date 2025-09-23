# Troubleshooting Guide

*Sanctum Cochlea is a fork of the letta-voice experiment, evolved into a comprehensive voice agent platform.*

This guide covers common issues and their solutions when setting up and running Sanctum Cochlea.

## Quick Diagnosis

Before diving into specific issues, run these diagnostic commands:

```bash
# Check Python version
python --version

# Check if dependencies are installed
pip list | grep -E "(letta|livekit|deepgram|cartesia)"

# Check environment variables
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Environment loaded:', bool(os.getenv('LETTA_API_KEY')))"
```

## Common Issues and Solutions

### 1. Import Errors

#### Problem: ModuleNotFoundError
```
ModuleNotFoundError: No module named 'letta_client'
```

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or install specific package
pip install letta-client
```

#### Problem: Version Conflicts
```
ImportError: cannot import name 'X' from 'Y'
```

**Solution:**
```bash
# Check installed versions
pip list | grep package_name

# Upgrade to compatible version
pip install --upgrade package_name
```

### 2. Environment Variable Issues

#### Problem: Variables Not Loading
```
KeyError: 'LETTA_API_KEY'
```

**Solutions:**
1. **Check .env file location** - Must be in project root
2. **Verify file syntax** - No spaces around `=`
3. **Check file permissions** - Ensure readable
4. **Restart application** - Environment changes require restart

**Debug commands:**
```bash
# Check if .env exists
ls -la .env

# Test environment loading
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API Key:', os.getenv('LETTA_API_KEY', 'NOT SET'))"
```

#### Problem: Wrong Variable Values
```
ValueError: Invalid API key format
```

**Solutions:**
1. **Copy-paste carefully** - No extra spaces or quotes
2. **Verify in service dashboard** - Check if key is active
3. **Test API key separately** - Use curl or Postman

### 3. Connection Issues

#### Problem: Connection Refused
```
ConnectionRefusedError: [Errno 111] Connection refused
```

**For Letta Cloud:**
- Check internet connection
- Verify service status at [Letta Status](https://status.letta.com)
- Ensure API key is valid

**For Self-Hosted:**
```bash
# Check if Docker container is running
docker ps | grep letta

# Check if port is exposed
netstat -tlnp | grep 8283

# Test connectivity
curl http://YOUR_VPS_IP:8283/health
```

#### Problem: SSL/TLS Errors
```
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED]
```

**Solutions:**
1. **Use HTTP for development** - `http://IP:8283/v1`
2. **Fix SSL certificate** - Ensure valid certificate
3. **Use reverse proxy** - Let nginx handle SSL

### 4. Authentication Issues

#### Problem: Invalid API Key
```
401 Unauthorized: Invalid API key
```

**Solutions:**
1. **Regenerate API key** in service dashboard
2. **Check key permissions** - Ensure correct scope
3. **Verify environment** - Development vs production keys
4. **Check key format** - No extra characters

#### Problem: Letta Authentication
```
Authentication failed: Invalid token
```

**For Self-Hosted:**
1. **Check Docker environment** - Ensure `OPENAI_API_KEY` is set
2. **Verify Letta configuration** - Check Docker logs
3. **Restart container** - `docker restart container_name`

### 5. LiveKit Connection Issues

#### Problem: WebSocket Connection Failed
```
WebSocket connection failed: Connection refused
```

**Solutions:**
1. **Verify LiveKit URL** - Check format and room name
2. **Check API credentials** - Key and secret must match
3. **Verify room exists** - Create room in LiveKit dashboard
4. **Check network** - Firewall blocking WebSocket connections

#### Problem: Room Access Denied
```
Access denied: Invalid room token
```

**Solutions:**
1. **Generate new room token** in LiveKit dashboard
2. **Check room permissions** - Ensure public or correct access
3. **Verify API key scope** - Must have room access permissions

### 6. Speech Service Issues

#### Problem: Deepgram STT Errors
```
DeepgramError: Invalid API key
```

**Solutions:**
1. **Check API key** - Verify in Deepgram dashboard
2. **Check quota** - Ensure sufficient credits
3. **Verify model** - Check if model is available
4. **Test separately** - Use Deepgram's test tools

#### Problem: Cartesia TTS Errors
```
CartesiaError: Text-to-speech failed
```

**Solutions:**
1. **Verify API key** - Check in Cartesia dashboard
2. **Check text format** - Ensure valid input
3. **Verify voice models** - Check available voices
4. **Test API directly** - Use Cartesia's API tester

### 7. Performance Issues

#### Problem: High Latency
```
LLM response time: 15.2 seconds
```

**Solutions:**
1. **Use faster model** - Switch to GPT-4o-mini
2. **Check network** - Ensure low latency to VPS
3. **Optimize prompts** - Reduce context length
4. **Use caching** - Enable response caching

#### Problem: Memory Issues
```
MemoryError: Not enough memory
```

**Solutions:**
1. **Reduce batch size** - Process fewer items at once
2. **Use smaller models** - Switch to lighter AI models
3. **Optimize code** - Reduce memory allocations
4. **Increase system memory** - Add more RAM to VPS

## Debug Mode

Enable debug logging to get more detailed error information:

```bash
# Set debug environment variable
export DEBUG=True
export LOG_LEVEL=DEBUG

# Or add to .env file
DEBUG=True
LOG_LEVEL=DEBUG
```

## Network Diagnostics

### Test Connectivity
```bash
# Test Letta connection
curl -v http://YOUR_VPS_IP:8283/health

# Test LiveKit connection
curl -v https://YOUR_ROOM.livekit.cloud

# Test DNS resolution
nslookup YOUR_VPS_IP
```

### Check Firewall
```bash
# Check if port is open
telnet YOUR_VPS_IP 8283

# Check firewall rules (Linux)
sudo iptables -L

# Check firewall rules (Windows)
netsh advfirewall firewall show rule name=all
```

## Docker Troubleshooting

### Container Issues
```bash
# Check container status
docker ps -a

# View container logs
docker logs container_name

# Restart container
docker restart container_name

# Remove and recreate container
docker rm -f container_name
docker run [your-docker-command]
```

### Volume Issues
```bash
# Check volume mounts
docker volume ls

# Inspect volume
docker volume inspect volume_name

# Remove corrupted volume
docker volume rm volume_name
```

## System Requirements

### Minimum Requirements
- **Python**: 3.10+
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 10GB free space
- **Network**: Stable internet connection

### Recommended Requirements
- **Python**: 3.11+
- **RAM**: 16GB+
- **Storage**: SSD with 50GB+ free space
- **Network**: Low-latency connection (<50ms to VPS)

## Getting Help

### Before Asking for Help
1. **Check this guide** - Your issue might be covered
2. **Enable debug logging** - Get more detailed error information
3. **Test with minimal setup** - Isolate the problem
4. **Check service status** - External services might be down

### When Asking for Help
Include:
- **Error message** - Full error traceback
- **Environment details** - OS, Python version, dependencies
- **Configuration** - Relevant parts of .env (no sensitive data)
- **Steps to reproduce** - What you did and what happened
- **Debug output** - Logs with debug mode enabled

### Resources
- **Letta Documentation**: [docs.letta.com](https://docs.letta.com)
- **LiveKit Documentation**: [docs.livekit.io](https://docs.livekit.io)
- **Deepgram Documentation**: [developers.deepgram.com](https://developers.deepgram.com)
- **Cartesia Documentation**: [docs.cartesia.ai](https://docs.cartesia.ai)

## Prevention

### Best Practices
1. **Use version control** - Track configuration changes
2. **Test in stages** - Verify each component separately
3. **Monitor resources** - Watch CPU, memory, and network usage
4. **Regular updates** - Keep dependencies and system updated
5. **Backup configurations** - Save working configurations

### Monitoring
```bash
# Monitor system resources
htop
iotop
nethogs

# Monitor Docker resources
docker stats

# Monitor application logs
tail -f application.log
```

## Next Steps

After resolving your issue:
1. **Document the solution** - Help others with similar problems
2. **Implement monitoring** - Prevent future issues
3. **Optimize performance** - Improve user experience
4. **Set up alerts** - Get notified of problems early

See the [VPS Connection Guide](vps-connection.md) for self-hosting setup or the [Environment Configuration](environment.md) for configuration details. 