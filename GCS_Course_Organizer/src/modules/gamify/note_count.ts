interface NoteTracker {
  onNoteChange(text: string): void
  getCharCount(): number
  onThresholdReached(callback: ()=>void): void
}
