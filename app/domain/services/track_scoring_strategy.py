from abc import ABC, abstractmethod

from app.domain.entities.track import Track
from app.domain.value_objects.mood_profile import MoodProfile
from app.domain.value_objects.recommendation_score import RecommendationScore


class TrackScoringStrategy(ABC):
    @abstractmethod
    def score(
        self,
        mood: MoodProfile,
        track: Track,
    ) -> RecommendationScore:
        """
        Return similarity score between 0.0 and 1.0.
        """
        raise NotImplementedError
