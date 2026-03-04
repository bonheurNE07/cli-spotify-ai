from __future__ import annotations

from math import sqrt

from app.domain.entities.track import Track
from app.domain.services.recommendation_service import RecommendationService
from app.domain.value_objects.mood_profile import MoodProfile


class BasicSimilarityRecommendationService(RecommendationService):
    def score_track(
        self,
        track: Track,
        mood: MoodProfile,
    ) -> float:
        if track.features is None:
            raise ValueError("Track features are required to score a track")

        features = track.features

        energy_diff = features.energy - mood.target_energy
        valence_diff = features.valence - mood.target_valence
        danceability_diff = features.danceability - mood.target_danceability

        distance = sqrt(energy_diff**2 + valence_diff**2 + danceability_diff**2)

        max_distance = sqrt(3)  # Max possible distance in this 3D space

        similarity_score = 1 - (distance / max_distance)

        return similarity_score

    def rank_tracks(self, mood: MoodProfile, tracks: list[Track]) -> list[Track]:
        if not tracks:
            return []

        scored_tracks = [(track, self.score_track(track, mood)) for track in tracks]

        scored_tracks.sort(key=lambda item: item[1], reverse=True)

        return [track for track, _ in scored_tracks]
