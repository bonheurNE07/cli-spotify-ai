from abc import ABC, abstractmethod

from app.domain.entities.track import Track
from app.domain.value_objects.mood_profile import MoodProfile

class RecommendationService(ABC):
    @abstractmethod
    def score_track(self, track: Track, mood: MoodProfile) -> float:
        """
        Calculate a score for how well a track matches a given mood profile.

        Higher scores indicate a better match.
        """
        raise NotImplementedError
    
    @abstractmethod
    def rank_tracks(
        self,
        mood: MoodProfile,
        tracks: list[Track],
    ) -> list[Track]:
        """
        Rank tracks according to how well they match the given mood profile.

        Returns tracks sorted from best match to worst match.
        """
        raise NotImplementedError