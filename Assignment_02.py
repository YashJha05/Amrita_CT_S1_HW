''' 
Multiple Choice Questions
1. What will be the output of the following code?
s = 'hello world'
print(s.upper())
a) hello world
b) HELLO WORLD
c) Hello World
d) Error

--> B

2. Which of the following methods is used to add an item to the end of a list?
a) add()
b) append()
c) insert()
d) extend()

--> B

3. What will be the output of the following code?
tuple1 = (1, 2, 3)
tuple1[0] = 4
a) (4, 2, 3)
b) [4, 2, 3]
c) Error
d) None of the above

--> C

4. Which method is used to remove an item from a list by its value?
a) pop()
b) remove()
c) delete()
d) discard()

--> B

5. What does the following code return?
s = 'Python Programming'
s.find('gram')
a) 4
b) 7
c) 10
d) -1

--> C
'''

'''
Fill in the Blanks
6. The __________ method is used to convert a string to lowercase. --> .lower()
7. A tuple is __________, meaning its elements cannot be changed after it is created. --> immutable
8. The __________ method returns the number of times a specified value appears in a list. --> .count()
9. The __________ method can be used to reverse the elements of a list in place. --> .reverse()
10. The __________ method returns a copy of the string with leading and trailing whitespace removed. --> .strip()
'''

'''
Programming Exercises
11. Write a Python program to find the length of a string using a built-in function.

s = input("Enter String")
print(len(s)

12. Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_elem(s):
    a = set(s)
    t = list(a)
    print(t)

13. Write a Python program to reverse a string.

s = "hello"
print(s[::-1}

14. Write a Python program to convert a tuple into a list.

s = (1, 2, 3, 4, 5)
p = list(s)

15. Write a Python program to find the maximum and minimum values in a list.

s = [1, 2, 3, 4, 5]
print(max(s))
print(min(s))

16. Write a Python program to check if a given string is a palindrome.

s = input("enter string")
p = s[::-1]
if s == p:
    print("String is Palindrome")
    
17. Write a Python function that takes a list of numbers and returns the sum of the numbers.

def ls(l1):
    x = 0
    for i in l1:
        x += i
    print(x)
    
18. Write a Python program to find the index of an item in a tuple.

s = ('a', 'b', 'c')
print(s.index('a'))

19. Write a Python program to count the occurrences of a specified element in a list.

s = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4]
print(s.count(3))

20. Write a Python function to check whether an element exists within a tuple.

def tc(a, b):
    if a in b:
        print("Element exists in tuple")
    
'''
