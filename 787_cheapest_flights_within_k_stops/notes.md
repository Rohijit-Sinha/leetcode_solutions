https://leetcode.com/problems/cheapest-flights-within-k-stops/

We use djikstra's algo. We store [stops,dest,cost] in a simple queue since we dont need to get lowest priority. Priority will increase gradually 1 by 1.