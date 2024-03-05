n = [int(input()) for _ in range(3)]


def findMiddle(n):
    middle = float(len(n))/2
    if middle % 2 != 0:
        return n[int(middle - .5)]
    else:
        return (n[int(middle)], n[int(middle-1)])
        

print(findMiddle(n))