# Chapter 1: COMMENTS

# This line is a comment. Same with the lines above and below it.
# Any line that starts with a hashtag is as a comment and ignored
# when the program is run.


# -------------------------------------------------------------------

# Chapter 2: VARIABLES AND *THINGS*

# A word and then an equal sign and then a *thing* creates a variable
# with that *thing* as the value

# This creates a variable called name, and sets it equal to
# the String "Craig"
name = "Craig"

# Whenever the computer sees a variables, it looks at what the
# variable was set equal to, and treats it exactly like that *thing*.

# We have seen Strings as one valid *thing*, but there are many more

# A *thing* can be a Number.
age = 35

# A *thing* can be a Boolean (True or False)
is_cool = True

# Some *things* are more complicated.
# Here is a List *thing*
friends = ["Pat", "John", "Vince"]

# A List is a collection of other *things*, in the example it is a
# collection of Strings.

# We can get each of the things out of the list like this
friends[0] # Pat
friends[1] # John
friends[2] # Vince


# All these *things* (Strings, Numbers, Booleans, Lists) are built-in.
# Later we will see that we can create our own *things*.


# -------------------------------------------------------------------

# Chapter 3: CALLING METHODS

# Besides creating variables which store *things*, you can create
# methods which *do stuff*

# Some methods come built-in. An example of built-in method is `print`.

# To call a method you give it's name and then inside parenthese any
# data which the method was defined to accept.

# This passes the String "Craig" to print, which *does stuff*
# Print was made to print things to the screen.
print("Craig")

# If we run this script we will see "Craig" printed to the screen.

# Remember variables and *things* are the same.
# Instead of passing "Craig" we could pass the variable `name`
# which will result in the same thing (print "Craig" to the screen)
print(name)

# In a later chapter we will look at how to create our own methods.


# -------------------------------------------------------------------

# Chapter 4: IF STATEMENTS

# If statements allow us to only run some code if soemthing is true.

# The code that will only run if the `if` evaluates to True is
# indented under the if statement.

# Here's an example
age = 30
if age > 16:
  print("You are old enough to drive")

# The computer sees the `if` and evaluates `age > 16`. Age was set
# to 30, which is greater than 16, so it runs the code indented
# under that if statement and so "You are old enough to drive"
# is printed.

# If the code was like this with age set to 10
age = 10
if age > 16:
  print("You are old enough to drive")

# Nothing is printed. The computer sees the `if` and evaluates
# `age > 16`. Age was set to 10, which is NOT greater than 16,
# so it does NOT run the code indented under that if statement
# and so "You are old enough to drive" is NOT printed.


# The if statement can have any expression which evaluates to
# true or false.

# Expression checking if one number is GREATER THAN another
if age > 16:
  print("Age is greater than 16")

# Expression checking if one number is LESS THAN another
if age < 16:
  print("Age is less than 16")

# Expression checking if one number is EQUAL TO another
if age == 16: # notice the double equal signs
  print("Age is exactly 16")

# Expression checking if one number is LESS THAN another
if age != 16:
  print("Age is not 16")


# If statements can have an `else`.
# The `else` is ran if the if condition is not true.

# Here is an example
age = 30
if age > 16:
  print("You are old enough to drive")
else:
  print("You are too young to drive")

# The `if` statement `age > 16` is true, so
# "You are old enough to drive" is printed to the screen
# and the `else` is not run.

# However, when age is 10
age = 10
if age > 16:
  print("You are old enough to drive")
else:
  print("You are too young to drive")

# The `if` statement is false since age is NOT great than 16 and
# so the code indented under the `else` is run instead, and so
# "You are too young to drive" is printed to the screen.


# -------------------------------------------------------------------

# Chapter 5: LOOPS

# Lets say we have a list of friends
names = ["Jessica", "Alexa", "Amanda", "Susan", "Meg", "Julie"]

# We can print our friends names like this:
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

# PROBLEM: This is a lot of typing, and if we add a more
# friends we need to add more print statements.

# Instead of the above, lets loop over our friends list.
# The loop has the same output as above.
for name in names:
  print(name)

# Loops begin with `for` and then a variable name and then `in`
# and then a list (or a variable which holds a list)

# The loop runs as many times as there are *things* in the list,
# each time with the variable `friend` set to a different *thing*
# from the list, and will run the all the lines of code that are
# indented "inside" the loop


# The loop can have as much code inside it as you want.
# Any code indented under it is in the loop.
# To make this clear, here is an example:
for name in names:
  print("Hello from the beginning of the loop")
  print(name)
  print("Goodbye from the end of the loop")

print("I am outside the loop")

