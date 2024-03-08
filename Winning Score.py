total_points_apples = 0
total_points_bananas = 0

points_for_3_shot = 3
points_for_2_goal = 2
points_for_1_free_throw = 1

for _ in range(3):
    score = int(input())
    if _ == 0:  
        total_points_apples += score * points_for_3_shot
    elif _ == 1: 
        total_points_apples += score * points_for_2_goal
    else: 
        total_points_apples += score * points_for_1_free_throw

for _ in range(3):
    score = int(input())
    if _ == 0:  
        total_points_bananas += score * points_for_3_shot
    elif _ == 1:  
        total_points_bananas += score * points_for_2_goal
    else:  
        total_points_bananas += score * points_for_1_free_throw

if total_points_apples > total_points_bananas:
    print("A")
elif total_points_bananas > total_points_apples:
    print("B")
else:
    print("T")
