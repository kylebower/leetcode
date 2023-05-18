class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title_split = title.split(' ')
        for i, word in enumerate(title_split):
            if len(word) <= 2:
                title_split[i] = word.lower()
            else:
                title_split[i] = word[0].upper() + word[1:].lower()
        return ' '.join(title_split)
        