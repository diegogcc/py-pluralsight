import pytest

from tennis import score_tennis

''' 
With duplication
'''
def test_0_0_score_tennis():
    assert score_tennis(0, 0) == "Love-All"

def test_1_1_score_tennis():
    assert score_tennis(1, 1) == "Fifteen-All"

def test_2_2_score_tennis():
    assert score_tennis(2, 2) == "Thirty-All"


'''
With parameterisation
'''
@pytest.mark.parametrize("player1_points, player2_points, expected_score",
                         [(0, 0, "Love-All"),
                          (1, 1, "Fifteen-All"),
                          (2, 2, "Thirty-All")
                          ])
def test_score_tennis(player1_points, player2_points, expected_score):
    assert score_tennis(player1_points, player2_points) == expected_score