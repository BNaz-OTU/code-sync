class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        count = 0
        dictTask = {}
        queue = deque()

        for task in tasks:
            if (task in dictTask):
                dictTask[task] -= 1
            
            else:
                dictTask[task] = -1
        
        for val in dictTask.values():
            heap.append(val)
        
        heapify(heap)
        while len(queue) > 0 or len(heap) > 0:
            count += 1

            if (heap):
                v1 = 1 + heappop(heap)
                if (v1 < 0):
                    queue.append([v1, count + n])
            
            if (queue and queue[0][1] == count):
                heappush(heap, queue.popleft()[0])

        return count