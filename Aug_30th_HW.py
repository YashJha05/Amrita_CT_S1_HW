''' 
Name: Yash Jha
Subject: Computational Thinking
Date: August 30th
'''

# 1. Create a list of 5 different data types (int, float, string, etc.). Print the list.

q1 = [1, 1.4, 'a', (0,4), [1,2]]
print(q1)

# 2. Create a tuple of 4 elements. Attempt to change the third element and note the result.

#q2 = (1, 2, 3, 4)
#q2[2] = 5       

'''
line 15, in <module>
q2[2] = 5
TypeError: 'tuple' object does not support item assignment
'''

# 3. Convert the following list [5, 10, 15] into a tuple.

q3 = tuple([5, 10, 15])
print(q3)

# 4. Convert the following tuple ('a', 'b', 'c') into a list.

q4 = list(('a', 'b', 'c'))
print(q4)

# 5. Create a list with numbers from 1 to 10. Print the list and then print only the last three elements.

q5 = []
for i in range(1, 11):
    q5.append(i)
print(q5)
print(q5[-3:])

# 6. Create a tuple with 5 elements. Use slicing to print the first three elements.

q6 = (1, 2, 3, 4, 5)
print(q6[:3])

# 7. Write a program that checks if the element 'Python' exists in the tuple ('C', 'C++', 'Python', 'Java').

q7 = ('C', 'C++', 'Python', 'Java')
print('Python' in q7)

# 8. Concatenate two lists [1, 2, 3] and [4, 5, 6] and print the result.

q8 = [1, 2, 3] + [4, 5, 6]
print(q8)

# 9. Concatenate two tuples (1, 2, 3) and (4, 5, 6) and print the result.

q9 = (1, 2, 3) + (4, 5, 6)
print(q9)

# 10. Create a list of your favorite fruits and then remove the second fruit from the list.

q10 = ['apple', 'mango', 'banana', 'strawberry', 'kiwi']
q10.remove('mango')
print(q10)

# 11. Given the tuple (10, 20, 30, 40, 50), print the tuple in reverse order.

q11 = (10, 20, 30, 40, 50)
q11_1 = list(q11)
q11_1.reverse()
q11 = tuple(q11_1)
print(q11)

# 12. Create a list of 5 names. Sort the list in alphabetical order and print it.

q12 = ['Yash', 'Satya', 'Dikshant', 'Madhava', 'Arjun']
q12.sort()
print(q12)

# 13. Given the list [2, 4, 6, 8, 10], replace the third element with 7.

q13 = [2, 4, 6, 8, 10]
q13[2] = 7
print(q13)

# 14. Create a tuple with one element 'hello'. Verify the type of the variable.

q14 = 'hello', 
print(type(q14))

# 15. Write a program that counts the number of occurrences of the element 2 in the list [1, 2, 2, 3, 4, 2, 5].

q15 = [1, 2, 2, 3, 4, 2, 5]
print(q15.count(2))

# 16. Create a list of numbers and print each element using a for loop.

q16 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in q16:
    print(i)

# 17. Create a tuple with the elements ('a', 'b', 'c'). Check if 'd' is in the tuple.

q17 = ('a', 'b', 'c')
print('d' in q17)

# 18. Write a program to find the maximum and minimum numbers in a list [3, 5, 7, 2, 8].

q18 = [3, 5, 7, 2, 8]
print(max(q18))
print(min(q18))

# 19. Create a nested list with the structure [[1, 2], [3, 4], [5, 6]]. Access the element 4.

q19 = [[1, 2], [3, 4], [5, 6]]
print(q19[1][1])

# 20. Given a list of integers [10, 20, 30, 40], create a tuple where each element is the square of the corresponding element in the list.

q20 = [10, 20, 30, 40]
q20_1 = []
for i in q20:
    q20_1.append(i**2)
q20_2 = tuple(q20_1)
print(q20_2)