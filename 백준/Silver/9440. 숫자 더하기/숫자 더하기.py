while True:
    problem = list(map(int, input().split()))
    if problem == [0]:
        break

    problem = sorted(problem[1:])
    n1, n2 = [], []
    current = n1
    i = 0
    while problem:
        if len(current) == 0:
            i = next(i for i, _ in enumerate(problem) if problem[i] != 0)
        
        current.append(str(problem[i]))
        
        del problem[i]
        i = 0

        if current is n1:
            current = n2
        else:
            current = n1
            
    print(int("".join(n1)) + int("".join(n2)))

