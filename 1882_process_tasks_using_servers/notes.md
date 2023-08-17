https://leetcode.com/problems/process-tasks-using-servers

We use two priority queues. For available servers and occupied servers.
Store (weight, idx) in available and (wait_till, weight, index) in occupied.