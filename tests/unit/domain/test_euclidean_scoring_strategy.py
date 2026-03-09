import pytest

from app.domain.entities.track import Track
from app.domain.services.euclidean_scoring_strategy import (
    EuclideanScoringStrategy,
)
from app.domain.value_objects.mood_profile import MoodProfile
from app.domain.value_objects.track_features import TrackFeatures


@pytest.fixture
def strategy() -> EuclideanScoringStrategy:
    return EuclideanScoringStrategy()


def test_score_is_within_range(strategy: EuclideanScoringStrategy):
    mood = MoodProfile(
        target_energy=0.5,
        target_valence=0.5,
        target_danceability=0.5,
    )

    features = TrackFeatures(
        energy=0.2,
        valence=0.7,
        danceability=0.9,
        acousticness=0.0,
        instrumentalness=0.0,
        liveness=0.0,
        speechiness=0.0,
        tempo=120.0,
        loudness=-5.0,
    )

    track = Track(
        id="1",
        name="Test",
        artist="Artist",
        features=features,
        duration_ms=200000,
        popularity=50,
    )

    score = strategy.score(mood, track)

    assert 0.0 <= score <= 1.0


def test_perfect_match_returns_one(strategy: EuclideanScoringStrategy):
    mood = MoodProfile(
        target_energy=1.0,
        target_valence=1.0,
        target_danceability=1.0,
    )

    features = TrackFeatures(
        energy=1.0,
        valence=1.0,
        danceability=1.0,
        acousticness=0.0,
        instrumentalness=0.0,
        liveness=0.0,
        speechiness=0.0,
        tempo=120.0,
        loudness=-5.0,
    )

    track = Track(
        id="2",
        name="Perfect",
        artist="Artist",
        features=features,
        duration_ms=200000,
        popularity=50,
    )

    score = strategy.score(mood, track)

    assert score == pytest.approx(1.0)


def test_worst_match_returns_zero(strategy: EuclideanScoringStrategy):
    mood = MoodProfile(
        target_energy=1.0,
        target_valence=1.0,
        target_danceability=1.0,
    )

    features = TrackFeatures(
        energy=0.0,
        valence=0.0,
        danceability=0.0,
        acousticness=0.0,
        instrumentalness=0.0,
        liveness=0.0,
        speechiness=0.0,
        tempo=120.0,
        loudness=-5.0,
    )

    track = Track(
        id="3",
        name="Worst",
        artist="Artist",
        features=features,
        duration_ms=200000,
        popularity=50,
    )

    score = strategy.score(mood, track)
    assert score == pytest.approx(0.0)
