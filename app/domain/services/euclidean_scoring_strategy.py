from math import sqrt

from app.domain.entities.track import Track
from app.domain.services.track_scoring_strategy import TrackScoringStrategy
from app.domain.value_objects.mood_profile import MoodProfile


class EuclideanScoringStrategy(TrackScoringStrategy):
    def score(
        self,
        mood: MoodProfile,
        track: Track,
    ) -> float:
        if track.features is None:
            raise ValueError("Track must contain features for scoring")

        features = track.features

        energy_diff = features.energy - mood.target_energy
        valence_diff = features.valence - mood.target_valence
        dance_diff = features.danceability - mood.target_danceability

        distance = sqrt(energy_diff**2 + valence_diff**2 + dance_diff**2)

        max_distance = sqrt(3)

        similarity = 1 - (distance / max_distance)

        return similarity
