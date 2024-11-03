Leetcode Weekly Contest 422

Q1 Check Balanced String

Solution Explanation

The function isBalanced checks if the sum of digits at even indices is equal to the sum of digits at odd indices in a given string num.

Steps:
Initialize Sums: The variables oddSum and evenSum are initialized to 0. These will hold the sums of digits at odd and even indices, respectively.

Loop through the String: We iterate through each character in num using a for loop, where i is the index of each character.

Check Index Parity:
If i is even (i % 2 == 0), we add the digit at index i to evenSum.
If i is odd, we add the digit at index i to oddSum.

Return Result: After completing the loop, we check if evenSum is equal to oddSum. If they are equal, the function returns True, indicating the number is “balanced.” Otherwise, it returns False.

Time complexity: O(N)
Space complexity: O(1)





Leetcode Weekly Contest 422

Q2 Find Minimum Time to Reach Last Room I

This problem is text-book example of shortest weighted path solution using Dijkstra’s algorithm

Step-by-Step Explanation

1. Setup:
• The moveTime matrix represents the grid, where each cell tells us the “wait time” required before we can enter it.
• We need to move from the top-left (0, 0) to the bottom-right (n-1, m-1), where n and m are the dimensions of the grid.
• We create a min_heap, a type of priority queue that helps us always process the cell with the smallest “current time” first. We start by adding the starting cell (0, 0) with a time of 0.
2. Main Loop:
• The algorithm works by repeatedly taking the cell with the smallest time from the min_heap (like a list of tasks sorted by priority).
• For each cell, we check:
• If we’ve reached the destination: If (x, y) is the bottom-right corner, we return the time it took to get there since that’s the minimum time required.
• If we’ve already visited this cell: We skip it if it’s already in our visited set to avoid unnecessary re-processing.
3. Explore Neighboring Cells:
• For each cell, we check its four neighboring cells (down, up, right, and left).
• For each neighbor:
• Bounds Check: We ensure it’s within grid boundaries and hasn’t been visited.
• Wait Time Check:
• If we arrive at the neighbor after the “wait time” of that cell, we move there immediately, adding 1 second to the current time.
• If not, we “wait” until we can enter (set by the neighbor’s wait time) and then add 1 second.
• Add to Queue: We then add this neighbor to the min_heap with the updated time to reach it.
4. End Condition:
• If there’s no way to reach the bottom-right cell, we return -1 (though we assume there’s always a path in most grid problems).

Time complexity: O(N*MLog(N*M)), N*M to process the NxM grid and min_heap takes log(N*M) to arrange NxM grid

Space complexity: O(N*M), visited set stores at most NxM positions






Leetcode Weekly Contest 422

Q3 Find Minimum Time to Reach Last Room II

Solution is same as Q2(Find Minimum Time to Reach Last Room I) but only difference is in this problem there are two move types, type1 adds one second to the time and type 2 adds two seconds to the time. First move(from position(0,0)) is move type1 next move is move type this will alternate till grid position reaches (n-1, m-1).

next_move = 1 if move_type == 2 else 2

Track current move_type, based on current move_type update next_move type and push to min heap.



Time complexity: O(N*MLog(N*M)), N*M to process the NxM grid and min_heap takes log(N*M) to arrange NxM grid

Space complexity: O(N*M), visited set stores at most NxM positions

#leetcode#DSA#Google#Dijkstra#shortestpath#minHeap 
