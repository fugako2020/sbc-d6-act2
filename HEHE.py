
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))


cols = 4


for i in range(rows):
    for j in range(cols):
        if j == 0 or j == cols - 1:  
            print("* ", end=" ")
        elif i == 0 or i == rows - 1:  
            print("* ", end="  ")
        else:  
            print("  ", end="  ")
    print()  





