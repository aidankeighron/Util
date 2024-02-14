def power_sum(needed_sum: int, power: int) -> int:
    result = 0

    def backtrack(current_sum, current_num):
        nonlocal result
        if current_sum == needed_sum:
            result += 1
            return

        next_num = current_num ** power
        if current_sum + next_num <= needed_sum:
            current_sum += next_num
            backtrack(current_sum, current_num+1)
            current_sum -= next_num
        if next_num < needed_sum:
            backtrack(current_sum, current_num+1)

    backtrack(0, 1)
    return result

print(power_sum(13, 2))