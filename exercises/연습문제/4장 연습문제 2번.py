total_sum = 0

for i in range(1, 51):
    if i % 2 == 0 and i % 3 != 0:
        total_sum += i  

print("조건을 만족하는 합:", total_sum)