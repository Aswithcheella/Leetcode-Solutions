class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] #bottom, top, left and right
        #move_type can be 1 or 2 alternating between each move, move_type start with 1
        min_heap = [(0, 0, 0, 1)] #(current_time, x, y, move_type)
        visited = set()

        while min_heap:
            time, x, y, move_type = heapq.heappop(min_heap)
            if (x, y) == (n-1, m-1):
                return time
            if (x, y, move_type) in visited:
                continue
            visited.add((x, y, move_type))

            #explore in all four directions
            for dx, dy in directions:
                nx, my = x + dx, y + dy
                if 0 <= nx < n and 0 <= my < m and (nx,my, move_type) not in visited:
                    wait_time = moveTime[nx][my]
                    if time >= wait_time:
                        new_time = time + move_type
                    else:
                        new_time = wait_time + move_type
                    next_move = 1 if move_type == 2 else 2
                    heapq.heappush(min_heap, (new_time, nx, my, next_move))
        return -1