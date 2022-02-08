# Conditional Statements

## IF
# if test expression:
#     Body of if

# Example: 
A = 20
B = 30
C = A+B
if C>50:
    print("Answer is greater than 50")
if C<50:
    print("Answer is less than 50")

## One line if statement:
if A > B: print("A is greater than B")

## Else IF
# if test expression:
#     Body of if
# elif:
#     Body of elif
# else:
#     Body of else

#Example
A = 20
B = 30
C = A+B
if C>50:
    print("Answer is greater than 50")
elif C<50:
    print("Answer is less than 50")
else:
    print("Answer equal to 50")



## Nested IF
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")



## and
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a number: "))
if num_1 > 10 and num_2 > 10 :
    print("Both numbers are greater than 10")
elif num_1 < 10 and num_2 < 10 :
    print("Both numbers are less than 10")
else:
    print("Something else")

## or
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a number: "))
if num_1 > 10 or num_2 > 10 :
    print("One of the number is greater than 10")
elif num_1 < 10 or num_2 < 10 :
    print("One of the number is less than 10")
else:
    print("Something else")








