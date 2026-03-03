from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class TrackFeatures:
    danceability: float
    energy: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float

    def __post_init__(self) -> None:
        for field_name in (
            "danceability",
            "energy",
            "speechiness",
            "acousticness",
            "instrumentalness",
            "liveness",
            "valence",
        ):
            value = getattr(self, field_name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{field_name} must be a number between 0.0 and 1.0")

        if self.tempo < 0:
            raise ValueError("tempo must be a non-negative value")
