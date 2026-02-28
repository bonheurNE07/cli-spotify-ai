from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .track import Track

@dataclass(slots=True)
class Playlist:
    id: str
    name: str
    tracks: List[Track] = field(default_factory=list)

    def add_track(self, track: Track) -> None:
        self.tracks.append(track)
        
    def total_duration_ms(self) -> int:
        return sum(track.duration_ms for track in self.tracks)
    
    def total_tracks(self) -> int:
        return len(self.tracks)