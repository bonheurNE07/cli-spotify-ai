from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from app.domain.entities.track import Track


@dataclass(slots=True)
class Playlist:
    """
    Pure Domain Entity representing a collection of tracks.

    Attributes:
        spotify_id: External Spotify identifier.
        name: Playlist name.
        owner_id: Internal UUID or Spotify ID of the owner.
        tracks: List of Track entities.
        id: Internal system UUID.
    """

    spotify_id: str
    name: str
    owner_id: str
    tracks: list[Track] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not self.spotify_id.strip():
            raise ValueError("spotify_id cannot be empty")
        if not self.name.strip():
            raise ValueError("Playlist name cannot be empty")

    def add_track(self, track: Track) -> None:
        """Adds a track to the playlist if it's not already present."""
        if track not in self.tracks:
            self.tracks.append(track)

    @property
    def total_duration_ms(self) -> int:
        """Calculates total duration of all tracks in milliseconds."""
        return sum(track.duration_ms for track in self.tracks)

    @property
    def total_tracks(self) -> int:
        """Returns the number of tracks in the playlist."""
        return len(self.tracks)

    def __str__(self) -> str:
        return f"Playlist({self.name}, {self.total_tracks} tracks)"
