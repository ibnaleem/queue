class QueueEmptyError(Exception):
    def __init__(self, message: str) -> str:
        self.message = message

class QueueFullError(Exception):
    def __init__(self, message: str) -> str:
        self.message = message

class QueueError(Exception):
    def __init__(self, message: str) -> str:
        self.message = message

class Queue:
    def __init__(self, items: object = None, size: int = None) -> None:
        if isinstance(items, list):
            self.items = items
        elif items is None:
            self.items = []
        else:
            self.items = [items]  

        for item in self.items:
            if isinstance(item, list):
                raise QueueError("Queue cannot contain nested lists.")

        self.size = size if size else (len(self.items) + 1)
        self.head = self.items[0] if bool(self) else []
        self.tail = self.items[-1] if bool(self) else []

    def __len__(self) -> int:
        return len(self.items)

    def __bool__(self) -> bool:
        return bool(self.items)

    def __repr__(self) -> str:
        return str(self.items)

    def enqueue(self, item: object) -> object:

        if len(self) < self.size:
            if isinstance(item, list):
                self.items.extend(item)
            else:
                self.items.append(item)
        else:
            raise QueueFullError(f"Cannot enqueue at full size: {self.size}")

        return self.items

    def dequeue(self) -> object:

        if bool(self):
            self.items.pop(0)

        else:
            raise QueueEmptyError("Cannot dequeue from an empty queue.")

        return self.items

    def peek(self) -> object:

        if not bool(self):
            raise QueueEmptyError("Cannot peek from an empty queue.")

        return self.items[0]

    def clear(self) -> object:

        self.items = []
        return self.items

    def merge(self, queue: 'Queue') -> object:

        if bool(self) and bool(queue):
            self.enqueue(queue)

        else:
            raise QueueEmptyError(f"Provided queue is empty, nothing to merge.")

        return self.items

    def frequency(self, item: object) -> int:

        if bool(self):
            count = 0
            for i in range(len(self)):
                if i == item:
                    count += 1

            return count

        else:
            raise QueueEmptyError("Queue is empty, no item frequency to calculate.")

    def copy(self) -> object:
        if bool(self):
            new_queue = Queue(items=self.items, size=self.size)
        else:
            new_queue = Queue()

        return new_queue

    def is_full(self) -> bool:
        return True if len(self) - self.size == 0 else False

    def is_empty(self) -> bool:
        return bool(self)

    def available_size(self) -> int:
        return len(self) - self.size

    def sort(self) -> object:
        sorted_queue = self.copy()
        sorted_queue.clear()  
        while bool(self):
            min_item = min(self.items)  
            sorted_queue.enqueue(min_item)  
            self.items.remove(min_item)  
        return sorted_queue
