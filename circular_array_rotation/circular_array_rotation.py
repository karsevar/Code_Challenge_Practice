def circularArrayRotation(a, k, queries):
    solution = []
    print(k % len(a))
    if k <= len(a):
        print(a[-k:]+a[:-k])
        newArray = a[-k:]+a[:-k]

        for query in queries:
            solution.append(newArray[query])

    elif k > len(a):
        remainder = k % len(a) 
        newArray = a[-remainder:] + a[:-remainder]

        for query in queries:
            solution.append(newArray[query])
    else:
        for query in queries:
            if query < len(a):
                solution.append(a[query])

    return solution