class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_num_words = 0
        for sentence_i in sentences:
            words_i = 1
            for c in sentence_i:
                if c == ' ':
                    words_i += 1
            max_num_words = max(max_num_words, words_i)
        return max_num_words
        