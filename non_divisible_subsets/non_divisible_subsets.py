def nonDivisibleSubset(k, s):
    print(k) 
    print(s)
    
    counts = [0] * k 

    for num in s:
        counts[num%k] += 1 

    count = min(counts[0], 1)

    print(counts)
    
    for i in range(1, k//2+1):
        if i != k-i:
            count += max(counts[i], counts[k-i])
    
    if k%2 == 0:
        count += 1
    
    return count