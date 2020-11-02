nums = [3,3,3,2,2,4]

def solution(nums):
    can_get = len(nums)//2
    nums = list(set(nums))
    if can_get >= len(nums):
        return len(nums)
    else:
        return can_get

print(solution(nums))

