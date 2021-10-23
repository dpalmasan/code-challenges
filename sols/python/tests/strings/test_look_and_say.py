"""Look and say tests."""
from code_challenges.strings.look_and_say import next_sequence


def test_next_sequence():
    """Test sample cases."""
    assert next_sequence("1") == "11"
    assert next_sequence("11") == "21"
    assert next_sequence("21") == "1211"
    assert next_sequence("31131211131221") == "13211311123113112211"
