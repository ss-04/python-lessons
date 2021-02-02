row = int(input("Enter row : "))
col = int(input("Enter col : "))
for row in range(1, row + 1):
    for col in range(1,col + 1):
        print("*", end=" ")
    print(" ")
