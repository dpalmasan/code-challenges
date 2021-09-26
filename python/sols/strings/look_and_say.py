"""Look and say problem."""


def next_sequence(seq: str) -> str:
    """Get next string for the look and say.

    For example, if input is ``11``, this function will return
    ``21`` because it is read as ``two ones``.

    :param seq: Input sequence
    :type seq: str
    :return: Look and say result
    :rtype: str
    """
    curr_val = seq[0]
    count = 0
    output = ""
    for char in seq:
        if char == curr_val:
            count += 1
        else:
            output += f"{count}{curr_val}"
            count = 1
            curr_val = char

    if count > 0:
        output += f"{count}{curr_val}"
    return output


def look_and_say_seq(n: int):
    """Print look and say sequence up to ``n`` element.

    :param n: The number of elements to be printed.
    :type n: int
    """
    curr_seq = "1"
    for i in range(0, n):
        print(curr_seq)
        curr_seq = next_sequence(curr_seq)
