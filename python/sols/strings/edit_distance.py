"""Edit distance implementation module."""

def one_edit_apart(s1: str, s2: str) -> bool:
    """Check if two strings are one edit apart.

    The possible operations to consider are:

    - Insert
    - Replace
    - Remove

    If using one of these operations we can convert string ``s1`` in string
    ``s2`` then the function returns True, otherwise it will return False.

    :param s1: Input string 1
    :type s1: str
    :param s2: Input string 2
    :type s2: str
    :return: True if strings are one edit apart, False otherwise
    :rtype: bool
    """
    len_diff = abs(len(s1) - len(s2))

    # To be one edit apart this is required
    if len_diff > 1:
        return False

    # Making s1' as the largest string
    if len(s1) > len(s2):
        s1p = s1
        s2p = s2
    else:
        s1p = s2
        s2p = s1

    # Base case, if s1' is one char then we now distance is 1
    if len(s1p) == 1:
        return True

    diffs = 0

    # For corner cases like "cat" "at", we check the first character.
    s1_idx = 1 if s1p[0] != s2p[0] else 0
    for s2_idx, c in enumerate(s2p):
        if s1_idx < len(s1p) and c != s1p[s1_idx]:
            # This is for corner cases like "cat" "ca"
            if diffs < 1 and len_diff > 0:
                s1_idx += 1
            diffs += 1
        s1_idx += 1

    # If we found less or 1 difference, then strings are one edit apart
    return diffs <= 1
