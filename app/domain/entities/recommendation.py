from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from app.domain.entities.track import Track


@dataclass(slots=True, frozen=True)
class RecommendationResult:
    """
    Entity representing an AI-generated music recommendation.
    """

    mood: str
    recommended_tracks: list[Track]
    confidence_score: float = 0.0
    generated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        if not self.mood.strip():
            raise ValueError("Mood cannot be empty")

        if not (0.0 <= self.confidence_score <= 1.0):
            raise ValueError("confidence_score must be between 0 and 1")

    def top(self, n: int) -> list[Track]:
        """Returns the top N recommended tracks."""
        if n < 0:
            return []
        return self.recommended_tracks[:n]

    @property
    def is_empty(self) -> bool:
        return len(self.recommended_tracks) == 0

    @property
    def total_recommendations(self) -> int:
        return len(self.recommended_tracks)
