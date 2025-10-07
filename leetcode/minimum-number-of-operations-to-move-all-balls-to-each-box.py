class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # [0, 0, 0, 0, 1, 2, 4]
        # [11, 8, 5, 3, 1, 0, 0]
        pass1 = [0] * (len(boxes) + 1)
        pass2 = [0] * (len(boxes) + 1)
        final = []
        ballCount = 0

        # First Pass
        for idx in range(len(boxes)):
            # Check Prev
            if (idx != 0):
                pass1[idx] = pass1[idx - 1] + ballCount
            
            if (boxes[idx] == "1"):
                ballCount += 1
        
        ballCount = 0
        r_boxes = boxes[::-1]
        # Second Pass
        for idx in range(len(boxes)):
            # Check Prev
            if (idx != 0):
                pass2[idx] = pass2[idx - 1] + ballCount
            
            if (r_boxes[idx] == "1"):
                print(idx, "Fo")
                ballCount += 1
            # print(idx)
        
        pass2 = pass2[::-1]

        for idx in range(1, len(pass1)):
            final.append(pass1[idx - 1] + pass2[idx])
        
        return final