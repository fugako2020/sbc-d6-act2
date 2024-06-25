
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
cols = 4  

i = 0

while i < rows:
    
    j = 0
    
    while j < cols:
        if j == 0 or j == cols - 1:  
            print("* ", end=" ")
        elif i == 0 or i == rows - 1:  
            print("* ", end="  ")
        else:  
            print("  ", end="  ")
        j += 1  
    print()  
    i += 1  
 




