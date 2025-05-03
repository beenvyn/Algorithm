def solution(n):
    x = n

    while True:
        x += 1
        
        bin_n = bin(n)[2:]
        bin_x = bin(x)[2:]
        
        if bin_n.count('1') == bin_x.count('1'):
            return x
        
    