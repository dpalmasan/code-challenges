import heappq


class Queue:
    def __init__(self):
        self._elements = []
        self._min = None
        self._min_heap = []

    def enqueue(self, val: int):
        """(1, 3, 4, -100)

        Cola:
        1 (min = 1)
        3 (min = 1)
        4 (min = 1)
        -100 (min = -100)

        :param val: [description]
        :type val: int
        """
        heappq.heappush(self._min_heap, val)
        if self._min is None:
            self._min = val
        else:
            self._min = min(val, self._elements[-1])

        self._elements.insert(0, val)

    def dequeue(self) -> int:
        if self._elements:
            val = self._elements.pop()
            if val == self._min:
                self._min_linear_search()

        raise RuntimeError("Empty queue!")

    def _min_linear_search(self):
        min_val = self._elements[0]
        for el in self._elements:
            min_val = min(min_val, el)
        return min_val

    def get_min(self) -> int:
        """Complexity: O(N)

        O(1)

        :return: [description]
        :rtype: int
        """
        return self._min

    def get_first(self) -> int:
        return self._elements[-1]

    @property
    def elements(self):
        return self._elements


def test_queue():
    queue = Queue()
    for num in (3, 5, 8, 9, 10, -100):
        queue.enqueue(num)

    assert queue.dequeue() == 3
    assert queue.get_min() == -100
    assert queue.get_first() == 5
    assert queue.dequeue() == 5

    print(queue.elements)
    print(queue.dequeue())


test_queue()
