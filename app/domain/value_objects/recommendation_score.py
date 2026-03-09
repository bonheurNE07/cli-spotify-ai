from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class RecommendationScore:
    value: float

    def __post_init__(self) -> None:
        if not (0.0 <= self.value <= 1.0):
            raise ValueError("Recommendation Score must be between 0.0 and 1.0")

    def __float__(self) -> float:
        return self.value

    def __repr__(self) -> str:
        return f"RecommandationScore({self.value:.3f})"
