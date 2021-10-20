"""
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# Method 01

givenNumber = int(input("Enter you Number: "))

NumList = []

for number in range(1,givenNumber+1):
    NumList.append(number)

print(NumList)
print(sum(NumList))

# method 2 

result = 0

givenNumber = int(input("Please enter you number here: "))

for i in range(1,givenNumber+1):
    result += i

print(result)

"""


"""
Exercise 4: Write a program to print multiplication table of a given number
For example, num = 2 so the output should be

# Method 01
TableOf = int(input("Enter your number here: "))

for i in range(1,11):
    print(i*TableOf)

"""



"""
Exercise 5: Display numbers from a list using loop
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
Given:

numbers = [12, 75, 150, 180, 145, 525, 50]
"""
numbers = [12, 75, 150, 180, 145, 525, 50]

while True:
    for number in numbers:
        if number/5 and number < 150:
            print(number)
        elif number < 500 :
            break


    
