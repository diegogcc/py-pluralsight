'''
    '$ python3 -m pytest'

    '$ pytest --cov-report html:{report_folder} --cov={module_tested} {modules_folder}'
    '$ pytest --cov-report html:cov_html --cov=tennis .'
    {report_folder} is created
    check report_folder/index.html

    BRANCH COVERAGE:
    -Evaluates also partially covered lines
    For branch coverage add flag '--cov-branch'
    '$ pytest --cov-report html:{report_folder} --cov-branch --cov={module_tested} {modules_folder}'
    result:
        -"line 5 didn't jumpt to line 8, because the condition on line 5 was never false"
'''

import pytest

from tennis import score_tennis

'''
Install pip packages 'coverage' and 'pytest-cov'
'''

@pytest.mark.parametrize("player1_points, player2_points, expected_score",
                         [(0, 0, "Love-All"),
                          (1, 1, "Fifteen-All"),
                          (2, 2, "Thirty-All")
                          ])
def test_score_tennis(player1_points, player2_points, expected_score):
    assert score_tennis(player1_points, player2_points) == expected_score