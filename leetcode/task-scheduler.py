class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashTask = {}
        heap = []
        queue = deque()

        for task in tasks:
            if (task not in hashTask):
                hashTask[task] = 0
            
            hashTask[task] -= 1

        for val in hashTask.values():
            heap.append(val)
        
        heapify(heap)
        
        time = 0
        while heap or queue:
            time += 1
            if (heap):
                val = heappop(heap)

                if ((val + 1) < 0):
                    queue.append([time + n, val + 1])
            
            if (queue and queue[0][0] == time):
                heappush(heap, queue.popleft()[1])
                
        return time