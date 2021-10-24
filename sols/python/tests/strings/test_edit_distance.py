"""Edit distance implementation tests."""
from code_challenges.strings.edit_distance import one_edit_apart


def test_one_edit_apart():
    """Test cases for one edit apart problem."""
    assert one_edit_apart("cat", "cat")
    assert not one_edit_apart("c", "cat")
    assert one_edit_apart("cat", "cut")
    assert one_edit_apart("cat", "at")
    assert one_edit_apart("ca", "cat")
    assert not one_edit_apart("cat", "dog")
    assert one_edit_apart("c", "")
