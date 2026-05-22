class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        minStops = 0
        curlocation = 0
        heap = []
        heapify(heap)

        stations.append([target, 0])

        for location, fuel in stations:
            startFuel -= (location - curlocation)
            curlocation += (location - curlocation)

            while startFuel < 0 and len(heap) > 0:
                startFuel += -heappop(heap)
                minStops += 1
            
            if startFuel < 0:
                return -1
            
            heappush(heap, -fuel)
        
        if (curlocation < target):
            return - 1

        return minStops