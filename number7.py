#number 7
# Write a function called show_stars(rows). If rows is 5, it should print the following:


rows = 5
for i in range(0, rows):
    #print(1)
    #loop for each column
    for j in range(0, i + 1):
        # 
        print("*", end=' ')
    #each row
    print("\r")
