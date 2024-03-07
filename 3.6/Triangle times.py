angles = []

for _ in range(3):
    angle = int(input())
    angles.append(angle)

if sum(angles) != 180:
    print("Error")
elif len(set(angles)) == 1:  # All angles are the same
    print("Equilateral")
elif len(set(angles)) == 2:  # Exactly two angles are the same
    print("Isosceles")
else:  # All angles are different and they sum up to 180
    print("Scalene")
