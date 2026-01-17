import { BarVisualizer, useVoiceAssistant } from '@livekit/components-react'

export function AudioVisualizer() {
  const { state, audioTrack } = useVoiceAssistant()

  return (
    <div className="audio-visualizer">
      <BarVisualizer state={state} barCount={5} trackRef={audioTrack} />
      <p>{state}</p>
    </div>
  )
}
