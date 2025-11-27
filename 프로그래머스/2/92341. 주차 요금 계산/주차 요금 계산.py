import math

def solution(fees, records):
    result = []
    answer = []
    car_time = {}
    
    def to_minutes(time):
        h, m = map(int, time.split(':'))
        return h * 60 + m
    
    for record in records:
        time, car, opt = record.split()
        
        mins = to_minutes(time)
        if car not in car_time:
            car_time[car] = []
        car_time[car].append(mins)
    
    for car, mins in car_time.items():
        total = 0
        length = len(mins)
        mins.sort()
        
        if length % 2 == 0:
            for i in range(1,length,2):
                total += (mins[i] - mins[i-1])
        else:
            for i in range(1,length-1,2):
                total += (mins[i] - mins[i-1])
            total += to_minutes("23:59") - mins[length-1]
        result.append((car,total))
    
    result.sort()
    for car, mins in result:
        price = fees[1]
        if mins > fees[0]:
            price += math.ceil((mins - fees[0]) / fees[2]) * fees[3]
        answer.append(price)
    
    return answer