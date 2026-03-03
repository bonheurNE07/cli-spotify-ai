from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta


@dataclass(slots=True, frozen=True)
class SpotifyToken:
    access_token: str
    token_type: str
    expires_in: int
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        if not self.access_token.strip():
            raise ValueError("access_token cannot be empty")

        if self.expires_in <= 0:
            raise ValueError("expires_in must be a positive integer")

        if self.created_at.tzinfo is None:
            raise ValueError("created_at must be timezone-aware")

    @property
    def expires_at(self) -> datetime:
        return self.created_at + timedelta(seconds=self.expires_in)

    def is_expired(self, now: datetime | None = None) -> bool:
        if now is None:
            now = datetime.now(UTC)

        if now.tzinfo is None:
            raise ValueError("now must be timezone-aware")

        return now >= self.expires_at
