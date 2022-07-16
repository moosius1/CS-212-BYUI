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


exampleQueue.append(4);
exampleQueue.append(5);
exampleQueue.pop(0);
exampleQueue.append(6);
exampleQueue.append(7);
exampleQueue.pop(0);
exampleQueue.append(8);
exampleQueue.append(9);
exampleQueue.pop(0);
exampleQueue.append(10);
exampleQueue.append(11);

print(exampleQueue)

# output is [5, 6, 7, 8, 9, 10, 11]



