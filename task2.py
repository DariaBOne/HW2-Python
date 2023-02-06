S =  int (input("введите сумму чисел X и Y:"))
P =  int (input("введите произведение чисел X и Y:"))
for X in range (1,1001):
    Y = S-X
    if X<=Y and X*Y == P:
        print(X,Y)