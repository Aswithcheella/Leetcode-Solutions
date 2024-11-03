class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] #bottom, top, left and right
        min_heap = [(0, 0, 0)] #(current_time, x, y)
        visited = set()
        while min_heap:
            #pop from min heap
            time, x, y = heapq.heappop(min_heap)
            #check if grid reached last room
            if (x, y) == (n-1, m-1):
                return time
            if (x, y) in visited:
                continue
            #add current grid position to visited set
            visited.add((x, y))
            #explore in all four directions
            for dx, dy in directions:
                nx, my = x + dx, y + dy
                #check out of bounce and visited set
                if 0 <= nx < n and 0 <= my < m and (nx,my) not in visited:
                    wait_time = moveTime[nx][my]
                    #move only when time is greater than wait_time(neighor value)
                    if time >= wait_time:
                        new_time = time + 1
                    else:
                        new_time = wait_time + 1
                    #push new neighbour to min heap along with updated time
                    heapq.heappush(min_heap, (new_time, nx, my))
        return -1