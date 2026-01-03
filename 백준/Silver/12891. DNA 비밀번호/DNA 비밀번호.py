import sys
input = sys.stdin.readline

m, p = map(int, input().split())
string = input().strip()
A, C, G, T = map(int, input().split())
answer = 0

temp = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
start = string[:p]
for s in start:
    temp[s] += 1

if temp['A'] >= A and temp['C'] >= C and temp['G'] >= G and temp['T'] >= T:
    answer += 1

start_idx = 0
end_idx = start_idx + p

for i in range(m - p):
    temp[string[start_idx + i]] -= 1
    temp[string[end_idx + i]] += 1
    if temp['A'] >= A and temp['C'] >= C and temp['G'] >= G and temp['T'] >= T:
        answer += 1

print(answer)