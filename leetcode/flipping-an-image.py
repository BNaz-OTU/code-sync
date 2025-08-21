class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        # USED SOLN: https://www.youtube.com/watch?v=qnd1WiutGio

        for idx in range(len(image)):
            left = 0
            right = len(image) - 1

            while (left <= right):
                if (image[idx][left] == image[idx][right]):
                    image[idx][left] = 1 - image[idx][left]
                    image[idx][right] = image[idx][left]
                
                left += 1
                right -= 1
        
        return image