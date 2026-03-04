from abc import ABC, abstractmethod

from app.domain.entities.track import Track
from app.domain.value_objects.spotify_token import SpotifyToken
from app.domain.value_objects.track_features import TrackFeatures


class SpotifyRepository(ABC):
    @abstractmethod
    def get_token(self) -> SpotifyToken:
        """Retrieve a valid Spotify access token."""
        raise NotImplementedError

    @abstractmethod
    def get_track(self, track_id: str) -> Track:
        """Fetch track details by Spotify track ID."""
        raise NotImplementedError

    @abstractmethod
    def get_track_features(self, track_id: str) -> TrackFeatures:
        """Fetch track features by Spotify track ID."""
        raise NotImplementedError

    @abstractmethod
    def search_tracks(self, query: str, limit: int = 10) -> list[Track]:
        """Search for tracks matching a query string."""
        raise NotImplementedError
