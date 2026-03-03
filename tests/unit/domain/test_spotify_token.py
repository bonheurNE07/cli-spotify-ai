from datetime import UTC, datetime, timedelta

import pytest

from app.domain.value_objects.spotify_token import SpotifyToken


def test_token_expiration_logic() -> None:
    created_at = datetime.now(UTC)

    token = SpotifyToken(
        access_token="valid_token",
        token_type="Bearer",
        expires_in=3600,
        created_at=created_at,
    )

    assert token.is_expired(created_at) is False

    future = created_at + timedelta(hours=2)
    assert token.is_expired(future) is True


def test_invalid_token() -> None:
    created_at = datetime.now(UTC)

    with pytest.raises(ValueError):
        SpotifyToken(
            access_token="", token_type="Bearer", expires_in=3600, created_at=created_at
        )
