class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dictTask = {}
        heap = []
        queue = deque()

        for task in tasks:
            if task in dictTask:
                dictTask[task] -= 1
            else:
                dictTask[task] = -1
        
        for val in dictTask.values():
            heap.append(val)
        
        heapify(heap)
        time = 0
        while queue or heap:
            time += 1

            if (heap):
                val = heappop(heap)
                if val < -1:
                    queue.append((time + n, val + 1))
            
            if (queue and queue[0][0] == time):
                heappush(heap, queue.popleft()[1])

        return time