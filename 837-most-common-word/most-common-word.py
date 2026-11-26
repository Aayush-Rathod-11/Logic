from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned_set = set(banned)
        counts = defaultdict(int)
        n = len(paragraph)

        best_word = ""
        best_count = 0
        start = -1

        for i in range(n + 1):
            # Treat any non-alphabetic character (or end of string) as a word boundary
            if i < n and paragraph[i].isalpha():
                if start == -1:
                    start = i
            elif start != -1:
                word = paragraph[start:i].lower()
                start = -1
                if word not in banned_set:
                    cnt = counts[word] + 1
                    counts[word] = cnt
                    if cnt > best_count:
                        best_count = cnt
                        best_word = word

        return best_word