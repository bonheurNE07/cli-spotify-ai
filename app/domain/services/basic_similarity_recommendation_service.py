from app.domain.entities.track import Track
from app.domain.services.recommendation_service import RecommendationService
from app.domain.services.track_scoring_strategy import TrackScoringStrategy
from app.domain.value_objects.mood_profile import MoodProfile


class BasicSimilarityRecommendationService(RecommendationService):
    def __init__(
        self,
        scoring_strategy: TrackScoringStrategy,
    ) -> None:
        self._scoring_strategy = scoring_strategy

    def score_track(
        self,
        track: Track,
        mood: MoodProfile,
    ) -> float:
        return self._scoring_strategy.score(mood, track)

    def rank_tracks(
        self,
        mood: MoodProfile,
        tracks: list[Track],
    ) -> list[Track]:
        if not tracks:
            return []

        scored_tracks = [(track, self.score_track(track, mood)) for track in tracks]

        scored_tracks.sort(
            key=lambda x: x[1],
            reverse=True,
        )

        return [track for track, _ in scored_tracks]
