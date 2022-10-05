_ = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

front = 0
back = len(nums) - 1
count = 0
while front < back:
    add = nums[front] + nums[back]
    if add == x:
        count += 1
        front += 1
        back -= 1
    elif add > x:
        back -= 1
    else:
        front += 1

print(count)