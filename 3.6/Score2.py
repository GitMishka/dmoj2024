scores = list(map(int, input("Enter all 6 scores separated by space: ").split()))

if len(scores) != 6:
    print("Error: Please enter exactly 6 scores.")
else:
    points_values = [3, 2, 1]

    total_points_apples = sum(scores[i] * points_values[i % 3] for i in range(3))
    total_points_bananas = sum(scores[i] * points_values[i % 3] for i in range(3, 6))

    if total_points_apples > total_points_bananas:
        print("A")
    elif total_points_bananas > total_points_apples:
        print("B")
    else:
        print("T")
