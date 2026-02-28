from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID, uuid4

@dataclass(slots=True)
class User:
    id: UUID = field(default_factory=uuid4)
    spotify_id: str = field(default="")
    email: Optional[str] = None
    display_name: Optional[str] = None
    
    def __post_init__(self):
        if not self.spotify_id:
            raise ValueError("spotify_id is required")
    
    def has_email(self) -> bool:
        return self.email is not None
    
    def has_display_name(self) -> bool:
        return self.display_name is not None
    