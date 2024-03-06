n = [int(input()) for _ in range(2)]

if n[0] < 2 and n[1] < 18:
    print('Before')
elif n[0] > 2 and n[1] > 18:
    print("After")
else:
    print("Special")