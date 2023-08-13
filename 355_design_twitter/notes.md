https://leetcode.com/problems/design-twitter

The biggest problem we face is of choosing the proper data structure.
For storing the followeeIDs, we will use a hashmap of userID->set(followeeID).
For storing tweets, userID -> List(tweetID).
For getting the latest tweets, we just need to use a maxHeap. Keep a count which will hact as the timestamp.