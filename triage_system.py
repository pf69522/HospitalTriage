import heapq


class TriageSystem:
    def __init__(self):
        self.__heap = []
        self.__arrival_counter = 0
        
    def add_patient(self, name, severity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a nonempty string.")

        if type(severity) is not int or not 1 <= severity <= 5:
            raise ValueError("Severity must be an integer from 1 to 5.")

        entry = (-severity, self.__arrival_counter, name)
        heapq.heappush(self.__heap, entry)
        self.__arrival_counter += 1

    def process_next(self):
        if self.is_empty():
            return None

        priority, arrival, name = heapq.heappop(self.__heap)
        return (name, -priority)

    def peek_next(self):
        if self.is_empty():
            return None

        priority, arrival, name = self.__heap[0]
        return (name, -priority)

    def is_empty(self):
        return len(self.__heap) == 0

    def size(self):
        return len(self.__heap)

    def clear(self):
        self.__heap.clear()