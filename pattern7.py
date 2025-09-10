# Set the number of rows
n = 5

# You can also take input from the user
# n = int(input("Enter the number of rows: "))

# Outer loop for each row
for i in range(1, n + 1):
    
    # Inner loop to print the dashes
    # This loop runs 'n - i' times
    for j in range(n - i):
        print('-', end='')
        
    # Inner loop to print the stars
    # This loop runs 'i' times
    for k in range(i):
        print('*', end='')
        
    # After printing all characters for a row, print a newline
    print()