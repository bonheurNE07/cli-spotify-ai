from datetime import UTC, datetime
from uuid import UUID

import pytest

from app.domain.entities import Playlist, RecommendationResult, Track, User


class TestTrackEntity:
    def test_track_creation_valid(self) -> None:
        track = Track(
            id="spotify:123",
            name="Midnight City",
            artist="M83",
            duration_ms=243000,
            popularity=85,
        )
        assert track.name == "Midnight City"
        assert track.duration_seconds == 243.0

    def test_track_validation_fails_on_negative_duration(self) -> None:
        with pytest.raises(ValueError, match="duration_ms must be positive"):
            Track("id", "Name", "Artist", -1, 50)


class TestUserEntity:
    def test_user_dual_id_strategy(self) -> None:
        user = User(spotify_id="sp_123", display_name="Dev")
        assert isinstance(user.id, UUID)
        assert user.spotify_id == "sp_123"
        assert user.created_at <= datetime.now(UTC)

    def test_user_missing_id_fails(self) -> None:
        # Change "is required" to "cannot be empty"
        with pytest.raises(ValueError, match="spotify_id cannot be empty"):
            User(spotify_id="  ", display_name="Dev")


class TestPlaylistEntity:
    def test_playlist_management(self) -> None:
        track = Track("t1", "Song", "Artist", 1000, 50)
        playlist = Playlist(spotify_id="p1", name="My List", owner_id="u1")

        playlist.add_track(track)
        assert playlist.total_tracks == 1
        assert playlist.total_duration_ms == 1000

        # Test idempotency (no duplicates)
        playlist.add_track(track)
        assert playlist.total_tracks == 1


class TestRecommendationEntity:
    def test_recommendation_top_n(self) -> None:
        tracks = [Track(f"id_{i}", f"Song {i}", "Artist", 100, 50) for i in range(5)]
        rec = RecommendationResult(
            mood="Happy", recommended_tracks=tracks, confidence_score=0.95
        )

        assert len(rec.top(3)) == 3
        assert rec.top(10) == tracks
        assert rec.top(-1) == []

    def test_invalid_confidence_score(self) -> None:
        with pytest.raises(
            ValueError, match="confidence_score must be between 0 and 1"
        ):
            RecommendationResult(
                "Sad", [Track("1", "S", "A", 1, 1)], confidence_score=1.5
            )
