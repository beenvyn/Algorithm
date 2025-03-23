n = input()
n = int(n)
options = [300, 60, 10]

def cal(n):
    answer = [0, 0, 0]

    for idx, option in enumerate(options):
        answer[idx] = n // option
        n -= answer[idx] * option
    
    return ' '.join([str(n) for n in answer]) if n == 0 else -1
         

print(cal(n))