# This would print:
# Hello from the beginning of the loop
# Jessica
# Goodbye from the end of the loop
# Hello from the beginning of the loop
# Alexa
# Goodbye from the end of the loop
# Hello from the beginning of the loop
# Amanda
# Goodbye from the end of the loop
# Hello from the beginning of the loop
# Susan
# Goodbye from the end of the loop
# Hello from the beginning of the loop
# Meg
# Goodbye from the end of the loop
# Hello from the beginning of the loop
# Julie
# Goodbye from the end of the loop
# I am outside the loop


# -------------------------------------------------------------------

# Chapter 6: CREATING OUR OWN METHODS

# You can create your own methods.
def double(number):
  answer = number * 2
  return answer

# We have defined a `double` method which accepts one *thing* which
# we call `number`. Whatever is passed to `double` goes in this
# `number` variable.
# We then have two lines of code indented in this method. They are
# run when the method is called. First we create a variable called 
# `answer` which is the number times 2. Then we `return` the answer.

# We can now call this method
double(10) # 20

# We can capture the returned value in a variable
doubled = double(10)

# You can imagine a program like:
# print("Please enter a number and we will double it:") 
# users_number = get_number_from_user()
# doubled = double(users_number)
# print(dobuled)

# A method can accept as many *things* as you want

# Here is a method which accepts three *things*
def add_three_numbers(number1, number2, number3):
  return number1 + number2 + number3

# Here is a method which prints something mean based on an
# age
def print_mean_thing(age):
  if age > 30:
    print("You're so old!")
  else:
    print("You're a baby!")

# Unlike the other examples, this method doesn't `return`
# anything. It is not computing something that needs to be
# returned. Instead it is performing a task (printing to
# the screen.)


# -------------------------------------------------------------------

# Chapter 7: CLASSES

# Classes allow us to create our own *things*

# Lets say we wanted to print our friends names AND ages

# We have our List of names
names = ["Jessica", "Alexa", "Amanda", "Susan", "Meg", "Julie"]
# And now we need a list of ages
ages = [10, 15, 13, 17, 11, 16]

# PROBLEM: If we wanted to print their names and ages, we now have
# to loop over 2 lists. It is also confusing to see details about a
# friend split across two different lists.

# We want a single *thing* that can hold a name and age
# While this doesn't exist, we can create our own new *thing*
# for this using classes!

class Friend:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# `__init__` is a special method that is called when a new instance
# of a class is being created.

# In our case, we want to accept two piece of data `name` and `age`.
# However, we must first accept `self` which is the variable
# that holds the class instance we're creating.

# On this class instance, we attach `name` and `age`.

# We can now create a new Friend *thing* like this
Friend("Bob", 12)

# Just like all *things*, we can create a variable to hold it
friend = Friend("Bob", 12)

# We have created a new instance of our Friend class.

# We can access the name and age of this Friend instance like this
friend.name
friend.age

# Lets return to our example of wanting to print our friends
# names and ages.

# We can create a single List which has instances of our
# Friend *thing*, one for each friend.
friends = [
  Friend("Jessica", 10),
  Friend("Alexa", 15),
  Friend("Amanda", 13),
  Friend("Susan", 17),
  Friend("Meg", 11),
  Friend("Julie", 16)
]

# And then we can loop over this `friends` list and print
# the name of each `friend` using the regular built-in `print`
# method and passing `friend.name`, and then calls
# `print_mean_thing` passing in the `friend.age` to print something
# mean about the friend based on their age.
for friend in friends:
  print(friend.name)
  print_mean_thing(friend.age)


# -------------------------------------------------------------------

# Chapter 8: CLASSES (MORE)

# So far we have seen how classes can hold multiple pieces of
# data in one *thing*, like how the Friend class can hold both
# a name and age.

# But that is only half of what classes are good for.
# Classes can also hold methods.

# We've already seen how all classes have the special
# `__init__` method which is called when the class instance
# is being created.

# But we can add our own methods too.

# Lets add a method to Friend that returns whether the friend
# can drive.
class Friend:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def driving_status(self):
    if self.age > 16:
      return "I am old enough to drive!"
    else:
      return "I can't drive yet."

# Notice like with `__init__`, ALL methods must accept `self`
# as the first piece of data.

# Now, if we create a Friend instance:
friend = Friend("Bob", 12)
# Not only can we get the data back:
print(friend.name) # Bob
print(friend.age) # 12
# But we can so call our defined methods on the friend instance
status = friend.driving_status()
print(status) # I can't drive yet

# If we create a new Friend instance:
friend = Friend("Sandy", 17)
status = friend.driving_status()
print(status) # "I am old enough to drive!"