import functools

def min_edit_distance(word1: str, word2: str) -> int:
    @functools.cache
    def min_distance(index1, index2):
        if index1 >= len(word1):
            return len(word2) - index2
        if index2 >= len(word2):
            return len(word1) - index1
        diff = int(word1[index1] != word2[index2])
        return min(1+min_distance(index1+1, index2), 1+min_distance(index1, index2+1), diff+min_distance(index1+1, index2+1))

    return min_distance(0, 0)

print(min_edit_distance("zooicoarchaeologist", "zoologist"))