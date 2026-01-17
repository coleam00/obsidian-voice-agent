import { useState, useCallback, useEffect } from 'react'
import { LiveKitRoom, RoomAudioRenderer, useRoomContext } from '@livekit/components-react'
import '@livekit/components-styles'
import { VoiceControls } from './VoiceControls'
import { AudioVisualizer } from './AudioVisualizer'
import { ReferencedFiles } from './ReferencedFiles'
import { useReferencedFiles, FileReference } from '../hooks/useReferencedFiles'

const LIVEKIT_URL = import.meta.env.VITE_LIVEKIT_URL || 'wss://localhost:7880'

function RoomContent() {
  const room = useRoomContext()
  const [isMuted, setIsMuted] = useState(false)
  const { referencedFiles, addReference, clearReferences } = useReferencedFiles()

  useEffect(() => {
    room.localParticipant.registerRpcMethod('showReferencedFiles', async (data) => {
      const payload = JSON.parse(data.payload)
      payload.files?.forEach((f: FileReference) => addReference(f))
      return ''
    })
    return () => {
      room.localParticipant.unregisterRpcMethod('showReferencedFiles')
    }
  }, [room, addReference])

  const toggleMute = useCallback(async () => {
    await room.localParticipant.setMicrophoneEnabled(isMuted)
    setIsMuted(!isMuted)
  }, [room, isMuted])

  const disconnect = useCallback(() => {
    room.disconnect()
    clearReferences()
  }, [room, clearReferences])

  return (
    <>
      <RoomAudioRenderer />
      <AudioVisualizer />
      <VoiceControls
        isConnected={true}
        isMuted={isMuted}
        onConnect={() => {}}
        onDisconnect={disconnect}
        onToggleMute={toggleMute}
      />
      <ReferencedFiles files={referencedFiles} />
    </>
  )
}

export function VoiceAgent() {
  const [token, setToken] = useState<string | null>(null)
  const [isConnecting, setIsConnecting] = useState(false)

  const connect = useCallback(async () => {
    setIsConnecting(true)
    try {
      const roomName = `room-${Date.now()}`
      const res = await fetch('/api/livekit-token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ room_name: roomName, participant_name: 'user' }),
      })
      const data = await res.json()
      setToken(data.token)
    } finally {
      setIsConnecting(false)
    }
  }, [])

  if (!token) {
    return (
      <div className="voice-container">
        <VoiceControls
          isConnected={false}
          isMuted={false}
          onConnect={connect}
          onDisconnect={() => {}}
          onToggleMute={() => {}}
        />
        {isConnecting && <p>Connecting...</p>}
      </div>
    )
  }

  return (
    <div className="voice-container">
      <LiveKitRoom
        serverUrl={LIVEKIT_URL}
        token={token}
        connect={true}
        audio={true}
        onDisconnected={() => setToken(null)}
      >
        <RoomContent />
      </LiveKitRoom>
    </div>
  )
}
