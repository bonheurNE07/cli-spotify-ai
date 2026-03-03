import pytest

from app.domain.value_objects.track_features import TrackFeatures

def test_valid_track_features() -> None:
    features = TrackFeatures(
        danceability=0.5,
        energy=0.8,
        loudness=-5.0,
        speechiness=0.05,
        acousticness=0.1,
        instrumentalness=0.0,
        liveness=0.2,
        valence=0.6,
        tempo=120.0
    )
    assert features.danceability == 0.5
    assert features.tempo == 120.0
    
def test_invalid_track_features() -> None:
    with pytest.raises(ValueError):
        TrackFeatures(
            danceability=1.5,
            energy=0.8,
            loudness=-5.0,
            speechiness=0.05,
            acousticness=0.1,
            instrumentalness=0.0,
            liveness=0.2,
            valence=0.6,
            tempo=120.0
        )