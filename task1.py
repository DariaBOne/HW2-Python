n = int(input("введите количество монеток"))
count_1 = count_2 = 0
list = []
import random
for i in range(n):
    list.append(random.randint(0,1))
print(list)
for j in range(len(list)): 
    if list[j]==1: count_1+=1
    else: count_2+=1
print("надо перевернуть", count_2) if count_2<count_1 else print("надо перевернуть", count_1)


