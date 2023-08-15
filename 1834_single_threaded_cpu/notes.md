https://leetcode.com/problems/single-threaded-cpu/

We need to keep track of indexes of each task. Add idx to each element.
Sort task according to enque time and it will act as a queue.
We will add each task to a task heap(minHeap) if the task enque time is <= current time.
We do not need to increae current time by one.
If cpu is idle, go to the time of next task enque time in queue.
If cpu just started processing, go to the end off processing of cur task.