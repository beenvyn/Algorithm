import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
package = []
individual = []

for _ in range(m):
    p, i = map(int, input().rstrip().split())
    package.append(p)
    individual.append(i)

package = sorted(package)
individual = sorted(individual)    

opt1 = (n // 6 + 1) * package[0]
opt2 = (n // 6) * package[0] + (n % 6) * individual[0]
opt3 = n * individual[0]
print(min(opt1, opt2, opt3))