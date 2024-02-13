def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = word1
        word2 = word2

        len_word1 = len(word1)
        len_word2 = len(word2)

        final_word = ""
        append = ""

        if len_word2 > len_word1:
            size = len_word1
            append = word2[size:]
        else:
            size = len_word2
            append = word1[size:]

        for i in range(size):
            final_word += word1[i] + word2[i]

        return final_word + append
