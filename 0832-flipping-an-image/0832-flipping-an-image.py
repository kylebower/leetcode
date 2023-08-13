class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(image):
            image[i] = [-x+1 for x in reversed(row)]
        return image
    