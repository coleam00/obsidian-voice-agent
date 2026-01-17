import { useState, FormEvent } from 'react'
import { VoiceAgent } from './components/VoiceAgent'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

export default function App() {
  const [mode, setMode] = useState<'text' | 'voice'>('text')
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  const sendMessage = async (e: FormEvent) => {
    e.preventDefault()
    if (!input.trim() || loading) return

    const userMessage = input.trim()
    setInput('')
    setMessages((prev) => [...prev, { role: 'user', content: userMessage }])
    setLoading(true)

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage }),
      })
      const data = await response.json()
      setMessages((prev) => [...prev, { role: 'assistant', content: data.response }])
    } catch {
      setMessages((prev) => [...prev, { role: 'assistant', content: 'Error: Failed to get response' }])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="chat-container">
      <h1>Obsidian Voice Agent</h1>
      <div className="mode-toggle">
        <button className={mode === 'text' ? 'active' : ''} onClick={() => setMode('text')}>Text</button>
        <button className={mode === 'voice' ? 'active' : ''} onClick={() => setMode('voice')}>Voice</button>
      </div>
      {mode === 'voice' ? (
        <VoiceAgent />
      ) : (
        <>
          <div className="messages">
            {messages.map((msg, i) => (
              <div key={i} className={`message ${msg.role}`}>
                <strong>{msg.role === 'user' ? 'You' : 'Agent'}:</strong> {msg.content}
              </div>
            ))}
            {loading && <div className="message assistant loading">Thinking...</div>}
          </div>
          <form onSubmit={sendMessage} className="input-form">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask about your notes..."
              disabled={loading}
            />
            <button type="submit" disabled={loading || !input.trim()}>
              Send
            </button>
          </form>
        </>
      )}
    </div>
  )
}
