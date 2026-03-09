import pytest

from app.domain.value_objects.recommendation_score import RecommendationScore


def test_invalid_score_low():
    with pytest.raises(ValueError):
        RecommendationScore(-0.1)


def test_invalid_score_high():
    with pytest.raises(ValueError):
        RecommendationScore(1.5)


def test_valid_score():
    score = RecommendationScore(0.7)
    assert score.value == 0.7


def test_score_ordering():
    low = RecommendationScore(0.2)
    high = RecommendationScore(0.9)

    assert high > low
