from app.domain.entities.track import Track
from app.domain.services.basic_similarity_recommendation_service import (
    BasicSimilarityRecommendationService,
)
from app.domain.value_objects.mood_profile import MoodProfile
from app.domain.value_objects.track_features import TrackFeatures


def test_rank_tracks_empty_list() -> None:
    service = BasicSimilarityRecommendationService()
    mood = MoodProfile(target_energy=0.5, target_valence=0.5, target_danceability=0.5)
    ranked = service.rank_tracks(mood, [])

    assert ranked == []


def create_track(energy: float, valence: float, danceability: float) -> Track:
    return Track(
        id="1",
        name="Test Track",
        artist="Test Artist",
        duration_ms=200000,
        popularity=50,
        features=TrackFeatures(
            energy=energy,
            valence=valence,
            danceability=danceability,
            acousticness=0.0,
            instrumentalness=0.0,
            liveness=0.0,
            speechiness=0.0,
            tempo=120.0,
            loudness=-5.0,
        ),
    )


def test_rank_tracks_orders_by_similarity() -> None:
    service = BasicSimilarityRecommendationService()

    mood = MoodProfile(target_energy=0.8, target_valence=0.8, target_danceability=0.8)

    perfect_match = create_track(0.8, 0.8, 0.8)  # Perfect match
    medium_match = create_track(0.6, 0.6, 0.6)  # Close match
    bad_match = create_track(0.1, 0.1, 0.1)  # Distant match

    ranked = service.rank_tracks(
        mood,
        [bad_match, medium_match, perfect_match],
    )

    assert ranked[0] == perfect_match
    assert ranked[1] == medium_match
    assert ranked[2] == bad_match


def test_score_range() -> None:
    service = BasicSimilarityRecommendationService()

    mood = MoodProfile(
        target_energy=0.0,
        target_valence=0.0,
        target_danceability=0.0,
    )

    track = create_track(1.0, 1.0, 1.0)

    score = service.score_track(track, mood)

    assert 0.0 <= score <= 1.0
