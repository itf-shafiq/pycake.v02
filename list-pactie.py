"""
                            Try It Yourself

4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,inclusive.

4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)

4-5. Summing a Million: Make a list of the numbers from one to one million,and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.

4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

4-8. Cubes: A number raised to the third power is called a cube. For example,the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.

4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.

"""
# Practice 01
"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,inclusive.

for number in range(1,21):
    print(number)

"""
#practice 02
"""
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)

miliList = []

for milion in range(1,100001):
    miliList.append(milion)
    print(miliList)

"""


# Practice 03

"""
4-5. Summing a Million: Make a list of the numbers from one to one million,and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.

MilionList = []

for milion in range(1,100001):
    MilionList.append(milion)

print(min(MilionList))
print(max(MilionList))
print(sum(MilionList))

"""
#practice 05

"""
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

OddNumberList = []

for OddNumber in range(1,20,2):
    OddNumberList.append(OddNumber)
print(OddNumberList)

"""
# Practice 06
"""
4-6-1. Odd Numbers: Use the third argument of the range() function to make a list of the Even numbers from 1 to 20. Use a for loop to print each number.

EvenNumberList = []

for EvenNumber in range(2,20,2):
    EvenNumberList.append(EvenNumber)

print(EvenNumberList)

"""
# Practice 07
"""

4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

# Method 01
ThreesList = []

for threes in range(3,30):
    th = threes*3
    ThreesList.append(th)

print(ThreesList)

# Method 02

ThreesList02 = []

for threes in range(3,30):
    ThreesList02.append(threes*3)

print(ThreesList02)

# Method 03 (List Comprehensive)

ThreesList = [threes*3 for threes in range(3,30)]
print(ThreesList)

"""
# Practice 08
"""
4-8. Cubes: A number raised to the third power is called a cube. For example,the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.
CubeList = []

for cb in range(1,10):
    cube = cb**3
    CubeList.append(cube)
    print(cube)
print(CubeList)

"""
# Practice 09

"""
4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.
CubeList = [cube**3 for cube in range(1,10)]

print(CubeList)

"""
