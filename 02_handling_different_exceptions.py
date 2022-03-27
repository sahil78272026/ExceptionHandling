# Program execution will stop even if any error or exception occurs in mid way5

try:
    inp = int(input("enter a number..."))
    a = 2/inp  # if we enter any string like "sajcnsdjcnds" then this will raise exception 
                #and flow of program will move to Exception block
    print(a)

# Handing different kind of Exceptions

except ValueError as e:
    print("Please enter a Valid Number")
   #  print(e) # printing the exception occured 

except ZeroDivisionError as e:
    print("make sure you are not divinding the number by Zero")



print("thanks for using the program") # this will print anyhow