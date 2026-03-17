import heapq

def solution(book_time):
    answer = 0
    book_mins = []
    
    def get_mins(s):
        h, m = map(int, s.split(':'))
        return h * 60 + m
    
    for start, end in book_time:
        book_mins.append([get_mins(start), get_mins(end) + 10])
    
    book_mins.sort()
    
    heap = []
    for start, end in book_mins:
        # 가장 빨리 비는 방(heap[0])이 현재 예약 시작 시간보다
        # 빠르거나 같으면 그 방은 재사용 가능
        while heap and start >= heap[0]:
            heapq.heappop(heap) # 방 제거
            
        heapq.heappush(heap, end)
        
        # 현재 사용 중인 방의 개수 = len(heap)
        answer = max(answer, len(heap))
    
    return answer