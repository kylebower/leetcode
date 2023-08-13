class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(image):
            flip_row = [row[k] for k in range(len(row)-1,-1,-1)]
            image[i] = [-x+1 for x in flip_row]
        return image
    