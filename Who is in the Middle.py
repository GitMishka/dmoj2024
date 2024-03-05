first = int(input())
second = int(input())
third = int(input())

n = []

n.append(first)
n.append(second)
n.append(third)

n.sort()

def findMiddle(n):
    middle = float(len(n))/2
    if middle % 2 != 0:
        return n[int(middle - .5)]
    else:
        return (n[int(middle)], n[int(middle-1)])

print(findMiddle(n))