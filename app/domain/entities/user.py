from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4


@dataclass(slots=True, frozen=True)
class User:
    """
    Pure Domain Entity representing a User.
    Separates internal identity (UUID) from external identity (Spotify ID).
    """
    spotify_id: str
    display_name: str
    email: Optional[str] = None
    country: Optional[str] = None
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        if not self.spotify_id.strip():
            raise ValueError("spotify_id cannot be empty")
        
        if not self.display_name.strip():
            raise ValueError("display_name cannot be empty")

    @property
    def has_email(self) -> bool:
        return self.email is not None

    def __str__(self) -> str:
        return f"User({self.display_name}, internal_id={self.id})"