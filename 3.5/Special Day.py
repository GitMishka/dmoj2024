n = [int(input()) for _ in range(2)]
if n[0] == 2 :
    if n[1] < 18:
        print('Before')
    elif n[1] > 18:
        print('After')
    else:
        print('Special')
elif n[0] > 2 :
    print("After")
else:
    print("Before")