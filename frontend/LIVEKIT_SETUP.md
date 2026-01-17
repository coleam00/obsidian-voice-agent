# LiveKit React Components Installation & Usage

## Install Dependencies

```bash
npm install @livekit/components-react livekit-client
# or
pnpm add @livekit/components-react livekit-client
```

## Package.json Dependencies to Add

```json
{
  "dependencies": {
    "@livekit/components-react": "^2.0.0",
    "livekit-client": "^2.0.0"
  }
}
```

## Key Components Explained

### 1. LiveKitRoom Setup
- `connect={true}` - Auto-connect on mount
- `audio={true}` - Enable audio
- `video={false}` - Disable video for voice-only

### 2. useVoiceAssistant Hook
- Returns `{ state, audioTrack }` 
- `state` values: 'disconnected', 'connecting', 'connected', 'speaking', 'listening'
- `audioTrack` is the audio track reference for visualization

### 3. Connect/Disconnect Controls
- Use `room.connect()` and `room.disconnect()`
- Check `room.state` for connection status

### 4. Mute Controls
- Access via `room.localParticipant.getTrackPublication('microphone')`
- Use `setMuted(true/false)` to control mute state

### 5. BarVisualizer Props
- `trackRef` - Audio track reference from useVoiceAssistant
- `barCount` - Number of bars (default: 20)
- `minHeight/maxHeight` - Bar height range
- `accentColor/accentShade` - Color customization
- `frequencies` - Frequency bands to visualize

### 6. RPC Handlers
- Register with `registerRpcMethod(methodName, handler)`
- Send with `performRpc({ destinationIdentity, method, payload })`
- Handle responses and errors appropriately

## CSS Styling (Optional)

```css
.voice-assistant-interface {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem;
}

.controls {
  display: flex;
  gap: 0.5rem;
}

.visualizer {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.connect { background: #4CAF50; }
.disconnect { background: #f44336; }
.muted { background: #ff9800; }
.unmuted { background: #2196F3; }
```