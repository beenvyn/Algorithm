
scores = {'A+': 4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
total = 0
total_hours = 0

for i in range(20):
    sub, hours, grade = input().split()
    
    if grade != 'P':
        total_hours += float(hours)
        total += float(hours) * scores[grade]

print(total / total_hours)
                