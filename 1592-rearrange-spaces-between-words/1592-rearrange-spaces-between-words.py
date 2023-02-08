class Solution:
    def reorderSpaces(self, text: str) -> str:
        num_spaces = 0
        for c in text:
            if c == " ":
                num_spaces += 1
        
        num_words = 0
        result = []
        split_text = text.split(' ')
        for w in split_text:
            if w != '':
                result.append(w)
                num_words += 1
        
        if num_words < 2:
            num_spaces_between_words = 0
        else:
            num_spaces_between_words = int(num_spaces // (num_words-1))
        num_spaces_at_end = num_spaces - num_spaces_between_words * (num_words - 1)
        
        seperator = ""
        print(num_spaces_between_words)
        for _ in range(num_spaces_between_words):
            seperator += " "
        
        
        end_space = ""
        print(num_spaces_at_end)
        for _ in range(num_spaces_at_end):
            end_space += " "
        
        
        return seperator.join(result) + end_space