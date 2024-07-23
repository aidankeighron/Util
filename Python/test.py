def all_construct(target: str, bank: list) -> list:
    table = [[] for _ in range(len(target)+1)]

    table[0] = [[]]

    for i in range(len(target)+1):
        if table[i] != []:
            for word in bank:
                if target[i:i+len(word)] == word:
                    new_combinations = [[word, *way] for way in table[i]]

                    table[i+len(word)] += new_combinations

    for combination in table[len(target)]:
        combination.reverse()

    return table[len(target)]

print(all_construct("purple",["purp","p","ur","le","purpl"]))