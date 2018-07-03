import unittest
from queue import Queue

class TestQueue(unittest.TestCase):

    def test_that_returns_true_if_queue_is_empty(self):
        queue_list = []
        queue = Queue(queue_list)

        self.assertTrue(queue.is_empty())

    def test_that_element_added_to_array(self):
        queue_list = []
        queue = Queue(queue_list)
        queue.enqueue('banana')

        self.assertEqual(queue.queue_list, ['banana'])

if __name__ == '__main__':
    unittest.main()
