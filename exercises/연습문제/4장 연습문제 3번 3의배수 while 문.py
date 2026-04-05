total_sum = 0
i = 1  

while i <= 50:
 
    if i % 2 == 0 and i % 3 != 0:
        total_sum += i
    

    i += 1

print("합계:", total_sum)