class Queue(object):
    def __init__(self, queue_list):
        self.queue_list = queue_list

    def is_empty(self):
        if not self.queue_list:
            return True
