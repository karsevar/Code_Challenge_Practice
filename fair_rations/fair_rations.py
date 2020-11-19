def fairRations(B):
    breads = 0 
    n = len(B) 
    
    for i in range(n - 1):
        if B[i] % 2 != 0:
            breads += 2 
            B[i+1] += 1
            
    if B[-1]%2 != 0:
        return 'NO'
    else:
        return breads