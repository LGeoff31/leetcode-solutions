class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # reverse
        for i in range(len(image)):
            image[i] = image[i][::-1]
        print(image)
        for r in range(len(image)):
            for c in range(len(image)):
                image[r][c] = (1 if image[r][c] == 0 else 0)
        return image