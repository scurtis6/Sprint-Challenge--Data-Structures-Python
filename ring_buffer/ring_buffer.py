from doubly_linked_list import DoublyLinkedList 

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = 0

    def append(self, item):
        # if length is less than capacity
        if self.storage.length < self.capacity:
            # add item to the tail
            self.storage.add_to_tail(item)
            # set current to current the tail
            self.current = self.storage.tail
        # if current is tail
        if self.current == self.storage.tail:
            # set current to the head
            self.current = self.storage.head
        # if current is head
        # elif self.current == self.storage.head:
        else:
            # set the current to the next value
            self.current = self.current.next
        self.current.value = item

    def get(self):
        # make a list
        list_ring_buffer = []
        # set the current
        current = self.storage.head
        # if current, loop
        while current:
            # add current value to list
            list_ring_buffer.append(current.value)
            # get the next value in the list
            current = current.next
        # return the list
        return list_ring_buffer