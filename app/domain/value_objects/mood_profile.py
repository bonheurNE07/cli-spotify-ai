from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MoodProfile:
    target_energy: float
    target_valence: float
    target_danceability: float

    def __post_init__(self) -> None:
        for field in (
            "target_energy",
            "target_valence",
            "target_danceability",
        ):
            value = getattr(self, field)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{field} must be between 0.0 and 1.0")