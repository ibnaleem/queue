# Queue
<div align="center">
  <img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230726165642/Queue-Data-structure1.png" width="50%" height="50%">
  <h6><i><a href="https://www.geeksforgeeks.org/queue-data-structure/">Queue Data Structure, GeeksForGeeks.org</a></i></h6>
</div>

A Queue is a linear data structure characterised by its first-in-first-out (FIFO) behaviour. Queues `pop` (remove, `'dequeue'`) the `head` (front, first element) of the Queue (i.e `1` is `'dequeued'` from `[1,2,3,4,5]`) and `append` (add, put, `'enqueue'`) an element at the `tail` (back, rear, last element) of the Queue. Queues are fixed sized, meaning an object cannot be enqueued if the Queue is full.
### Example
```python
q = Queue([1,2,3,4,5])
print(q)
```
```
[1,2,3,4,5]
Size: 6 (one more than the length of the Queue)
```
```python
q.enqueue(6)
print(q)
```
```
[1,2,3,4,5,6]
```
```python
q.dequeue() # no args since it will always remove the head of the Queue
print(q)
```
```
[2,3,4,5,6]
Removed: 1 (previous head)
New head: 2
```
```python
q.enqueue(7)
```
```
[2,3,4,5,6,7]
```
```python
q.enqueue(8)
```
```
raise QueueFullError("Cannot enqueue at full size: 6")
```
## Classes, Attributes, Methods and Exceptions
### Classes
- `Queue(items: object = None, size: int = None)` - Optional parameters: `items` (the items in the queue) and `size` (the size allocated for the queue)
### Attributes
- `items` - the queue itself, more specifically its items, constructed as a list
- `size` - the size of the queue
- `head` - the first element of the queue, i.e `self.items[0]`
- `tail` - the last element of the queue, i.e `self.items[-1]`
### Methods
- `enqueue(item: object)` - appends an `object` to the end of the queue; extends the queue if `object` is of type `list`
-  `dequeue()` - removes the `head` of the queue (`self.items.pop(0)`)
-  `peek()` - equivalent to `head` attribute
-  `clear()` - empties the queue
-  `merge(queue: 'Queue')` - merges two queues together via `enqueue()` method
-  `frequency(item: object)` - returns the amount of times (frequency) an item is present in a queue
-  `copy()` - creates a copy of current queue and returns it
-  `is_full()` - returns a `True` if queue is full
-  `is_empty()` - returns `True` if queue is empty
-  `available_size()` - subtracts the length of the queue by the `size` attribute to calculate the available size remaining in the queue
-  `sort()` - sorts the queue in ascending order 
### Exceptions:
- `QueueFullError()` - Raised when attempting to enqueue a full Queue, exceeding its fixed size
- `QueueEmptyError()` - Raised when attempting to dequeue an empty Queue
- `QueueError()` - Raised when ran into esoteric errors, such as trying to enqueue 2D arrays
