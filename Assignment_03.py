# Assignment 3


# 1.) Difference between Break and Continue. Illustrate with the help of a python program.

for i in range(10):
    if i < 5:
        continue
        print(i)
    elif i == 7:
        print(i)
        continue
    else:
        break

'''
In the above program, nothing will be printed. When the program starts, i takes values between 0 to 4 respectively, but even though there is a condition
of print(i) in line no. 9, it will not be executed as the continue statement reiterates the loop from that point itself. whereas, as soon as the value
of i exceeds 4, the program will straightaway break, as it is given in line no 14. There is no restarting of loop as in the case of continue statement.
Hence it should be clear that the break statement forces the system to exit the loop whereas the continue statement restarts the loop from the moment 
that statement is reached.
'''

# 2.) Print both the student’s name and their corresponding grades from the dictionary gradestudent_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

gradestudent_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
for i in gradestudent_grades.items():
    print(i)

# 3.) Add student id,name and subjects(Ask for user input) to the dictionary. Add all names to a tuple. Add all subjects to a list.

def sm():
    b = {}
    ans = input("Do you want to enter student records? enter y/n")
    while ans == "y":
        sid = input("Enter Student Id")
        name = input("Enter name")
        Subject = input("Enter Subject")
        Subjectl = []
        namel = []
        namel.append(name)
        namet = tuple(namel)
        Subjectl.append(Subject)
        record = {sid:{namet:Subjectl}}
        b.update(record)
        s = input("do you want to enter one more value? enter y/n")
        if s == "n":
            break
    print(b)

# 4.) Design a simple Python-based Library Management System that can:
    '''
    Add new books to the library.
        function: add_book() with return variables(id,title,author,quantity)
        Create a dictionary ‘library_books’ and add all the variables to the dictionary with key as id
        Register members to the library.
            function: register_member () with return variables (name, member_id)
            Create a dictionary ‘library_members’ and add all the variables to the dictionary, with key as member_id
        Check book availability.
        View issued books.
    '''

def add_book(id, title, author, quantity):
    library_books = {id : {'title' : title, 'author' : author, 'quantity' : quantity}}
    return(id, title, author, quantity, library_books)

def register_member(name, member_id):
    library_members = {member_id : {'name' : name}}
    return(name, member_id, library_members)

def check_book(id):
    # I have no idea which variable to be searched here so I'm defining an empty dictionary which would have the books
    # I'll use a similar solution for viewing issued books, where a dictionary would perhaps all the issued books
    a = {}
    if id in a:
        print("book is available")
    else:
        print("Book is unavailable")

def view_issued():
    b = {}
    print(b)

# 5.) Print numbers from 1 to 5 using while loop

a = 1
while a < 6:
    print(a)
    a += 1

# 6.) Infinite Loop with Break

while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input == 'exit':
        break
    print("You entered:", user_input)

# 7.) Sum of Numbers using while
'''
I am assuming that we need to ask the user to input a number and then we'll add all the numbers starting from 1 to the number entered
'''

num = int(input("Enter the number till whose sum you want"))
checker = 0
sum = 0
while checker != num:
    sum += checker
    checker += 1
print(sum)

# 8.) Reverse a number using for loop and while loop

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print(reverse)

num = int(input("Enter a number: "))
reverse = 0

for i in range(num):
    if num == 0:
        break
    else:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
print(reverse)
