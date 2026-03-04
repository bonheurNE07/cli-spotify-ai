from abc import ABC, abstractmethod


class LyricsRepository(ABC):
    @abstractmethod
    def get_lyrics(self, artist: str, title: str) -> str | None:
        """Fetch lyrics for a given artist and track title."""
        raise NotImplementedError
