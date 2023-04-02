# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print(input(f"hello_{user_name.upper()}"))
hello_name("username!")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for x in range(1,100,2):
        print(x)
    
first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
        print(max(a_list))
a_list = list(range(1,11))

max_num_in_list(a_list)

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
     if a_year % 400 == False: #a_year has to be be divisible by 400
          return True
     else:
          return False   
     if a_year % 100 != False and a_year % 4 == False:  #a_year cannot be divisble by 100 but can be divisible by 4  
          return True
     else:
          return False

a_year = 400

if(is_leap_year(a_year)):
     print(True)
else:
     print(False)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    allTrue =  True         
    i = 0
    length = len(a_list)

    while i < length - 1:
        if a_list[i] == a_list[i + 1] - 1:
            True
        else:
            False
            
            allTrue = False
        i += 1
    print(allTrue)

a_list = [1,2,3,4,5,6,7,8]

is_consecutive(a_list)
    
    

        
