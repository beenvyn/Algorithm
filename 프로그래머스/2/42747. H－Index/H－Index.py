def solution(citations):
    n = len(citations)
    citations.sort()

    for i in range(n):
        if n - i <= citations[i]:
            return n - i
    return 0