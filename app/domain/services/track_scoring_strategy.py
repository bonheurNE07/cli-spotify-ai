from abc import ABC, abstractmethod

from app.domain.entities.track import Track
from app.domain.value_objects.mood_profile import MoodProfile


class TrackScoringStrategy(ABC):
    @abstractmethod
    def score(
        self,
        mood: MoodProfile,
        track: Track,
    ) -> float:
        """
        Return similarity score between 0.0 and 1.0.
        """
        raise NotImplementedError
