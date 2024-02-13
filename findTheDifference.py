def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if i not in s:
                return i
            elif i in s and t.count(i) > s.count(i):
                return i
