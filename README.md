Queue algorithm
=================

A queue is a list where you can only insert new items at the back ```enqueue``` and remove items from the front ```dequeue```. This ensures that the first item you enqueue is also the first item you dequeue.

Since, in this implementation, we want to add an item to the end of the list, this operation will be O(1) - constant-time operation. Adding to the end of a list always takes the same amount of time regardless of the size of the array. Because we would just add one element to memory without touching other elements, other elements of the list will stay on there positions.

Removing item operation will be O(n), we want to add items at the beginning of the list and it will require to shift all elements of the list on one position in memory.

It means, that in our queue one operation - ```enqueue``` will take fewer memory resources and will be more efficient than another - ```dequeue```.


#### Technology used:

* Python 2.7.14

#### Run project:

In the file directory type: ```python ```
To run tests: ```python ```
