import { useState, useCallback } from 'react'

export interface FileReference {
  path: string
  title?: string
}

export function useReferencedFiles() {
  const [referencedFiles, setReferencedFiles] = useState<FileReference[]>([])

  const addReference = useCallback((file: FileReference) => {
    setReferencedFiles((prev) => {
      if (prev.some((f) => f.path === file.path)) return prev
      return [...prev, file]
    })
  }, [])

  const clearReferences = useCallback(() => {
    setReferencedFiles([])
  }, [])

  return { referencedFiles, addReference, clearReferences }
}
