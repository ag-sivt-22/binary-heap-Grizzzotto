from dataclasses import dataclass

@dataclass
class Element:
    value: object
    prio: int

class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []

    def push(self, element):
        self.queue.append(element)
        self.heap_up(len(self.queue) - 1)

    def heap_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.queue[index] < self.queue[parent_index]:
                self.queue[index], self.queue[parent_index] = self.queue[parent_index], self.queue[index]
                index = parent_index
            else:
                break

    def pop(self):
        if not self.queue:
            return None
        if len(self.queue) == 1:
            return self.queue.pop()

        root = self.queue[0]
        self.queue[0] = self.queue.pop()
        self.heap_down(0)
        return root

    def heap_down(self, index):
        size = len(self.queue)
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index
            if left_child < size and self.queue[left_child] < self.queue[smallest]:
                smallest = left_child
            if right_child < size and self.queue[right_child] < self.queue[smallest]:
                smallest = right_child
            if smallest != index:
                self.queue[index], self.queue[smallest] = self.queue[smallest], self.queue[index]
                index = smallest
            else:
                break


pr = PriorityQueue()
pr.push(3)
pr.push(5)
pr.push(2)
pr.push(4)
pr.push(6)
pr.push(7)
pr.push(9)
pr.push(1)
print("heap:", pr.queue)
print("pop:", pr.pop())
print("heap:", pr.queue)
