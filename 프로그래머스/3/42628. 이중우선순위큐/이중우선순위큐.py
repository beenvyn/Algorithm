import heapq

def solution(operations):
    heap = []
    
    for op in operations:
        a, b = op.split()
        
        if a == 'I':
            heapq.heappush(heap, int(b))
        elif a == 'D' and b == '1' and heap:
            heap.sort()
            heap.pop()
        elif a == 'D' and b == '-1' and heap:
            heapq.heappop(heap)
    
    heap.sort()
    if not heap:
        return [0,0]
    else:
        return [heap[-1], heap[0]]
