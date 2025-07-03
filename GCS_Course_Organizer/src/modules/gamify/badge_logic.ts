enum Badge { None, Bronze, Silver, Gold }
interface BadgeEngine {
  update(noteChars: number, matchedCount: number, totalTerms: number): Badge
  onBadgeChange(callback: (badge: Badge)=>void): void
}