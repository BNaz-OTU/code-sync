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
        # * Keep looping through if there are values still in the heap or the queue
        # * Queue keeps track of tasks waiting to go again
        # * Heap sorts the tasks, sorts tasks by the tasks that need to do the most work. 
        #   This will help find the min time
        while len(queue) > 0 or len(heap) > 0:
            count += 1 # Regardless if a task can be processed or not, increment the count

            if (heap): # If there is a value in the heap, remove it and decrement its remaining todo tasks
                v1 = 1 + heappop(heap)

                # If you haven't completed the task add it to the queue, 
                # and keep track of time for when your able to call it again
                if (v1 < 0): 
                    queue.append([v1, count + n])
            
            # If there is something in the queue and enough time has passed, remove the value 
            # from the queue and re-add it to the heap so it can be called again later
            if (queue and queue[0][1] == count):
                taskLeft = queue.popleft()[0]
                heappush(heap, taskLeft)

        return count