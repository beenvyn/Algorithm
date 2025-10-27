import heapq

def solution(book_time):
    answer = 0
    book_mins = []
    for start, end in book_time:
        start_h, start_m = map(int,start.split(':'))
        end_h, end_m = map(int,end.split(':'))
        book_mins.append((start_h*60+start_m, end_h*60+end_m))
    book_mins.sort()
    
    using_heap = []
    for start, end in book_mins:
        while using_heap and using_heap[0] + 10 <= start:
            heapq.heappop(using_heap)
        
        heapq.heappush(using_heap,end)
        answer = max(answer,len(using_heap))
    
    return answer