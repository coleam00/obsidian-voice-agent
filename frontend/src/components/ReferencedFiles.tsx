import { FileReference } from '../hooks/useReferencedFiles'

interface Props {
  files: FileReference[]
}

export function ReferencedFiles({ files }: Props) {
  if (files.length === 0) return null

  return (
    <div className="referenced-files">
      <h3>Referenced Files</h3>
      <ul>
        {files.map((file) => (
          <li key={file.path}>{file.title || file.path}</li>
        ))}
      </ul>
    </div>
  )
}
