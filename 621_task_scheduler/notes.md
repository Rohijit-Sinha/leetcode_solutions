https://leetcode.com/problems/task-scheduler

We have to process the task with most count first.
Since count changes every time, we will have to look for the task with most count.
This means an O(n) lookup. Alternatively, we can use a max heap of counts.
Every time we pop from the heap, we can queue the popped task for addition to the heap just before we can process it.
This means, if a task "A" can be processed at 1,3 i.e. n = 1, we pop from queue and add to heap at time == 2.