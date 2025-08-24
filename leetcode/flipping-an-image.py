class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        left = 0
        right = len(image) - 1

        for row in image:

            # Case for when the middle row is odd
            if (len(row) % 2 == 1):
                row[len(row) // 2] = 1 - row[len(row) // 2]

            while left < right:
                print('hi')
                if (row[left] == row[right]):
                    row[left] = 1 - row[left]
                    row[right] = 1 - row[right]

                left += 1
                right -= 1

            left = 0
            right = len(image) - 1

        return image