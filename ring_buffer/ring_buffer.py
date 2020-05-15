from doubly_linked_list import DoublyLinkedList 

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = 0

    def append(self, item):
        if self.storage.length <self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.current.tail


    # need another method??
  
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