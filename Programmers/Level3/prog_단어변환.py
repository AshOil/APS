from difflib import SequenceMatcher

begin = "hit"
target = "cog"
length = len(begin)
words = ["hot", "dot", "dog", "lot", "log", "cog"]
diff_ratio = (length-1)/length

def DFS(come_word, depth):
    global result
    if come_word == target:
        if result > depth:
            result = depth

    for word in words:
        if SequenceMatcher(None, come_word, word).ratio() == diff_ratio and word not in visit:
            visit.append(word)
            DFS(word, depth+1)
            visit.pop()

visit = []
result = 10000
DFS(begin, 0)
print(result)