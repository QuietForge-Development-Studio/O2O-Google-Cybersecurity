interface TranscriptFetcher {
  fetchTranscript(elementId: string): Promise<Transcript>
  isFetched(elementId: string): boolean
}
