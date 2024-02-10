'''
simple_programming_

This code prints the numbers from 1 to 4, 
except 2 and 4, 
using a while loop and a continue statement
'''
i = 1 
while i < 5:
    # Check if i is equal to 2 or 4
    if i == 2 or i == 4: 
        i += 1
        # Skip the rest of the loop body 
        # and go back to the condition
        continue 
    print(i) 
    i += 1 