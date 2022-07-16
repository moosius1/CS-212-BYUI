# Queues

[Back to Welcome page](/welcome.md)

Lines. We all have been in them before. When they run properly, it makes everyone happy there is order and regulation in the world, but when they don't, people get frustrated, tired and impatient. 

Queues are the savior of waiting lines. They can ensure that one set of data is specifically next in line no matter how many other people hop in line. Everything has a place in the queue. 

Most queue operations have a performance of O(1) meaning that no matter the size of your queue you can get almost instant results. The operators that have this performance are appending to the queue (enqueue), getting the size of the queue (size()), checking if the queue is empty (empty()). The only exception is the dequeue which if your queue is larger will take longer to complete making it O(n).  

## Purposes and usage

Queues are a type of data structure that stores items First in First out. This means that the first item added into the queue will be processed first, and the last item added to the queue will be processed last. I like to relate this to being on hold with a company over the phone. There will most likely be a number of different callers calling into the company, but the person who is next in line will have their call answered first.


![Queue Visual Aide](/pictures/queue.png)


## Examples

```
#initialize the queue
exampleQueue = [];

# this is basically now an empty line at the grocery store,
# no one is in it, though it still exists 

# lets say someone gets in line

exampleQueue.append(1);

# while the first person is getting checked out, 2 more people come into the queue

exampleQueue.append(2);
exampleQueue.append(3);

# with that the line looks like this
# [1,2,3];

# lets say that the first person is finally done;

# the function would then need to remove the first person from the queue;

exampleQueue.pop(0);

# with that the line now appears as 
# [2,3];



```

## Problem: 

This is a simple test to see if you understand the basic structure of how a FIFO type queue works. 

Solution is included in the file

[Problem File](/py%20files/queueproblem.py)


## Operations used with Queues

enqueue(value): Adds to the queue starting with the first available space and increasing as needed. O(1) performance
```
exampleQueue.append(value);
```

dequeue(): Used to remove from the front of the queue, or to remove at a specific index from the queue. O(n) performance
```
exampleQueue.pop(value);
del exampleQueue[index];

``` 

size(): Used to determine the size or length of the queue. O(1) performance
```
len(exampleQueue);
```


empty(): pretty self explanitory, but it is a boolean operation returning either true or false depending if the queue contains values or not. O(1) performance

```
if len(exampleQueue) == 0:
    doSomething();
```

full(): oposite of empty() operation, can check to see if the queue contains a certain number of values, or if it contains anything at all. O(1) performance

```
if len(exampleQueue) < 0: 
    doSomething();

if len(exampleQueue) == x:
    doSomethingElse();
    
```

## Video walkthrough on Youtube by Joe James:

[Python Queues](https://youtu.be/XLXWidXVRJk)

## Codebasic's tutorial on Youtube it is Excellent
[Codebasic's queues video](https://youtu.be/qp8u-frRAnU)


## Images referenced can be found here:

[Queue Image](https://www.section.io/engineering-education/queue-data-structure-python/)


## [Back to Welcome page](/welcome.md)
