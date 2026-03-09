import pytest

from app.domain.entities.track import Track
from app.domain.services.euclidean_scoring_strategy import EuclideanScoringStrategy
from app.domain.value_objects.mood_profile import MoodProfile
from app.domain.value_objects.track_features import TrackFeatures


def test_energy_weight_dominates():
    strategy = EuclideanScoringStrategy(
        energy_weight=10,
        valence_weight=1,
        danceability_weight=1,
    )

    mood = MoodProfile(
        target_energy=1,
        target_valence=0,
        target_danceability=0,
    )

    features = TrackFeatures(
        energy=0,
        valence=0,
        danceability=0,
        acousticness=0,
        instrumentalness=0,
        liveness=0,
        speechiness=0,
        tempo=120,
        loudness=-5,
    )

    track = Track(
        id="1",
        name="test",
        artist="artist",
        duration_ms=200000,
        popularity=50,
        features=features,
    )

    score = strategy.score(mood, track)

    assert score.value < 0.5


def test_extreme_weights():
    strategy = EuclideanScoringStrategy(
        energy_weight=100,
        valence_weight=1,
        danceability_weight=1,
    )

    assert strategy.energy_weight > strategy.valence_weight


def test_invalid_weights():
    with pytest.raises(ValueError):
        EuclideanScoringStrategy(
            energy_weight=0,
            valence_weight=1,
            danceability_weight=1,
        )
