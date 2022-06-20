# NOTE: All credit for the notes and practice exercise prompts goes to STEPHANIE SU from the Superposition Hackathon VI (2022)

# 👋 Welcome to my Intro to Python workshop! I'm so excited to introduce you to this awesome, beginner-friendly coding language.

# 💬 FYI, this grayed-out text is called a comment. It starts with a #. The interpreter (the program that reads & executes your code) will not evaluate anything when the program is run. 

# 🏃‍♀️ After you write your code, click the "Run" button to see what the result. Try with this "Hello World" line! What does it do?

#--------------------------------print("Hello World")

# 🖋 Notes: Syntax & Style
 # ❓ What is syntax? - set of rules that define how a program will be written and interpreted
 # ❓ What is style? - make code more easily readable by human eye

# 🖋 Notes: Variables
  #❓  What is a variable? - symbol to represent a value (reusable code)
  #❓  What is the syntax for defining a variable? - varName = expression or myNum = 18

# 🖋 Notes: Expressions
  #❓  What is an expression? -combination of symbols evaluated to values
  #❓  What types of expressions are there? - primitives / arithmetic / call
  #❓  How are expressions evaluated? - primitives are the same / operations or functions are subexpressions

# 🖋 Notes: Lists (Sequences)
  #❓  What is a list? - data structure that's mutable and ordered, using square brackets
  #❓  How are lists defined & indexed? - in square brackets and zero indexed (i.e. lst = ["hello", 1, 2.0] and lst[0] = "hello")
  #❓  What types of functions & operators can you use with lists? - any type
  #❓ list comprehensions [expression FOR item IN list IF condiiton] or [x for x in range(10)]
  #❓ negative indexing --> starts the end at index of -1
  #❓ splicing --> lst[-2:] prints the last 2 index values

# 🖋 Notes: Strings & Tuples (Sequences)
  #❓  What is a String? - immutable, iterable sequence of character (can loop through each char of a string; can be changed aka imutable)
  #❓  What are some String functions? - slicing, list(), 
  #❓  What is a tuple? How are they different from lists? - cannot be changed unlike lists

# 🖋 Notes: Printing
  #❓  What does print() do? - outputs to console
  #❓  How & when do I use String formatting? - newline \n tab \t escape \ to make strings look nice (i.e. print("Hello, %s! I'm %s." %(n1, n2)))

# 🖋 Notes: Functions
  #❓  What is a function? - condense actions under a single name (reusable/readable)
  #❓  What is the syntax for defining a function? --> def functName(param):
  #❓  How do I call a function after it is defined? --> funcName(arguments)

# 🖋 Notes: Logic (Control)
  #❓  What are Booleans? - true or false
  #❓  What do and, or, and not do? - and(first false value or last true value) / or(returns first true value or last false value) / not(returns opposite truth value of operand)
  #❓  What are comparison operators? --> ==, !=, >=, <=, < , >
  #❓  What are Truthy values? Provide examples. --> everything else by default (1 and true)
  #❓  What are Falsy values? Provide examples. --> empty, 0, 0.0, none, false ("" and True)

# 🖋 Notes: If Statements (Control)
  #❓  What is an if statement? - method of performing different instructions based on conditions
  #❓  What are the parts of an if statement? - if/elif/else where elif/else are optional
  #❓  How do you define an if statement? - 
  #    if(condition):
  #      return " "
  #    elif(condition2):
  #      return " "
  #    else:
  #      return " "

# 🖋 Notes: Loops (Control)
  #❓  What are loops used for? - iterating multiple times
  #❓  What is a while loop? - perform a procedure until a certain condition is not true
  #❓  What is a for loop? - performs procedure for every element in a list or a finite number of times
  #   example --> for i in list: | for i in range(10) | for i in range(1, 5, 2)

# --------------------------------EXERCISES----------------------------------------------------


# ✅ Exercise #1: Create a function that returns a list of the prime numbers up to 100
    # Use: Functions, lists, loops, if-statements, arithmetic expressions, helper function

# 🖥 🖥 🖥 CODE EXERCISE #1 HERE

def primeNumbers():
  primeNumList = []
  counter = 0
  
  for num in range(2, 100):
    if (isPrimeNumber(num)):
      primeNumList.append(num)
      counter += 1

  print("There are", counter, "prime numbers from 1 to 100.\n")
  return primeNumList

def isPrimeNumber(x): #helper function
  result = True

  for num in range(2, x):
    if(x%num) == 0:
      result = False
      break
    else:
      result = True
      
  return result

print("---- CODE EXAMPLE #1 ----")
print("Prime numbers from 1 to 100:\n", primeNumbers())
print("\n")

# ✅ Exercise #2: Create a function that prints out the n-th term in the Fibonacci sequence
    # 1, 1, 2, 3, 5, 8, 13, 21... (start n = 0)
    # Use: Assignment statements, loops, functions

# 🖥 🖥 🖥 CODE EXERCISE #2 HERE

def fibFunction(n):

  currentNum = 1 # when n = 0
  nextNum = 1
  counter = 0
  numSequence = [] 
    
  if(n <= 0):
    print("Error: please enter a positive number")
  else:
    while (counter < n):
      numSequence.append(currentNum)
      sumNum = currentNum + nextNum

      #swap / update values
      currentNum = nextNum
      nextNum = sumNum
      
      counter += 1

  print("The Fibonacci sequence for the", n, "th term: ")
  return numSequence

print("---- CODE EXERCISE #2 ----")
print(fibFunction(5))
print("\n")

# ✅ Exercise #3: Create a function prints the hailstone sequence starting at n and return its length
    # Starts with n, if previous term is odd => 3 * n + 1,
    # if previous term is even => n // 2
    # Ends at 1
    # ex. 10, 5, 16, 8, 4, 2, 1; returns 7
    # Use: Functions, variables, printing, loops, conditionals

# 🖥 🖥 🖥 CODE EXERCISE #3 HERE

def hailstone(n): #function definition
  
  print("Starting number: ", n)
  counter = 1
  print(n)
  
  while(n != 1):
    
    if (n % 2 == 0):
      n = n // 2
      print(n)
      
    else: 
      n = 3 * n + 1
      print(n)
      
    counter += 1
    
  print("Length: ", counter)
  
  return counter

print("---- CODE EXAMPLE #3 ----")
hailstone(10) #function call