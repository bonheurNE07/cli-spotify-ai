from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True)
class Track:
    id: str
    name: str
    artist: str
    duration_ms: int
    popularity: int
    preview_url: Optional[str] = None
    
    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError("Track id cannot be empty")
        
        if self.duration_ms <= 0:
            raise ValueError("duration_ms must be positive")
        
        if not (0 <= self.popularity <= 100):
            raise ValueError("popularity must be between 0 and 100")
        
    @property
    def duration_seconds(self) -> float:
        return self.duration_ms / 1000.0
        