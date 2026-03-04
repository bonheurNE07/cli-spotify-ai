from __future__ import annotations

from dataclasses import dataclass

from app.domain.value_objects.track_features import TrackFeatures


@dataclass(slots=True)
class Track:
    id: str
    name: str
    artist: str
    duration_ms: int
    popularity: int
    album_name: str | None = None
    preview_url: str | None = None
    features: TrackFeatures | None = None

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("Track id cannot be empty or whitespace")

        if not self.name.strip():
            raise ValueError("Track name cannot be empty or whitespace")

        if self.duration_ms <= 0:
            raise ValueError("duration_ms must be positive")

        if not (0 <= self.popularity <= 100):
            raise ValueError("popularity must be between 0 and 100")

    @property
    def duration_seconds(self) -> float:
        return self.duration_ms / 1000.0

    def __str__(self) -> str:
        return f"{self.artist} - {self.name} ({self.popularity}/100)"
