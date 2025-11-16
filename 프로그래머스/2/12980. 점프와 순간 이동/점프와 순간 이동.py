def solution(n):
    bin_n = ''
    while n != 0:
        bin_n += str(n % 2)
        n //= 2
        
    return bin_n.count('1')
  