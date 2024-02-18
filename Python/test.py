def match_word_pattern(pattern: str, input_string: str) -> bool:
    pattern_map = {}
    string_map = {}
    
    def backtrack(pattern_index: int, string_index: int) -> bool:
        if pattern_index == len(pattern) and string_index == len(input_string):
            return True
        if pattern_index == len(pattern) or string_index == len(input_string):
            return False
        
        char = pattern[pattern_index]
        if char in pattern_map:
            mapped_str = pattern_map[char]
            if input_string.startswith(mapped_str, string_index):
                return backtrack(pattern_index + 1, string_index + len(mapped_str))
            else:
                return False
            
        for end in range(string_index + 1, len(input_string) + 1):
            sub_string = input_string[string_index:end]
            if sub_string in string_map:
                continue
            pattern_map[char] = sub_string
            string_map[sub_string] = char
            if backtrack(pattern_index + 1, end):
                return True
            del pattern_map[char]
            del string_map[sub_string]
        return False

    return backtrack(0, 0)

print(match_word_pattern("aba", "GraphTreesGraph"))
print(match_word_pattern("xyx", "PythonRubyPython"))
print(match_word_pattern("GG", "PythonJavaPython"))