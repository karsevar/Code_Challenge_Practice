def flatlandSpaceStations(n, c):
    answer = 0 
    c.sort()
    print('space stations', c)
    
    for i in range(1, len(c)):
        answer = max(answer, (c[i]-c[i-1])//2)
        
    answer = max(answer, c[0], n-1 - c[-1])
    
    return answer