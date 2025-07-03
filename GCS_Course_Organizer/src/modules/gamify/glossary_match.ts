interface GlossaryMatcher {
  match(transcript: Transcript, glossaryTerms: string[]): Set<string>
}
