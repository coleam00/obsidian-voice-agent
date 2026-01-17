interface Props {
  isConnected: boolean
  isMuted: boolean
  onConnect: () => void
  onDisconnect: () => void
  onToggleMute: () => void
}

export function VoiceControls({ isConnected, isMuted, onConnect, onDisconnect, onToggleMute }: Props) {
  return (
    <div className="voice-controls">
      {isConnected ? (
        <>
          <button onClick={onToggleMute}>{isMuted ? 'Unmute' : 'Mute'}</button>
          <button onClick={onDisconnect}>Disconnect</button>
        </>
      ) : (
        <button onClick={onConnect}>Connect</button>
      )}
    </div>
  )
}
