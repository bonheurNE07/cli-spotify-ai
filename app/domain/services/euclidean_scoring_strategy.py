from math import sqrt

from app.domain.entities.track import Track
from app.domain.services.track_scoring_strategy import TrackScoringStrategy
from app.domain.value_objects.mood_profile import MoodProfile


class EuclideanScoringStrategy(TrackScoringStrategy):
    def __init__(
        self,
        energy_weight: float = 1.0,
        valence_weight: float = 1.0,
        danceability_weight: float = 1.0,
    ) -> None:

        weights = [energy_weight, valence_weight, danceability_weight]

        if any(w <= 0 for w in weights):
            raise ValueError("Weights must be positive numbers")

        total = sum(weights)

        self.energy_weight = energy_weight / total
        self.valence_weight = valence_weight / total
        self.danceability_weight = danceability_weight / total

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

        weighted_distance = sqrt(
            self.energy_weight * energy_diff**2
            + self.valence_weight * valence_diff**2
            + self.danceability_weight * dance_diff**2
        )

        max_distance = sqrt(
            self.energy_weight + self.valence_weight + self.danceability_weight
        )

        similarity = 1 - (weighted_distance / max_distance)

        return similarity
