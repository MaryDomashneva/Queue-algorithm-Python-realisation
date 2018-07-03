import unittest
from queue import Queue

class TestQueue(unittest.TestCase):

    def test_that_returns_true_if_queue_is_empty(self):
        queue_list = []
        queue = Queue(queue_list)

        self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    unittest.main()
