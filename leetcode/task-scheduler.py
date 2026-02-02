class Solution:
    # USED SOLN: https://www.youtube.com/watch?v=s8p8ukTyA2I
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if (maxHeap):
                cnt = 1 + heappop(maxHeap)
                if (cnt):
                    q.append([cnt, time + n])
            if (q and q[0][1] == time):
                heappush(maxHeap, q.popleft()[0])
        return time