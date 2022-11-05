from collections import Counter


def run():
    name = input()
    char_counter = Counter(name)
    middle_char = ""
    char_list = []
    for key, value in char_counter.items():
        if value % 2 == 1:
            if middle_char != "":
                print("I'm Sorry Hansoo")
                return
            else:
                middle_char = key
        char_list.extend([key] * (value // 2))

    front = "".join(sorted(char_list))
    print(front + middle_char + front[::-1])
        
run()