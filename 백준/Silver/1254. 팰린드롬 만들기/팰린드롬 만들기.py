s = input()
# 9 -> 3,5
# 10 -> 4,5
# 11 -> 4,6
pivot1 = len(s) // 2 - 1
pivot2 = (len(s) + 1) // 2
while True:
    # end cond
    if pivot2 == len(s):
        answer = len(s) * 2 - 1
        break
    
    # check palindrome
    check_len = len(s) - pivot2
    if s[pivot1 - check_len + 1 : pivot1 + 1] == s[pivot2+check_len:pivot2-1:-1]:
        answer = len(s) + (len(s) - 2 * check_len)
        if pivot2 - pivot1 == 2:
            answer -= 1
        break

    # add
    if pivot2 - pivot1 == 1:
        pivot2 += 1
    else:
        pivot1 += 1

print(answer)